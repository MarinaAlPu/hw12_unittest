import unittest
from utils import arrs


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 2, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], 3), 'мир вашему дому')
        self.assertEqual(arrs.get(['f', 'b', 5], -1, "test"), "test")
        self.assertEqual(arrs.get([1, 2.56, 'мама'], 93, "test"), "test")
        self.assertEqual(arrs.get([], 0, "homework 12.2"), "homework 12.2")
        self.assertEqual(arrs.get([], -953, "test"), "test")
        self.assertEqual(arrs.get([1, ['g', 5], 13, 3], 1, "test"), ['g', 5])
        self.assertEqual(arrs.get([{'key': 'value'}, 2, 3], 0, "test"), {'key': 'value'})
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], -21), None)
        self.assertEqual(arrs.get([], 13), None)
        self.assertEqual(arrs.get([], 0), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], -4, -1), ['abc', 'мир вашему дому', [1, 7]])
        self.assertEqual(arrs.my_slice([1, 2.541265, 'а', 'б', 'вгдеё', 3], 0), [1, 2.541265, 'а', 'б', 'вгдеё', 3])
        self.assertEqual(arrs.my_slice(['f', 'w', 'b'], -2, 4), ['w', 'b'])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 'fgh', 6, 10.56, 13, 'a'], 0, 5), [1, 2, 'fgh', 6, 10.56])
        self.assertEqual(arrs.my_slice([1, 'мрвыалэ', 'аааа', 4, 'лес', 7], 0, -3), [1, 'мрвыалэ', 'аааа'])
        self.assertEqual(arrs.my_slice([1, 7, (2, 13, 19732.6525654), 3], 2, -1), [(2, 13, 19732.6525654)])
        self.assertEqual(arrs.my_slice(['а', 'б', 'вгдеё'], -2, -1), ['б'])
        self.assertEqual(arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], -2, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 'abc', 'мир вашему дому', [1, 7], 3], 3, 3), [])
        self.assertEqual(arrs.my_slice([], 0, 0), [])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice(['а', 'б', 'вгдеё']), ['а', 'б', 'вгдеё'])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4, 2), [1, 2])
