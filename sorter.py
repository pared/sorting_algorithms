
__author__ = 'pawel'
class Sorter:
    def merge_sort(self,array):
        if(len(array)>1):
            half = len(array)/2
            print half
            left = array[:half]
            right = array[half:]

            self.merge_sort(left)
            self.merge_sort(right)
            i=0;
            j=0;
            k=0;
            while i < len(left) and j < len(right):
                if(left[i]<right[j]):
                    array[k]=left[i]
                    i+=1
                else:
                    array[k]=right[j]
                    j+=1

                k+=1
            while i<len(left):
                array[k] = left[i]
                i+=1
                k+=1
            while j<len(right):
                array[k] = right[j]
                j+=1
                k+=1

    def bubble_sort_iteration(self,array):
        length = len(array)
        counter = 1;
        for i in range(length):
            for j in range(length-counter):
                if array[j]>array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
            counter+=1

    def check_sorting(self,array):
        for i in range(len(array)-1):
            if(array[i]>array[i+1]):
                return "incorrect"
        return "correct"

    def insertion_sort(self,array):
        for j in range (1,len(array)):
            key = array[j]
            i=j-1
            while i>=0 and array[i]>key:
                array[i+1]=array[i]
                i-=1
            array[i+1] = key





