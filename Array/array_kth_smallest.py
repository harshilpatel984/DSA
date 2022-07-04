from cgitb import small


def kth_smallaest(arr,k):
    for n in range(0,k):
        smallest = arr[0]
        for i in range(0,len(arr)):
            if smallest >= arr[i]:
                smallest = arr[i]
        arr.remove(smallest)

    return smallest


if __name__ == "__main__":
    arr = [12,15,10,5,6,3,4,25]
    print(kth_smallaest(arr, 3))