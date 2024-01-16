import os
import shutil
import tempfile
import unittest

from grepy.grep import grep, grep_count, grep_recursive

class TestGrepFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.test_dir)

    def test_grep_single_file(self):
        # Create a test file
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as test_file:
            test_file.write("apple\nbanana\norange\n")

        # Test grep function on a single file
        result = grep('apple', test_file_path)
        self.assertEqual(result, {test_file_path: [(1, 'apple')]})

    def test_grep_ignore_case(self):
        # Create a test file
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as test_file:
            test_file.write("apple\nBanana\norange\n")

        # Test grep function with case-insensitive option
        result = grep('banana', test_file_path, options=['i'])
        self.assertEqual(result, {test_file_path: [(2, 'Banana')]})

    def test_grep_recursive(self):
        # Create nested test directories and files
        subdir_path = os.path.join(self.test_dir, 'subdir')
        os.makedirs(subdir_path, exist_ok=True)
        file1_path = os.path.join(self.test_dir, 'test_file1.txt')
        file2_path = os.path.join(subdir_path, 'test_file2.txt')
        with open(file1_path, 'w') as file1, open(file2_path, 'w') as file2:
            file1.write("apple\nbanana\norange\n")
            file2.write("apple\nkiwi\nbanana\n")

        # Test grep_recursive function
        result = grep_recursive('kiwi', self.test_dir)
        expected_result = {file1_path: [], file2_path: [(2, 'kiwi')]}
        self.assertEqual(result, expected_result)

    def test_grep_count(self):
        # Create test files
        test_file1_path = os.path.join(self.test_dir, 'test_file1.txt')
        test_file2_path = os.path.join(self.test_dir, 'test_file2.txt')
        with open(test_file1_path, 'w') as file1, open(test_file2_path, 'w') as file2:
            file1.write("apple\nbanana\norange\n")
            file2.write("apple\nkiwi\nbanana\n")

        # Test grep_count function
        result = grep_recursive('apple', self.test_dir)
        count = grep_count(result)
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()
