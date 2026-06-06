import unittest
from employee import Employee
from unittest.mock import patch
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # RUNS BEFORE EVERY TESTS
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('vivek', 'suyal', 50000)
        self.emp_2 = Employee('yogesh', 'suyal', 60000)
    #  RUNS AFTER EVERY TEST
    def tearDown(self):
        print('tearDown\n')
        pass
    #self. def test_email(self):
    #     emp_1 = Employee('vivek','suyal',10000)
    #     emp_2 = Employee('yogesh','suyal',20000)
    #     self.assertEqual(emp_1.email,'vivek.suyal@gmail.com')
    #     self.assertEqual(emp_2.email,'yogesh.suyal@gmail.com')
    #     emp_1.first='john'
    #     emp_2.last='sharma'
    #     self.assertEqual(emp_1.email,'john.suyal@gmail.com')
    #     self.assertEqual(emp_2.email,'yogesh.sharma@gmail.com')
    # def test_fullname(self):
    #     emp_1 = Employee('vivek','rana',10000)
    #     emp_2 = Employee('yogesh','rana',1000)
    #     self.assertEqual(emp_1.fullname,'vivek rana')
    #     self.assertEqual(emp_2.fullname,'yogesh rana')
    #     emp_1.first='ayush'
    #     self.assertEqual(emp_1.fullname,'ayush rana')
    #
    #
    # def test_apply_raise(self):
    #     emp_1 = Employee('anand','suyal',50000)
    #     emp_2 = Employee('neeraj','suyal',60000)
    #     emp_1.apply_raise()
    #     emp_2.apply_raise()
    #     self.assertEqual(emp_1.pay,52500)
    #
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'vivek.suyal@gmail.com')
        self.assertEqual(self.emp_2.email, 'yogesh.suyal@gmail.com')
        self.emp_1.first = 'john'
        self.emp_2.last = 'sharma'
        self.assertEqual(self.emp_1.email, 'john.suyal@gmail.com')
        self.assertEqual(self.emp_2.email, 'yogesh.sharma@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'vivek suyal')
        self.assertEqual(self.emp_2.fullname, 'yogesh suyal')
        self.emp_1.first = 'ayush'
        self.assertEqual(self.emp_1.fullname, 'ayush suyal')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok= True
            mocked_get.return_value.text= 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/suyal/May')
            self.assertEqual(schedule,'Success')




if __name__ == '__main__':
    unittest.main()


# test doesn't run in order
# test should be isolated