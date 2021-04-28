import unittest
import json
import main

class Test_test_1(unittest.TestCase):
    '''Unit test class
    '''

    def test_check_standard_file(self):
        '''test method check_standard_file()
        '''
        with open('standard_definition.json') as f:
            standard=json.load(f)

        self.assertEqual([['L1', 'L11', 'digits', 'digits', 1, 1, 'E01'], ['L1', 'L12', 'word_characters', 'word_characters', 2, 3, 'E01'],
                         ['L1', 'L13', '', 'word_characters', '', 2, 'E05']],
                         main.check_standard_file(['L1', '1', 'AB'],standard))
        self.assertNotEqual([['L11', 'L11', 'digits', 'digits', 1, 1, 'E01'], ['L1', 'L12', 'word_characters', 'word_characters', 2, 3, 'E01'],
                            ['L1', 'L13', '', 'word_characters', '', 2, 'E05']],
                         main.check_standard_file(['L1', '1', 'AB'],standard))
    def test_check_sub_sections(self):
        self.assertEqual({'key': 'L11', 'data_type': 'digits', 'max_length': 1},main.check_sub_sections('1',0,0))
        self.assertNotEqual({'key': 'L44', 'data_type': 'digits', 'max_length': 1},main.check_sub_sections('1',0,0))
if __name__ == '__main__':
        unittest.main(verbosity=1) # run unit-test
