import unittest

from footballer import Footballer


class TestFootballer(unittest.TestCase):

    def setUp(self) -> None:
        self.footballer = Footballer("Lionel")

    def test_get_name(self):
        self.assertEqual(self.footballer.name, "Lionel")

    def test_default_class_values(self):
        self.assertEqual(self.footballer.pace, 0)
        self.assertEqual(self.footballer.shooting, 0)
        self.assertEqual(self.footballer.passing, 0)
        self.assertEqual(self.footballer.dribbling, 0)
        self.assertEqual(self.footballer.defending, 0)
        self.assertEqual(self.footballer.physics, 0)


if __name__ == '__main__':
    unittest.main()
