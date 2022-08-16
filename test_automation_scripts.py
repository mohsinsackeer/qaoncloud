import unittest
import sys
from automate1 import auto1
from automate2 import auto2


# from app1 import app as flaskApp1
# from app2 import app as flaskApp2

class TestMyAutomation(unittest.TestCase):

    def test_automation1(self):
        auto1()

    def test_automation2(self):
        auto2()


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromTestCase(TestMyAutomation)
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    # unittest.main()
    with open('testing.out', 'w') as f:
        main(f)
