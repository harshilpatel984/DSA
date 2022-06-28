def string_reverse(rev_str_input):
    
    rev_str_output = []
    
    for i in range(len(rev_str_input)-1,-1,-1):
        rev_str_output.append(rev_str_input[i])

    return rev_str_output

if __name__ == "__main__":
    print(string_reverse(['h','a','r','s','h','i','l']))