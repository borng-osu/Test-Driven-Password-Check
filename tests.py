import unittest
from check_pwd import check_pwd


class Testcase(unittest.TestCase):

    def test1(self):
        # Tests if string of valid length returns True
        pwd = "abc123#$%ABC"
        self.assertEqual(check_pwd(pwd), True,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test2(self):
        # Tests if string without symbol returns False
        pwd = "abc123ABC"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))

    def test3(self):
        # Tests if string without lowercase letter returns False
        pwd = "$$$123ABC"
        self.assertEqual(check_pwd(pwd), False,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
