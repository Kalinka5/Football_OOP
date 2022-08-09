#  make class exception to pace characteristic
class Pace_exception(Exception):
    #  init pace, minimal pace and maximum pace 
    def __init__(self, pace, minpace, maxpace):
        self.pace = pace
        self.minpace = minpace
        self.maxpace = maxpace
    
    #  print exception 
    def __str__(self):
        return f"Invalid value: {self.pace}. " \
               f"Pace should be from {self.minpace} to {self.maxpace}"
