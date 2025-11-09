import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze(self):
        blueprint = (
            ("void", "void", "void", "void", "void"),
            ("void", "void", "void", "void", "void"),
            ("void", "void", "void", "void", "void"),
            ("void", "void", "void", "void", "void"),
            ("void", "void", "void", "void", "void")
        )
