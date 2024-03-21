class MergeSort:
    def __init__(self, arr):
        self.array = arr

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        halfway_index = len(arr) // 2 #Ensure that the index is an int
        
        arr1 = arr[:halfway_index] # Get all the number up to but excluding the element at the halfway index
        arr2 = arr[halfway_index:] # Get all the number from the halfway index to the end of the array
        
        # Recursively split the arrays
        arr1 = self.mergeSort(arr1)
        arr2 = self.mergeSort(arr2)

        return self.merge(arr1, arr2)

    def merge(self, arr_a, arr_b):
        arr_c = []
        
        i, j = 0, 0
        while len(arr_a) > i and len(arr_b) > j:
            if arr_a[i] > arr_b[j]:
                arr_c.append(arr_b[j])
                j += 1
            else:
                arr_c.append(arr_a[i])
                i += 1   
        
        arr_c.extend(arr_a[i:])
        arr_c.extend(arr_b[j:])
        
        try:
            from playsound import playsound
            playsound("371266__mafon2__water-drop.mp3")
        except ModuleNotFoundError:
            print("Module 'playsound' could not be used. Skip playing sound.")

        print("Merged Array: ", arr_c)

        return arr_c


# MAIN
array = [10, 5, 7, 4, 1, 8, 2, 6, 3, 9] # generate using online random number generator
merge_sort = MergeSort(array)

print("Original Array: ", array)
sorted_arr = merge_sort.mergeSort(array)
print ("Sorted Array: ", sorted_arr)