# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if(len(arr)>1):
    mid = int(len(arr)/2)

    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)

    i=j=k=0
    while(i<len(L) and j<len(R)):
      if(L[i]<R[j]):
        arr[k] = L[i]
        k+=1
        i+=1
      else:
        arr[k] = R[j]
        k+=1
        j+=1
      
    while i<len(L):
      arr[k] = L[i]
      k+=1
      i+=1
    
    while(j<len(R)):
       arr[k]=R[j]
       k+=1
       j+=1



# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
       
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
