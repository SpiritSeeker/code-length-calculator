import numpy as np

def takeFirst(e):
	return e[0]

def Huffman(p):
	'''
	The Huffman algorithm sorts the array in decresing order of probability and merges two least probabilities in every iteration.
	The code symbols with less probabilities have more number of bits assigned to them. 
	'''
	p = np.flip(np.sort(p), axis = 0)
	p_ = []
	for i in range(0,p.shape[0]):
		p_.append([p[i],[i]])
	lens = np.zeros(p.shape,dtype=np.int32)
	while len(p_) > 1:
		p_.sort(key=takeFirst,reverse=True)
		for num in p_[-2][1]:
			lens[num] += 1
		for num in p_[-1][1]:
			lens[num] += 1	
		p_[-2][0] += p_[-1][0]
		for a in p_[-1][1]:
			p_[-2][1].append(a)
		p_.pop()
	ent = lens * p
	for i in range(np.min(lens),np.max(lens)+1):
		print('Number of ' + str(i) + '-bit codes: ' + str(np.count_nonzero(lens == i)))
	return ent.sum()

# The probability array of code symbols
p = np.array([0.35, 0.25, 0.12, 0.09, 0.08, 0.07, 0.04])

# Entropy is the lower bound of average word length
ent = (-1 * p * np.log(p) / np.log(2)).sum()
print('Entropy = ' + str(ent))
p_prev = np.zeros([1])
p_prev[0] = 1

# Compute the average word lenghts of code symbols using Huffman algorithm using tuple size 1 through 9
for tuple_size in range(1,10):
	print('\nTuple size = ' + str(tuple_size))
	p_new = np.zeros([7**tuple_size])	
	for i in range(0,7**(tuple_size-1)):
		p_new[7*i:7*(i+1)] = p * p_prev[i]
	print('Avg word length = ' + str(Huffman(p_new)/tuple_size))
	p_prev = p_new	