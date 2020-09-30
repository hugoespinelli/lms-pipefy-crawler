

class Examination:

    def __init__(self, id, score=0, is_completed=False, min_score=0):
        self.id = id
        self.score = score
        self.min_score = min_score
        self.is_completed = is_completed

    def is_approved(self):
        return self.score >= self.min_score and self.is_completed

    def __repr__(self):
        return f"<Examination id={self.id}, score={self.score}, is_completed={self.is_completed}, min_score={self.min_score}>"
