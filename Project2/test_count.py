
import unittest
from count import count_letter  # import the method from count.py

class CountTest(unittest.TestCase):
    def test_remove_case(self):
        remove_case = True
        selected_count_word = None
        fill_zero = False
        file_list = ["a.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'a': 2, 'b': 4, 'c': 8} == data
        # print("test_remove_case success")


    def test_not_remove_case(self):
        remove_case = False
        selected_count_word = None
        fill_zero = False
        file_list = ["a.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'A': 2, 'B': 4, 'b': 8, 'a': 16, 'c': 32} == data
        # print("test_not_remove_case success")

    def test_select_word(self):
        remove_case = False
        selected_count_word = ["a"]
        fill_zero = False
        file_list = ["a.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'A': 3, 'a': 2} == data
        # print("test_select_word success")


    def test_multi_file_and_selected_count_word(self):
        remove_case = False
        selected_count_word = ["a"]
        fill_zero = False
        file_list = ["a.txt","b.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'A': 2, 'a': 4} == data
        # print("test_multi_file_and_selected_count_word success")



    def test_multi_file_and_selected_count_word_and_remove_case(self):
        remove_case = True
        selected_count_word = ["a"]
        fill_zero = False
        file_list = ["a.txt","b.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'a': 8} == data
        # print("test_multi_file_and_selected_count_word_and_remove_case success")



    def test_multi_file_and_selected_count_word_and_remove_case_and_fill_zero(self):
        remove_case = True
        selected_count_word = ["a","b","c"]
        fill_zero = True
        file_list = ["a.txt","b.txt"]
        data = count_letter(remove_case, selected_count_word, fill_zero, file_list)
        print(data)
        # assert {'a': 8, 'b': 16, 'c': 2} == data
        # print("test_multi_file_and_selected_count_word_and_remove_case_and_fill_zero success")


if __name__ == '__main__':
    unittest.main()
    print("tests succeed")
