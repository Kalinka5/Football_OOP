from exceptions.pace_exception import PaceException
from exceptions.shooting_exception import ShootingException
from exceptions.passing_exception import PassingException
from exceptions.dribbling_exception import DribblingException
from exceptions.defending_exception import DefendingException
from exceptions.physics_exception import PhysicsException


def pace_checking(pace):
    min_pace, max_pace = 0, 100
    if min_pace <= pace <= max_pace:
        return pace
    else:
        raise PaceException(pace, min_pace, max_pace)


def shooting_checking(shooting):
    min_shooting, max_shooting = 0, 100
    if min_shooting <= shooting <= max_shooting:
        return shooting
    else:
        raise ShootingException(shooting, min_shooting, max_shooting)


def passing_checking(passing):
    min_passing, max_passing = 0, 100
    if min_passing <= passing <= max_passing:
        return passing
    else:
        raise PassingException(passing, min_passing, max_passing)


def dribbling_checking(dribbling):
    min_dribbling, max_dribbling = 0, 100
    if min_dribbling <= dribbling <= max_dribbling:
        return dribbling
    else:
        raise DribblingException(dribbling, min_dribbling, max_dribbling)


def defending_checking(defending):
    min_defending, max_defending = 0, 100
    if min_defending <= defending <= max_defending:
        return defending
    else:
        raise DefendingException(defending, min_defending, max_defending)


def physics_checking(physics):
    min_physics, max_physics = 0, 100
    if min_physics <= physics <= max_physics:
        return physics
    else:
        raise PhysicsException(physics, min_physics, max_physics)