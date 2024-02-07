import unittest

from footballer import Footballer


class TestFootballer(unittest.TestCase):

    def setUp(self) -> None:
        self.footballer = Footballer("Lionel")
        self.footballer.position = "Centre back"

    def test_get_name(self):
        self.assertEqual(self.footballer.name, "Lionel")

    def test_default_class_values(self):
        self.assertEqual(self.footballer.pace, 0)
        self.assertEqual(self.footballer.shooting, 0)
        self.assertEqual(self.footballer.passing, 0)
        self.assertEqual(self.footballer.dribbling, 0)
        self.assertEqual(self.footballer.defending, 0)
        self.assertEqual(self.footballer.physics, 0)

    def test_getter_position(self):
        self.assertEqual(self.footballer.position, "Centre back")

    def test_setter_position(self):
        self.footballer.position = "Goalkeeper"
        self.assertEqual(self.footballer.position, "Goalkeeper")

    def test_getter_idol(self):
        self.assertEqual(self.footballer.idol, "Lionel Messi")

    def test_setter_idol(self):
        self.footballer.idol = "Ronaldinho"
        self.assertEqual(self.footballer.idol, "Ronaldinho")


if __name__ == '__main__':
    unittest.main()
