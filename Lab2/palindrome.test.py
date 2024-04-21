import unittest
import palindrome
import sys
import io

class Testing(unittest.TestCase):

    def palindrome_test(self):
        res = palindrome.is_palindrome("шалаш")
        self.assertEqual(res, "True")

        res = palindrome.is_palindrome("1234321")
        self.assertEqual(res, "True")

        res = palindrome.is_palindrome("полуниця")
        self.assertEqual(res, "False")

        res = palindrome.is_palindrome("12345678")
        self.assertEqual(res, "False")

        res = palindrome.is_palindrome("1сс5сс1")
        self.assertEqual(res, "True")

        res = palindrome.is_palindrome("Кит нА моРі роМантик")
        self.assertEqual(res, "True")

        res = palindrome.is_palindrome("мама")
        self.assertNotEqual(res, "True")

        self.assertFalse(palindrome.is_palindrome(' '))
        self.assertFalse(palindrome.is_palindrome(1001))

    def setUp(self):
        self.stdin_backup = sys.stdin
        self.stdout_backup = sys.stdout
        self.stderr_backup = sys.stderr

    def tearDown(self):
        sys.stdin = self.stdin_backup
        sys.stdout = self.stdout_backup
        sys.stderr = self.stderr_backup

    def testing_correct(self):
        input = "radar\n"
        output = "True\n"

        sys.stdin = io.StringIO(input)
        sys.stdout = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            palindrome.main()

        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(sys.stdout.getvalue(), output)

    def testing_incorrect(self):
        errors = [(" ", "Помилка! Ви нічого не написали. Спробуйте ще раз :) \n")]

        for data, error in errors:
            sys.stdin = io.StringIO(data)
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()

            with self.assertRaises(SystemExit) as cm:
                palindrome.main()

            self.assertEqual(cm.exception.code, 1)
            self.assertEqual(sys.stderr.getvalue(), error)


if __name__ == '__main__':
    unittest.main()