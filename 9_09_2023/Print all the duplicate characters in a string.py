# Python3 program to count all duplicates
def printDups(Str):

	count = {}
	for i in range(len(Str)):
		if(Str[i] in count):
			count[Str[i]] += 1
		else:
			count[Str[i]] = 0

	for it,it2 in count.items(): 
		if (it2 >= 1): 
			print(str(it) + "with "+str(it2))
	
# Driver code
Str = "test string"
printDups(Str)
