def array_reverse(arr):
    reversed_arr = []

    for i in range(len(arr)-1,-1,-1):
        reversed_arr.append(arr[i])

    return reversed_arr


if __name__ == "__main__":

    print(array_reverse([1,2,3,4,5])) 