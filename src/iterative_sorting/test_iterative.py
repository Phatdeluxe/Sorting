import unittest
import random
from iterative_sorting import *

class IterativeSortingTest(unittest.TestCase):
    def test_selection_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)
        print('Test 1')
        self.assertEqual(selection_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        print('Test 2')
        self.assertEqual(selection_sort(arr2), [])
        print('Test 3')
        self.assertEqual(selection_sort(arr3), [0,1,2,3,4,5])
        print('Test 4')
        self.assertEqual(selection_sort(arr4), sorted(arr4))

    def test_bubble_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)

        print('Test 5')
        self.assertEqual(bubble_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        print('Test 6')
        self.assertEqual(bubble_sort(arr2), [])
        print('Test 7')
        self.assertEqual(bubble_sort(arr3), [0,1,2,3,4,5])
        print('Test 8')
        self.assertEqual(bubble_sort(arr4), sorted(arr4))

    # Uncomment this test to test your count_sort implementation
    # def test_counting_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [1, 5, -2, 4, 3]
    #     arr4 = random.sample(range(200), 50)

    #     self.assertEqual(count_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(count_sort(arr2), [])
    #     self.assertEqual(count_sort(arr3), "Error, negative numbers not allowed in Count Sort")
    #     self.assertEqual(count_sort(arr4), sorted(arr4))


if __name__ == '__main__':
    unittest.main()
