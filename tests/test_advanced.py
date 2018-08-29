# -*- coding: utf-8 -*-

import esperanto_analyzer

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_import(self):
        self.assertIsNotNone(esperanto_analyzer)


if __name__ == '__main__':
    unittest.main()
