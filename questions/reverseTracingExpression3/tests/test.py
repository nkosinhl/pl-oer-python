import numpy as np
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase

class Test(PLTestCase):
    
    @points(10)
    @name("A Test Case")
    def test(self):
        expected = 7 # self.data.params.result
        user_val = 7 # self.data.submitted_answers.y
#        code_to_run = f"def f(y):\n   {self.data.params.expression}   return x"
#        user_val = Feedback.call_user(code_to_run, self.data.submitted_answers.y)
#        if Feedback.check_scalar("", expected, user_val):
        if Feedback.check_scalar("Testing", expected, user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)


## import unittest, math, random, json, pltest
## from pltest import name, points
## from contextlib import redirect_stdout
## #import student_code
## import sys
## from io import StringIO
## import contextlib
## import traceback

## @contextlib.contextmanager
## def stdoutIO(stdout=None):
##     old = sys.stdout
##     if stdout is None:
##         stdout = StringIO()
##         sys.stdout = stdout
##         yield stdout
##         sys.stdout = old
## 
## qJson = pltest.getQuestionJson()
## 
## class Test(unittest.TestCase):
##     @points(10)
##     @name('')
##     def test(self):
##         expected = qJson['params']['result'] #Might be replaced automatically
##         f = open("student_code.py", "r")
##         studentAns = """
## y = {}
## print({})
## """.format(eval(f.read().split("\n")[2]), qJson['params']['expression']).strip()
##         with stdoutIO() as s:
##             try:
##                 exec(studentAns)
##             except:
##                 traceback.print_exc()
##         self.assertEqual(eval(str(s.getvalue().strip())), eval(str(expected)))
