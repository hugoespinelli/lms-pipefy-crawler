
from services.excel_service import ExcelService
from pytest import fixture


@fixture
def excel_service():
    filename = "Avaliacao-DISC_stat_20200916.xlsx"
    return ExcelService(filename)


def test_should_get_users(excel_service):
    users_dict = excel_service.get_users_email()
    assert len(users_dict.keys()) > 0



