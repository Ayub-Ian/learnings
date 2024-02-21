import unittest
import string
def removeWhite(s):
    if len(s) == 0:
        return ''
    elif s[0] in string.whitespace or s[0] in string.punctuation:
        return removeWhite(s[1:])
    else:
        return s[0] + removeWhite(s[1:])

def isPal(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return isPal(s[1:len(s)-1])
        
    return False
    
class TestPalindromeFunction(unittest.TestCase):
    def test_isPal(self):
        self.assertEqual(isPal(removeWhite("x")), True)
        self.assertEqual(isPal(removeWhite("radar")), True)
        self.assertEqual(isPal(removeWhite("hello")), False)
        self.assertEqual(isPal(removeWhite("")), True)
        self.assertEqual(isPal(removeWhite("hannah")), True)
        self.assertEqual(isPal(removeWhite("madam i'm adam")), True)
        
if __name__ == '__main__':
    unittest.main()