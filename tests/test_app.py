import unittest

from app import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_uses_default_name(self):
        self.assertEqual(greeting(), "Ahoj, svet!")

    def test_greeting_uses_provided_name(self):
        self.assertEqual(greeting("Kamil"), "Ahoj, Kamil!")


if __name__ == "__main__":
    unittest.main()
