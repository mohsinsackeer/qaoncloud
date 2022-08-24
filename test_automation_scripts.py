import webbrowser
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
    print(1)
    with open('testing.out', 'w') as f:
        main(f)
    print(2)
    with open('results.html', 'w') as h, open('testing.out') as t:
        result_text = list(t.readlines())
        result_text = '<br>'.join(result_text)
        h.write(f'<p>{result_text}</p>')
    print(3)

    webbrowser.open_new_tab('results.html')