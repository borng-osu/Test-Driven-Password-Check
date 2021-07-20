import unittest
from check_pwd import check_pwd


class Testcase(unittest.TestCase):

    def test1(self):
        # Test if string of valid length returns True
        pwd = "abc123#$%ABC"
        self.assertEqual(check_pwd(pwd), True,
                         msg='{} returned {}'.format(pwd, check_pwd(pwd)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
