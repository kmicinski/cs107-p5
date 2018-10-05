# Public tests for project 5
import unittest
from stacks import *

# Note that this function takes a lambda as its argument.  It
# executes that lambda and--if it returns without an
# exception--this function returns False, otherwise this returns
# True.
def raises(f):
    try:
        f()
        return False
    except Exception:
        return True

class TestStacks(unittest.TestCase):
    # Write more tests here
    def test_push(self):
        s = make_stack(2)
        push(s,1)
        self.assertEqual(s[0], 1)
        self.assertEqual(s[1], [1, None])
        self.assertEqual(s[2], 2)
        push(s,2)
        self.assertEqual(s[0], 2)
        self.assertEqual(s[1], [1, 2])
        self.assertEqual(s[2], 2)
        push(s,3)
        self.assertEqual(s[0], 3)
        self.assertEqual(s[1], [1, 2, 3, None])
        self.assertEqual(s[2], 4)

    def test_copyStackA(self):
        ex1 = [1, [235], 1]
        x = copyStack(ex1)
        self.assertEqual(x[2], 1)

    def test_copyStackB(self):
        ex1 = [1, [235], 1]
        x = copyStack(ex1)
        self.assertEqual(x[0], 1)

    def test_pop(self):
        ex1 = [1, [235], 1]
        self.assertEqual(pop(ex1), 235)

    def test_toArray(self):
        ex1 = [1, [235], 1]
        self.assertEqual(toArray(ex1),[235])

    def test_reverse(self):
        ex1 = [2, [1,2], 2]
        reverse(ex1)
        self.assertEqual(ex1[1], [2,1])

    def test_merge(self):
        x = [2, [1,3, None, None], 4]
        merge(x,[1,[2],1])
        self.assertEqual(x[1], [1,2,3,None])
        self.assertEqual(x[0], 3)

unittest.main()
