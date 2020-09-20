from dotenv import load_dotenv
from os import getenv

load_dotenv()

from crawlers.crawler_lms import CrawlerLMS
from services.pipefy_service import PipefyService
from adapters.user_adapter import UserAdapter
from adapters.examination_adapter import ExaminationAdapter
from services.excel_service import ExcelService

from utils import get_excel_sheet_path


TABLE_ID = getenv("TABLE_PIPEFY_ID")
CULTURE_FIT_ID = getenv("CULTURE_FIT_EXAM_ID")

PHASES_TO_CHECK = [
    "F2: Início da jornada",
    "F2: Follow up #3d",
    "F2: Follow up #2d (*)",
    "F2: Follow up #1d",
    "F2: Última Chance",
]

PHASE_TO_MOVE = "F3: Processo completo"


def run():

    print("Iniciando procura de avaliacao de candidatos...")

    pipes = ExaminationAdapter.group_examinations_in_pipes_ids(PipefyService.get_pipe_examination(TABLE_ID))

    crawler = CrawlerLMS(logger=True)

    print("Autenticando token...")
    crawler.authenticate()
    print("Autenticacao token finalizada.")

    print("Download avaliacao disk...")
    crawler.download_disk_exam()
    print("Download de avaliacao disk finalizado")
    excel_file = get_excel_sheet_path()
    print(f"Baixada planilha {excel_file}")
    excel_service = ExcelService(excel_file)

    for pipe_id, exams_ids in pipes.items():
        print(f"Pegando informacoes de candidato do pipe {pipe_id}...")
        add_culture_fit_exam(exams_ids)
        users = get_users_exams(pipe_id, exams_ids, crawler)
        excel_service.fill_completed_users_exams(users)

        cards_ids = list(map(lambda u: u.card_id, users))
        print(f"Movendo {len(cards_ids)} para a fase de {PHASE_TO_MOVE}")
        PipefyService.move_cards_ids_to_phase(pipe_id, cards_ids, PHASE_TO_MOVE)

    print("Finalizando procura de avaliacao de candidatos.")

    return True


def add_culture_fit_exam(exams_ids):
    return exams_ids.append(CULTURE_FIT_ID)


def get_users_exams(pipe_id, exams_ids, crawler):

    users = UserAdapter.transform_response_to_user(PipefyService.get_candidates_from_pipe(pipe_id))
    users = filter_user_by_phase_name(users)

    for exam_id in exams_ids:
        crawler.find_users(users, exam_id)
        print(f"Filtrando {len(users)} candidatos não completaram exames...")
        users = filter_completed_user_exams(users)
        print(f"{len(users)} restantes!")

    return users


def filter_user_by_phase_name(users):
    return list(filter(lambda user: user.current_phase in PHASES_TO_CHECK, users))


def filter_completed_user_exams(users):
    return list(filter(lambda user: user.is_approved(), users))
