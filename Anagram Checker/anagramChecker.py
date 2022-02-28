
from collections import Counter

# function to check if two strings are
# anagram or not
def check(string1, string2):

	# implementing counter function
	if(Counter(string1) == Counter(string2)):
		print("Yes")
	else:
		print("No")


# driver code
s1 = "mary"
s2 = "army"
check(s1, s2)
