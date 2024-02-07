class DribblingException(Exception):

    def __init__(self, dribbling, min_dribbling, max_dribbling):
        self.dribbling = dribbling
        self.min_dribbling = min_dribbling
        self.max_dribbling = max_dribbling


    def __str__(self):
        return f"Invalid dribbling value: {self.dribbling}.\n" \
               f"Dribbling should be from {self.min_dribbling} to {self.max_dribbling}"
