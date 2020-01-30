# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ): #insertion sort algorithm 
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    x = len(arr)
    for i in range(x):
        for y in range(0, x-i-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]
    
    return arr

arr = [75, 43, 12, 84, 5, 18]

bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i]),


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr