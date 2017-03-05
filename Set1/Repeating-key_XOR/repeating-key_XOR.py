msg = "Burning 'em, if you ain't quick and nimble"
msg1= "I go crazy when I hear a cymbal"
key = "ICE"
result = ''

def xor_(xs,xy):
	return ''.join((chr(ord(x) ^ ord(y))) for x,y in zip(xs,xy))

for i in range(0,len(msg),3):
	buff = msg[i:i+3]
	result += xor_(buff,key)

#ascii2hex
print ''.join("{:02x}".format(ord(i)) for i in result)



















