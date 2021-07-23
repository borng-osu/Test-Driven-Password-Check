import unittest
from check_pwd import check_pwd


class Testcase(unittest.TestCase):

    def test1(self):
        # Tests if string of valid length returns True
        pwd = "abc123#$%ABC"
        self.assertEqual(check_pwd(pwd), True,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test2(self):
        # Tests if string without symbols returns False
        pwd = "abc123ABC"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test3(self):
        # Tests if string without lowercase letters returns False
        pwd = "$$$123ABC"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test4(self):
        # Tests if string without uppercase letters returns False
        pwd = "$$$123abc"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test5(self):
        # Tests if string without digits returns False
        pwd = "$$$ABCabc"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test6(self):
        # Tests if string of 20 characters returns True
        pwd = "aB%12345ab1234567890"
        self.assertEqual(check_pwd(pwd), True,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
