def array_min_max(arr):
    
    min = arr[0]
    max = arr[0]

    for i in range(1,len(arr)):
        if min >= arr[i]:
            min = arr[i]
        if max <= arr[i]:
            max = arr[i]

    return min,max


if __name__ == "__main__":
    print(array_min_max([1]))