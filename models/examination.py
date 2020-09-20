

class Examination:

    def __init__(self, id, score=0, is_completed=False):
        self.id = id
        self.score = score
        self.is_completed = is_completed

    def is_approved(self):
        return self.score > 0 and self.is_completed
