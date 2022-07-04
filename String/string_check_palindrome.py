def check_palindrome(input_str:str):
    input_rev_str = input_str[::-1]
    if input_rev_str == input_str:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(check_palindrome("abba"))