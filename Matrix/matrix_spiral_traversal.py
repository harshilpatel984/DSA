def matrix_spiral_traversal(arr,row,col):

    new_row = 0
    new_col = 0

    while((new_row < row) and (new_col < col)):
        i = new_row
        for j in range(new_col,col):
            print(arr[i][j])

        new_row+=1

        j = col - 1
        for i in range(new_row,row):
            print(arr[i][j])

        col-=1

        if new_row < row:
            i = row - 1
            for j in range(col-1,new_col-1,-1):
                print(arr[i][j])

            row-=1

        if new_col < col:
            j = new_col
            for i in range(row-1,new_row-1,-1):
                print(arr[i][j])
            
            new_col+=1


if __name__ == "__main__":

    matrix_spiral_traversal(
        [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20]],4,5)