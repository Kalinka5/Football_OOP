import pytest

from exceptions.pace_exception import PaceException
from exceptions.shooting_exception import ShootingException
from exceptions.passing_exception import PassingException
from exceptions.dribbling_exception import DribblingException
from exceptions.defending_exception import DefendingException
from exceptions.physics_exception import PhysicsException

from footballer import Footballer, CentreBack, Midfielder, Forward

lower_than_zero = [
    -1,
    -5,
    -10,
    -100,
    -1000
]

higher_than_100 = [
    101,
    450,
    1000,
    10000,
    100000
]


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_pace_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", characteristic_lower_than_0, 70, 60, 70, 70, 80),
        lambda: CentreBack("John", characteristic_lower_than_0, 70, 60, 70, 70, 80),
        lambda: Midfielder("Leon", characteristic_lower_than_0, 70, 60, 70, 70, 80),
        lambda: Forward("Mike", characteristic_lower_than_0, 70, 60, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(PaceException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid pace value: {characteristic_lower_than_0}.\nPace should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_pace_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", characteristic_higher_than_100, 70, 60, 70, 70, 80),
        lambda: CentreBack("John", characteristic_higher_than_100, 70, 60, 70, 70, 80),
        lambda: Midfielder("Leon", characteristic_higher_than_100, 70, 60, 70, 70, 80),
        lambda: Forward("Mike", characteristic_higher_than_100, 70, 60, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(PaceException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid pace value: {characteristic_higher_than_100}.\n" \
                                     f"Pace should be from 0 to 100"


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_footballer_shooting_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", 70, characteristic_lower_than_0, 60, 70, 70, 80),
        lambda: CentreBack("John", 70, characteristic_lower_than_0, 60, 70, 70, 80),
        lambda: Midfielder("Leon", 70, characteristic_lower_than_0, 60, 70, 70, 80),
        lambda: Forward("Mike", 70, characteristic_lower_than_0, 60, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(ShootingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid shooting value: {characteristic_lower_than_0}.\n" \
                                     f"Shooting should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_shooting_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", 70, characteristic_higher_than_100, 60, 70, 70, 80),
        lambda: CentreBack("John", 70, characteristic_higher_than_100, 60, 70, 70, 80),
        lambda: Midfielder("Leon", 70, characteristic_higher_than_100, 60, 70, 70, 80),
        lambda: Forward("Mike", 70, characteristic_higher_than_100, 60, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(ShootingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid shooting value: {characteristic_higher_than_100}.\n" \
                                     f"Shooting should be from 0 to 100"


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_footballer_passing_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", 70, 70, characteristic_lower_than_0, 70, 70, 80),
        lambda: CentreBack("John", 70, 70, characteristic_lower_than_0, 70, 70, 80),
        lambda: Midfielder("Leon", 70, 70, characteristic_lower_than_0, 70, 70, 80),
        lambda: Forward("Mike", 70, 70, characteristic_lower_than_0, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(PassingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid passing value: {characteristic_lower_than_0}.\n" \
                                     f"Passing should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_passing_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", 70, 70, characteristic_higher_than_100, 70, 70, 80),
        lambda: CentreBack("John", 70, 70, characteristic_higher_than_100, 70, 70, 80),
        lambda: Midfielder("Leon", 70, 70, characteristic_higher_than_100, 70, 70, 80),
        lambda: Forward("Mike", 70, 70, characteristic_higher_than_100, 70, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(PassingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid passing value: {characteristic_higher_than_100}.\n" \
                                     f"Passing should be from 0 to 100"


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_footballer_dribbling_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, characteristic_lower_than_0, 70, 80),
        lambda: CentreBack("John", 70, 70, 80, characteristic_lower_than_0, 70, 80),
        lambda: Midfielder("Leon", 70, 70, 80, characteristic_lower_than_0, 70, 80),
        lambda: Forward("Mike", 70, 70, 80, characteristic_lower_than_0, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(DribblingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid dribbling value: {characteristic_lower_than_0}.\n" \
                                     f"Dribbling should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_dribbling_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, characteristic_higher_than_100, 70, 80),
        lambda: CentreBack("John", 70, 70, 80, characteristic_higher_than_100, 70, 80),
        lambda: Midfielder("Leon", 70, 70, 80, characteristic_higher_than_100, 70, 80),
        lambda: Forward("Mike", 70, 70, 80, characteristic_higher_than_100, 70, 80)
    ]
    for create_player in players:
        with pytest.raises(DribblingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid dribbling value: {characteristic_higher_than_100}.\n" \
                                     f"Dribbling should be from 0 to 100"


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_footballer_defending_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, 70, characteristic_lower_than_0, 80),
        lambda: CentreBack("John", 70, 70, 80, 70, characteristic_lower_than_0, 80),
        lambda: Midfielder("Leon", 70, 70, 80, 70, characteristic_lower_than_0, 80),
        lambda: Forward("Mike", 70, 70, 80, 70, characteristic_lower_than_0, 80)
    ]
    for create_player in players:
        with pytest.raises(DefendingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid defending value: {characteristic_lower_than_0}.\n" \
                                     f"Defending should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_defending_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, 70, characteristic_higher_than_100, 80),
        lambda: CentreBack("John", 70, 70, 80, 70, characteristic_higher_than_100, 80),
        lambda: Midfielder("Leon", 70, 70, 80, 70, characteristic_higher_than_100, 80),
        lambda: Forward("Mike", 70, 70, 80, 70, characteristic_higher_than_100, 80)
    ]
    for create_player in players:
        with pytest.raises(DefendingException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid defending value: {characteristic_higher_than_100}.\n" \
                                     f"Defending should be from 0 to 100"


@pytest.mark.parametrize("characteristic_lower_than_0", lower_than_zero)
def test_footballer_physics_lower_than_0(characteristic_lower_than_0):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, 70, 70, characteristic_lower_than_0),
        lambda: CentreBack("John", 70, 70, 80, 70, 70, characteristic_lower_than_0),
        lambda: Midfielder("Leon", 70, 70, 80, 70, 70, characteristic_lower_than_0),
        lambda: Forward("Mike", 70, 70, 80, 70, 70, characteristic_lower_than_0)
    ]
    for create_player in players:
        with pytest.raises(PhysicsException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid physics value: {characteristic_lower_than_0}.\n" \
                                     f"Physics should be from 0 to 100"


@pytest.mark.parametrize("characteristic_higher_than_100", higher_than_100)
def test_footballer_physics_higher_than_100(characteristic_higher_than_100):
    players = [
        lambda: Footballer("Tom", 70, 70, 80, 70, 70, characteristic_higher_than_100),
        lambda: CentreBack("John", 70, 70, 80, 70, 70, characteristic_higher_than_100),
        lambda: Midfielder("Leon", 70, 70, 80, 70, 70, characteristic_higher_than_100),
        lambda: Forward("Mike", 70, 70, 80, 70, 70, characteristic_higher_than_100)
    ]
    for create_player in players:
        with pytest.raises(PhysicsException) as excinfo:
            create_player()
        assert str(excinfo.value) == f"Invalid physics value: {characteristic_higher_than_100}.\n" \
                                     f"Physics should be from 0 to 100"
