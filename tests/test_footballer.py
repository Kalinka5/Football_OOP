import pytest

from footballer import Footballer, CentreBack, Midfielder, Forward


@pytest.fixture
def example_footballer_with_default_data():
    return Footballer("Daniil")


@pytest.fixture
def example_footballer_data():
    footballer = Footballer("Tom", 70, 70, 60, 70, 70, 80)
    footballer.position = "Forward"
    return footballer


@pytest.fixture
def example_centre_back_data():
    return CentreBack("Virgil")


@pytest.fixture
def example_midfielder_data():
    return Midfielder("Andres")


@pytest.fixture
def example_forward_data():
    return Forward("Kylian")


def test_get_footballer_name(example_footballer_data):
    assert example_footballer_data.name == "Tom"


def test_default_footballer_values(example_footballer_with_default_data):
    assert example_footballer_with_default_data.pace == 0
    assert example_footballer_with_default_data.shooting == 0
    assert example_footballer_with_default_data.passing == 0
    assert example_footballer_with_default_data.dribbling == 0
    assert example_footballer_with_default_data.defending == 0
    assert example_footballer_with_default_data.physics == 0


def test_improve_pace_method(example_footballer_data):
    example_footballer_data.improve_pace(10)
    assert example_footballer_data.pace == 80


def test_increasing_pace_over_100(example_footballer_data):
    example_footballer_data.improve_pace(110)
    assert example_footballer_data.pace == 100


def test_improve_shooting_method(example_footballer_data):
    example_footballer_data.improve_shooting(10)
    assert example_footballer_data.shooting == 80


def test_increasing_shooting_over_100(example_footballer_data):
    example_footballer_data.improve_shooting(110)
    assert example_footballer_data.shooting == 100


def test_improve_passing_method(example_footballer_data):
    example_footballer_data.improve_passing(10)
    assert example_footballer_data.passing == 70


def test_increasing_passing_over_100(example_footballer_data):
    example_footballer_data.improve_passing(110)
    assert example_footballer_data.passing == 100


def test_improve_dribbling_method(example_footballer_data):
    example_footballer_data.improve_dribbling(10)
    assert example_footballer_data.dribbling == 80


def test_increasing_dribbling_over_100(example_footballer_data):
    example_footballer_data.improve_dribbling(110)
    assert example_footballer_data.dribbling == 100


def test_improve_defending_method(example_footballer_data):
    example_footballer_data.improve_defending(10)
    assert example_footballer_data.defending == 80


def test_increasing_defending_over_100(example_footballer_data):
    example_footballer_data.improve_defending(110)
    assert example_footballer_data.defending == 100


def test_improve_physics_method(example_footballer_data):
    example_footballer_data.improve_physics(10)
    assert example_footballer_data.physics == 90


def test_increasing_physics_over_100(example_footballer_data):
    example_footballer_data.improve_physics(110)
    assert example_footballer_data.physics == 100


def test_footballer_getter_position(example_footballer_data):
    assert example_footballer_data.position == "Forward"


def test_footballer_setter_position(example_footballer_data):
    example_footballer_data.position = "Center Back"
    assert example_footballer_data.position == "Center Back"


def test_footballer_getter_idol(example_footballer_data):
    assert example_footballer_data.idol == "Lionel Messi"


def test_footballer_setter_idol(example_footballer_data):
    example_footballer_data.idol = "Ronaldinho"
    assert example_footballer_data.idol == "Ronaldinho"


def test_footballer_repr_method(example_footballer_data):
    assert str(example_footballer_data) == "[Footballer: Tom]"


def test_centre_back_position(example_centre_back_data):
    assert example_centre_back_data.position == "CENTRE BACK"


def test_midfielder_position(example_midfielder_data):
    assert example_midfielder_data.position == "MIDFIELDER"


def test_forward_position(example_forward_data):
    assert example_forward_data.position == "FORWARD"


def test_footballer_print_type_method(example_footballer_data, capsys):
    example_footballer_data.print_type()
    captured = capsys.readouterr()
    assert captured.out == "Footballer\n"


# testing print output
def test_footballer_speak_method(example_footballer_data, capsys):
    example_footballer_data.speak()
    captured = capsys.readouterr()
    assert captured.out == "I`m Tom and I`m the best Forward in the world!\n"


def test_footballer_print_idol_method(example_footballer_data, capsys):
    example_footballer_data.print_idol()
    captured = capsys.readouterr()
    assert captured.out == "My favourite footballer is Lionel Messi.\n"
