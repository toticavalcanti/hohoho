# -*- coding: utf-8 -*-
"""
@author: toti.cavalcanti
"""
import unittest
from noel import solution

class TestNoel(unittest.TestCase):
    def test_one_Ho(self):
        self.assertEqual(solution(1), "Ho!")

    def test_two_Ho(self):
        self.assertEqual(solution(2), "Ho Ho!")

unittest.main()