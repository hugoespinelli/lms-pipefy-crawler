from itertools import groupby
from models.examination import Examination

EXAMINATION_FIELD = "id_avaliacao_lms"


class ExaminationAdapter:

    @staticmethod
    def group_examinations_in_pipes_ids(data):
        sort_func = lambda row: row["title"]
        table_rows = list(map(lambda row: row["node"], data))
        table_rows.sort(key=sort_func)
        return {group: ExaminationAdapter.extract_examinations(list(elements)) for group, elements in groupby(table_rows, sort_func)}

    @staticmethod
    def extract_examinations(elements):
        examinations = []
        for row_data in elements:
            examination_dict = ExaminationAdapter.extract_examination(row_data)
            if EXAMINATION_FIELD in examination_dict and examination_dict[EXAMINATION_FIELD] != "":
                examinations.append(Examination(
                    id=examination_dict[EXAMINATION_FIELD],
                    min_score=0
                ))

        return examinations

    @staticmethod
    def extract_examination(row_data):
        record_fields = row_data["record_fields"]
        return {record["name"]: record["value"] for record in record_fields}

