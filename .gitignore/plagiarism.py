# Reads a file's words and inserts them into a dictionary with a
# key: value association of word: number of occurrences. 
def createMap(file1):
	f1 = open(file1, 'r')
	A = []
	for line in f1:
		A += ''.join(i for i in line.lower() if i.isalnum() or i in ' ;:').split()
	f1.close()
	hashMap = {}
	for w in set(A):
		hashMap[w] = A.count(w)
	return hashMap

# This function calculates the jaccard index, used commonly to find similarity.
def jaccard(set1, set2):
	print(len(set1 | set2))
	return 100*len(set1 & set2)/len(set1 | set2)

# Helper function to print the table analysis of words.
def printtable(h1, h2):
	print('Word, Count1, Count2')
	for i in sorted(set(h1) & set(h2)):
		print('{0:11}{1:10d}{2:10d}'.format(i, h1[i], h2[i]))

def main():
	h1 = createMap('1.txt')
	h2 = createMap('2.txt')
	set1 = set(h1)
	set2 = set(h2)



	print('Number of unique words in document 1: {}'.format(len(h1)))
	print('Number of unique words in document 2: {}'.format(len(h2)))
	print('They have {} words in common.\n'.format(len(set1 & set2)))
	printtable(h1,h2)
	print(jaccard(set1, set2))

if __name__ == '__main__':
	main()
