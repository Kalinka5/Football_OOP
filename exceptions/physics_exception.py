class PhysicsException(Exception):

    def __init__(self, physics, min_physics, max_physics):
        self.physics = physics
        self.min_physics = min_physics
        self.max_physics = max_physics
    
 
    def __str__(self):
        return f"Invalid physics value: {self.physics}.\n" \
               f"Physics should be from {self.min_physics} to {self.max_physics}"
