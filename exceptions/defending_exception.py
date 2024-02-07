class DefendingException(Exception):

    def __init__(self, defending, min_defending, max_defending):
        self.defending = defending
        self.min_defending = min_defending
        self.max_defending = max_defending
    

    def __str__(self):
        return f"Invalid defending value: {self.defending}.\n" \
               f"Defending should be from {self.min_defending} to {self.max_defending}"
