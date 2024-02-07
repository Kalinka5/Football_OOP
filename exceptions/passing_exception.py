class PassingException(Exception):
    
    def __init__(self, passing, min_passing, max_passing):
        self.passing = passing
        self.min_passing = min_passing
        self.max_passing = max_passing
    

    def __str__(self):
        return f"Invalid passing value: {self.passing}.\n" \
               f"Passing should be from {self.min_passing} to {self.max_passing}"
