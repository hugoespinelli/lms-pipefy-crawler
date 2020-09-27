from itertools import groupby

EXAMINATION_FIELD = "id_avaliacao_lms"


class ExaminationAdapter:

    @staticmethod
    def group_examinations_in_pipes_ids(data):
        sort_func = lambda row: row["title"]
        table_rows = list(map(lambda row: row["node"], data))
        table_rows.sort(key=sort_func)
        return {group: list(map(ExaminationAdapter.extract_examination, elements)) for group, elements in groupby(table_rows, sort_func)}

    @staticmethod
    def extract_examination(row_data):
        record_fields = row_data["record_fields"]
        examination_ids = list(filter(lambda record: record["name"] == EXAMINATION_FIELD, record_fields))[0]["value"]
        return examination_ids if "" not in examination_ids else []

