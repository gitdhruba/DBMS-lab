import socket		 

def xor(a, b):
	result = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)

def mod2div(dividend, divisor):
	pick = len(divisor)

	tmp = dividend[0 : pick]

	while pick < len(dividend):

		if tmp[0] == '1':
			tmp = xor(divisor, tmp) + dividend[pick]

		else:
			tmp = xor('0'*pick, tmp) + dividend[pick]

		pick += 1

	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword

def encodeData(data, key):

	l_key = len(key)

	# Appends n-1 zeroes at end of data
	appended_data = data + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)

	# Append remainder in the original data
	codeword = data + remainder
	return codeword 
	
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	  

host = socket.gethostname()
port = 5001

s.bind((host,port))
s.listen(5)

csoc,caddr = s.accept()

# receive data from the sender
data = csoc.recv(1024).decode()
key  = '1001'
print("Received feedback from sender :",data)

rem = mod2div(data,key)
print("Calculated Remainder: ",rem)

if rem != '0'*len(rem):
	print("Error!!")
else:
	print("Correct Data Received!!")
	
# close the connection
csoc.close()
s.close()