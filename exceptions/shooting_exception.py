class ShootingException(Exception):
    
    def __init__(self, shooting, min_shooting, max_shooting):
        self.shooting = shooting
        self.min_shooting = min_shooting
        self.max_shooting = max_shooting
    
    #  print exception 
    def __str__(self):
        return f"Invalid shooting value: {self.shooting}.\n" \
               f"Shooting should be from {self.min_shooting} to {self.max_shooting}"
