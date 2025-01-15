import unittest
from cad_parser import find_insertion_index, insert_label

class TestCADParser(unittest.TestCase):
    def test_find_insertion_index_found(self):
        lines = [
            "#CAD_FILE_HEADER",
            "#INSERT_LABEL_HERE",
            "#END_OF_FILE"
        ]
        index = find_insertion_index(lines, "#INSERT_LABEL_HERE")
        self.assertEqual(index, 2)  # should be right after the matching line

    def test_find_insertion_index_not_found(self):
        lines = [
            "#CAD_FILE_HEADER",
            "#END_OF_FILE"
        ]
        index = find_insertion_index(lines, "#SOME_MISSING_TERM")
        self.assertIsNone(index)

    def test_insert_label(self):
        lines = [
            "#CAD_FILE_HEADER",
            "#INSERT_LABEL_HERE",
            "#END_OF_FILE"
        ]
        updated = insert_label(lines, 2, "#NEW_LABEL: MyCustomLabel")
        self.assertIn("#NEW_LABEL: MyCustomLabel\n", updated)
        self.assertEqual(updated[2], "#NEW_LABEL: MyCustomLabel\n")

if __name__ == "__main__":
    unittest.main()
