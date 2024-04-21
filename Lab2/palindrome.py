# варіант 11

import sys

sys.stdout.write("Поліндром — слово, число, набір символів, словосполучення\n"
                 "або віршований рядок, що однаково читається в обох напрямках.\n"
                 "За допомогою цієї програми можна перевірити чи є заданий\n"
                 "рядок поліндромом. Тому введіть рядок для перевірки:\n")

def is_palindrome(n):
    n = n.lower()
    cleaned_str = ""
    for char in n:
        if char.isalpha():
            cleaned_str += char
        if char.isdigit():
            cleaned_str += char
    if cleaned_str == cleaned_str[::-1]:
        return True
    else:
        return False

def main():
    for row in sys.stdin:
        if not row.strip():
            sys.stderr.write("Помилка! Ви нічого не написали. Спробуйте ще раз :) \n")
            sys.exit(1)
        res = is_palindrome(row)
        if res is not None:
            sys.stdout.write(str(res) + "\n")
    sys.exit(0)

if __name__ == "__main__":
    main()
