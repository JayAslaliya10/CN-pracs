def calcRedundantBits(m):
	for i in range(m):
		if(2**i >= m + i + 1):
			return i

def posRedundantBits(data, r):
	j = 0
	k = 1
	m = len(data)
	res = ''
	for i in range(1, m+r+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1
	return res[::-1]


def calcParityBits(arr, r):
	n = len(arr)
	for i in range(r):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr
# 1011
# 1010101  r=3
# 1  0  1  0  1  0  0

def detectError(arr, nr):
	n = len(arr)
	res = 0
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
		res = res + val*(10**i)
	return int(str(res), 2)

data = input("Enter the data bits : ")
m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)

arr = calcParityBits(arr, r)

print("Data transferred is : " + arr)

recieved = input("Enter the recieved data : ")
print("Recieved Data is : " + recieved)
correction = detectError(recieved, r)

if(correction!=0):
    print("The position of error is ",len(recieved)-correction+1," from the left")
else:
    print("There is no error in recieved message")