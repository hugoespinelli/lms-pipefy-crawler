from dotenv import load_dotenv
from requests import Session
from retry_requests import retry
from os import getenv

load_dotenv()

SERVER_PIPEFY_API_URL = getenv("SERVER_PIPEFY_API_URL")

DELAY_PIPEFY_API_TOO_MUCH_REQUESTS = 60  # In seconds
RETRIES = 50

class PipefyService:

    def __init__(self):
        self.session = retry(Session(), retries=RETRIES, backoff_factor=DELAY_PIPEFY_API_TOO_MUCH_REQUESTS)

    def get_pipe_examination(self, table_id):
        response = self.session.get(f"{SERVER_PIPEFY_API_URL}/table/{table_id}")
        response.raise_for_status()
        return response.json()

    def get_candidates_from_pipe(self, pipe_id):
        response = self.session.get(f"{SERVER_PIPEFY_API_URL}/pipes/{pipe_id}/cards")
        response.raise_for_status()
        return response.json()

    def move_cards_ids_to_phase(self, pipe_id, cards_ids, phase_name):
        payload = {"toPhaseName": phase_name, "cardsIds": cards_ids}
        response = self.session.post(f"{SERVER_PIPEFY_API_URL}/pipes/{pipe_id}/move_cards_ids", json=payload)
        response.raise_for_status()
        return response.json()

