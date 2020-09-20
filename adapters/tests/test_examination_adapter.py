
from adapters.examination_adapter import ExaminationAdapter


def test_should_group_examinations():
    fake_response = [{
        'node': {
            'title': '301413532',
            'record_fields': [
                {
                    'name': 'id_avaliacao_lms',
                    'value': '356366'
                },
                {
                    'name': 'id_pipe',
                    'value': '["301413532"]'
                }
            ]
        }
    }, {
        'node': {
            'title': '301413532',
            'record_fields': [
                {
                    'name': 'id_avaliacao_lms',
                    'value': '356368'
                },
                {
                    'name': 'id_pipe',
                    'value': '["301413532"]'
                }
            ]
        }

    }]
    examinations_groups = ExaminationAdapter.group_examinations_in_pipes_ids(fake_response)
    assert "301413532" in examinations_groups and len(examinations_groups["301413532"]) == 2


def test_should_extract_field():
    row_data = {'title': '301413532', 'record_fields': [{'name': 'id_avaliacao_lms', 'value': '356366'}, {'name': 'id_pipe', 'value': '["301413532"]'}]}
    examination = ExaminationAdapter.extract_examination(row_data)
    assert examination == "356366"

