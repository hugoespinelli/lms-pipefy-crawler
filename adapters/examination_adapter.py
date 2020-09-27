from itertools import groupby

EXAMINATION_FIELD = "id_avaliacao_lms"


class ExaminationAdapter:

    @staticmethod
    def group_examinations_in_pipes_ids(data):
        sort_func = lambda row: row["title"]
        table_rows = list(map(lambda row: row["node"], data))
        table_rows.sort(key=sort_func)
        return {group: ExaminationAdapter.extract_examinations(elements) for group, elements in groupby(table_rows, sort_func)}

    @staticmethod
    def extract_examinations(elements):
        examinations_ids = []
        for row_data in elements:
            examination_id = ExaminationAdapter.extract_examination(row_data)
            if examination_id != "":
                examinations_ids.append(examination_id)

        return examinations_ids

    @staticmethod
    def extract_examination(row_data):
        record_fields = row_data["record_fields"]
        return list(filter(lambda record: record["name"] == EXAMINATION_FIELD, record_fields))[0]["value"]

