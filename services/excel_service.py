import openpyxl

from models.examination import Examination

ACTIVE_SHEET = "Sheet1"


class ExcelService:

    def __init__(self, filename):
        self.workbook = self.load(filename)

    def load(self, filename):
        return openpyxl.load_workbook(filename)

    def get_users_email(self):
        ws = self.workbook[ACTIVE_SHEET]
        emails_column = ws["H"]
        return {cell.value: True for cell in emails_column}

    def fill_completed_users_exams(self, users):

        emails_completed_exams = self.get_users_email()

        for user in users:

            if user.email in emails_completed_exams:
                user.add_examination(Examination(105435, 100, is_completed=True))
            else:
                user.add_examination(Examination(105435, 0, is_completed=False))

        return users

