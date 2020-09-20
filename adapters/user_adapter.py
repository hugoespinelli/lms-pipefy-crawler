from models.user import User


class UserAdapter:

    @staticmethod
    def transform_response_to_user(response):
        return list(map(lambda card: UserAdapter.build_user(card), response))

    @staticmethod
    def build_user(card):
        node = card["node"]
        return User(node["title"], node["id"], node["current_phase"]["name"])
