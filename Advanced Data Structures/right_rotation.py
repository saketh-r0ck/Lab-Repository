def reversing(arr,start, end):
    n = end - start + 1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def circular_right_rotate(arr,n,s):
   
    reversing(arr,0,n-1)
    reversing(arr,0,s-1)
    reversing(arr,s,n-1)
    print(arr)

def main():
    A = input("Enter array : ").split()
    Array = list(map(int,A))
    n = len(Array)
    s = int(input("Cells to rotate : "))
    circular_right_rotate(Array,n,s)

if __name__ == '__main__':
    main()