
from adapters.user_adapter import UserAdapter
from models.user import User


def test_should_change_response_to_user():
    response = [{"node": {
        "id": "384138764",
        "title": "eded@gmail.com",
        "current_phase": {
            "id": "309413156",
            "name": "F1: Cadastro completo"
        },
        "fields": [
            {
                "field": {
                    "id": "voc_tem_disponibilidade_para_trabalhar_presencialmente_no_munic_pio_de_rio_grande_rs"
                },
                "name": "Você tem disponibilidade em trabalhar XXX?",
                "value": "Sim",
                "array_value": None,
                "float_value": None
            },
            {
                "field": {
                    "id": "com_o_seu_n_vel_de_conhecimento_em_php"
                },
                "name": "Qual o seu nível de experiência com XXX?",
                "value": "Médio",
                "array_value": None,
                "float_value": None
            },
            {
                "field": {
                    "id": "qual_seu_n_vel_de_conhecimento_em_negocia_o"
                },
                "name": "Qual o seu nível de conhecimento em XXX?",
                "value": "Médio",
                "array_value": None,
                "float_value": None
            },
            {
                "field": {
                    "id": "telefone"
                },
                "name": "Telefone",
                "value": "+55 11 97232-4310",
                "array_value": None,
                "float_value": None
            },
            {
                "field": {
                    "id": "email_de_cadastro"
                },
                "name": "Email de cadastro",
                "value": "eded@gmail.com",
                "array_value": None,
                "float_value": None
            },
            {
                "field": {
                    "id": "nome"
                },
                "name": "Nome",
                "value": "teste",
                "array_value": None,
                "float_value": None
            }
        ],
        "due_date": None,
        "late": True,
        "createdAt": "2020-09-09T08:52:20-03:00",
        "child_relations": [
            {
                "cards": [],
                "name": "Informações de cadastro",
                "pipe": {
                    "id": "1175536",
                    "name": ".Startec Jobs"
                },
                "source_type": "PipeRelation"
            }
        ],
        "phases_history": [
            {
                "phase": {
                    "name": "Start form",
                    "id": "309413150"
                }
            },
            {
                "phase": {
                    "name": "F1: Inscrito na vaga",
                    "id": "309413151"
                }
            },
            {
                "phase": {
                    "name": "F1: Completar cadastro",
                    "id": "309413152"
                }
            },
            {
                "phase": {
                    "name": "F1: Cadastro completo",
                    "id": "309413156"
                }
            }
        ],
        "labels": [
            {
                "id": "304720121",
                "name": "Potencial"
            }
        ]
    }
    }]

    users = UserAdapter.transform_response_to_user(response)
    assert len(users) > 0 and isinstance(users[0], User)







