import unittest, math, random, json, pltest
from pltest import name, points
from contextlib import redirect_stdout
#import student_code
import sys
from io import StringIO
import contextlib
import traceback

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

qJson = pltest.getQuestionJson()

class Test(unittest.TestCase):
    @points(10)
    @name('')
    def test(self):
        expected = qJson['params']['result'] #Might be replaced automatically
        f = open("student_code.py", "r")
        studentAns = """
y = {}
print({})
""".format(eval(f.read().split("\n")[2]), qJson['params']['expression']).strip()
        with stdoutIO() as s:
            try:
                exec(studentAns)
            except:
                traceback.print_exc()
        self.assertEqual(eval(str(s.getvalue().strip())), eval(str(expected)))