import unittest
from app import add
class test_app(unittest.TestCase):
    def Test_add(self):
        self.asserEqual(add(2,3),5)
        self.assertEqual(add(1,3),4)

        self.asserEqual(add(12,13),25)
        self.asserEqual(add(5,5),10)
        self.asserEqual(add(6,6),12)
        if __name__=='__main__':
            unittest.main()
