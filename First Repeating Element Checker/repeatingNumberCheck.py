# This function prints the
# first repeating element in arr[]
def printFirstRepeating(arr, n):
	for i in range(len(arr)):
		if arr.count(arr[i]) > 1:
			return arr[i]
	return "there is no repetition number"


# Driver code
arrToCheck = [16, 2, 5, 6, 2, 5, 6]
n = len(arrToCheck)
print(printFirstRepeating(arrToCheck, n))

# This code is contributed by karthikeyakumarnallam
