

class User:

    def __init__(self, email, card_id, current_phase):
        self.email = email
        self.card_id = card_id
        self.current_phase = current_phase
        self.examinations = []

    def add_examination(self, examination):
        self.examinations.append(examination)

    def is_approved(self):
        return all(map(lambda exam: exam.is_approved(), self.examinations))

    def __repr__(self):
        return f"<User email={self.email} card_id={self.card_id} is_approved={self.is_approved()}>"
