import sys

sys.path.append('../automation_scripts')

from automate1 import auto1
from automate2 import auto2
import webbrowser
import unittest


# from app1 import app as flaskApp1
# from app2 import app as flaskApp2

class TestMyAutomation(unittest.TestCase):

    def test_automation1(self):
        auto1(path='chromedriver.exe')

    def test_automation2(self):
        auto2(path='chromedriver.exe')


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromTestCase(TestMyAutomation)
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    # unittest.main()
    print(1)
    with open('test_result.out', 'w') as f:
        main(f)
    print(2)
    with open('test_result.html', 'w') as h, open('test_result.out') as t:
        result_text = list(t.readlines())
        result_text = '<br>'.join(result_text)
        h.write(f'<p>{result_text}</p>')
    print(3)

    webbrowser.open_new_tab('test_result.html')
