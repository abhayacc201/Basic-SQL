'''Given a sorted array arr containing n elements with possibly some duplicate, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.'''

'''Sample output:
nput:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. '''

#Solution:
n=int(input("Enter the number of elements in the array:"))   #number of elements in array
print("Enter the array:")
arr=list(map(int,input().split()))                             #inputing the list
x=int(input("Enter the element to be found:"))               #inputing the element to be found
if arr.count(x)!=0:
            a=arr.index(x)                                               #if count of element is zero, [-1,-1] is returned else desired indices are returned to std output
            arr.reverse()
            b=n-1-arr.index(x)
            print(a,b)
else:
    print(-1,-1)
