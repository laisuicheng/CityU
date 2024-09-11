class MergeSort():
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        # Create temporary arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temporary arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[left + i]

        for j in range(0, n2):
            R[j] = arr[mid + 1 + j]

        # Merge the temporary arrays back into arr[left..right]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2

            # Sort first and second halves
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

# Example usage
if __name__ == "__main__":
    arr = [30, 53, 68, 1, 21, 79]
    print("Given array is:", arr)

    merge_sorter = MergeSort()
    merge_sorter.mergeSort(arr, 0, len(arr) - 1)

    print("Sorted array is:", arr)
