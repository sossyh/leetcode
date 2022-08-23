class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest=i
        right=2*i+2
        left=2*i+1
        
        if(left<n and arr[left]>arr[largest]):
            largest=left
        if(right<n and arr[right]>arr[largest]):
            largest=right
        if(largest!=i):
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        
        for i in range(n-2,-1,-1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        # for i in range(((n/2)-1),-1,-1):
            # self.heapify(arr,n,i)
        self.buildHeap(arr,n)
        for i in range(n-1,-1,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
