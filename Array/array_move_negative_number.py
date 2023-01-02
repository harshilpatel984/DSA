def move_negative_number(arr):
    positive_arr = []
    negative_arr = []
    for i in range(len(arr)):
        if arr[i] <=0:
            negative_arr.append(arr[i])
        else:
            positive_arr.append(arr[i])

    return negative_arr+positive_arr

if __name__ == "__main__":
    print(move_negative_number([1,4,3,-2,5,-6,0]))