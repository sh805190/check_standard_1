import unittest
from check_and_summary import check_and_summary
from check import check

class Test_test_1(unittest.TestCase):
    '''Unit test class
    '''

    def test_check_definition(self):
        '''test method check_definition()
        '''
        self.assertEqual([['L1', 'L11', 'digits', 'digits', 1, 1, 'E01'], ['L1', 'L12', 'word_characters', 'word_characters', 2, 3, 'E01'], 
                          ['L1', 'L13', '', 'word_characters', '', 2, 'E05']],
                         check_and_summary.check_definition(['L1', '1', 'AB']))
        self.assertNotEqual([['L2', 'L11', 'digits', 'digits', 1, 1, 'E01'], ['L1', 'L12', 'word_characters', 'word_characters', 2, 3, 'E01'], 
                             ['L1', 'L13', '', 'word_characters', '', 2, 'E05']],
                         check_and_summary.check_definition(['L1', '1', 'AB']))
    def test_check_sub_sectionsL11(self):
        '''test method check_sub_sectionsL11()
        '''
        self.assertEqual(['L1','L11','digits','digits',1,1,'E01','L11 field under segment L1 passes all the validation criteria.'],check.check_sub_sectionsL11('1'))
        self.assertNotEqual(['L1','L11','digits','digits',1,1,'E01','L11 field under segment L1 passes all the validation criteria.'],check.check_sub_sectionsL11('1asad'))
if __name__ == '__main__':
        unittest.main(verbosity=1) # run unit-test
