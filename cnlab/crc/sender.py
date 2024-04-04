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

	# Append CRC in the original data
	codeword = data + remainder
	return codeword 
	
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 

host = socket.gethostname()
port = 5001		

s.connect((host, port))

input_string = input("Enter data you want to send->")
data =(''.join(format(ord(x), 'b') for x in input_string))
print("Data in binary format :",data)
key = "1001"

encodedData = encodeData(data,key)
print("Encoded data to be sent to server in binary format :",encodedData)
s.sendall(encodedData.encode())

# close the connection
s.close()
