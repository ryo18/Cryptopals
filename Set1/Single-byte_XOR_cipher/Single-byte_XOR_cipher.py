a = 'ETAOINSHRDLU'
b = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

c = ''.join(chr(int(b[i:i+2],16)) for i in range(0,len(b),2))

for i in range(0,255):
	d = ''
	for j in range(len(c)):
		d += chr(ord(c[j])^i)
	print d, chr(i)

