from itertools import count


def find_duplicate(input_str:str):
    """find duplicate letters"""
    unique_letter_count = []
    for i in range(len(input_str)):
        if input_str.count(input_str[i])>1:
            if unique_letter_count.count(input_str[i]) == 0:
                print("{} letter is {} times in a word".format(input_str[i],input_str.count(input_str[i])))
                unique_letter_count.append(input_str[i])

if __name__ == "__main__":
    find_duplicate("test string")