import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re

from models.examination import Examination

from os import getenv
from dotenv import load_dotenv
load_dotenv()


DISK_EXAM_URL = getenv("DISC_EXAM_URL")
EASY_LMS_AUTH = "https://www.easy-lms.com/pt/entrar/item114"
EASY_LMS_PROVAS = "https://www.easy-lms.com/pt/meu-painel-de-controle/provas/prova/analisar/resultados/item10439?id={examination}"


SCRIPT_PATH = getenv("SCRIPT_PATH")

class CrawlerLMS:

    def __init__(self, *, logger=False):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": SCRIPT_PATH,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.logger = logger

    def authenticate(self):
        self.driver.get(EASY_LMS_AUTH)

        input_login = self.driver.find_element_by_name("LoginForm[email]")
        input_password = self.driver.find_element_by_name("LoginForm[password]")

        input_login.send_keys(getenv("EASY_LMS_EMAIL"))
        input_password.send_keys(getenv("EASY_LMS_PASSWORD"))

        input_password.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(20)

    def find_users(self, users, examination_id):
        self.get_in_user_page(examination_id)
        return [self.find_user(user, examination_id) for user in users]

    def get_in_user_page(self, examination_id):
        self._log(f"Entrando na pagina da avaliacao de id {examination_id}")
        url = EASY_LMS_PROVAS.format(examination=examination_id)
        self.driver.get(url)

    def find_user(self, user, examination_id):
        self._log(f"Procurando usuario {user.email}")
        participant_input_filter = self.driver.find_element_by_name("Result[participantFilter]")
        participant_input_filter.clear()
        participant_input_filter.send_keys(user.email)
        participant_input_filter.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(5)
        time.sleep(5)

        users_table_body = self.driver.find_element_by_xpath('//*[@id="w0"]/table/tbody')
        trs = users_table_body.find_elements_by_tag_name('tr')

        tr = trs[0]

        if not self.is_user_found(tr) or not self.is_user_found_matched_with_username(user.email):
            self._log(f"Avaliacao não encontrada!")
            user.add_examination(Examination(examination_id, 0))
            return user

        tds = tr.find_elements_by_tag_name('td')
        for td in tds:
            percentage = self.extract_percentage_completed(td.text)

            if percentage is not None:
                self._log(f"Avaliacao encontrada! Percentual: {percentage}!")
                user.add_examination(Examination(examination_id, percentage, is_completed=True))
                break

        return user

    def is_user_found(self, tr):
        return len(tr.find_elements_by_tag_name('td')) > 1

    def is_user_found_matched_with_username(self, username):
        try:
            my_element = self.driver.find_element_by_xpath(f"//a[text()='{username}']")
            return True
        except Exception as e:
            return False

    def extract_percentage_completed(self, text):
        match = re.search(r"(\d+)%", text)
        if match is None:
            return None
        return int(match.group(1))

    def end(self):
        self.driver.close()

    def download_disk_exam(self):
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.get(DISK_EXAM_URL)
        self.driver.implicitly_wait(20)
        time.sleep(20)

    def _log(self, message):
        if self.logger:
            print(message)


