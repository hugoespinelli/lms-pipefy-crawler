from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

SERVER_PIPEFY_API_URL = getenv("SERVER_PIPEFY_API_URL")


class PipefyService:

    @staticmethod
    def get_pipe_examination(table_id):
        response = requests.get(f"{SERVER_PIPEFY_API_URL}/table/{table_id}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_candidates_from_pipe(pipe_id):
        response = requests.get(f"{SERVER_PIPEFY_API_URL}/pipes/{pipe_id}/cards")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def move_cards_ids_to_phase(pipe_id, cards_ids, phase_name):
        payload = {"toPhaseName": phase_name, "cardsIds": cards_ids}
        response = requests.post(f"{SERVER_PIPEFY_API_URL}/pipes/{pipe_id}/move_cards_ids", json=payload)
        response.raise_for_status()
        return response.json()

