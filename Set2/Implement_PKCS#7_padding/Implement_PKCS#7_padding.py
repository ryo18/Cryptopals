a = "YELLOW SUBMARIE"

t = len(a)
t = 20 - ( t % 20)

b = ("\\x0" + chr(t + 48))*t
a = a+b
print a
