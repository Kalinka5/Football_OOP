#  make class exception to pace characteristic
class PaceException(Exception):
    #  init pace, minimal pace and maximum pace 
    def __init__(self, pace, min_pace, max_pace):
        self.pace = pace
        self.min_pace = min_pace
        self.max_pace = max_pace
    
    #  print exception 
    def __str__(self):
        return f"Invalid pace value: {self.pace}.\n" \
               f"Pace should be from {self.min_pace} to {self.max_pace}"
