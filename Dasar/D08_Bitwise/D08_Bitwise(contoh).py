#BITWISE

a = 22
b = 26
temp = int()
tempBits = ["00000000","00000000"]

#Desimal to Bitwise
print(50*"=")
print("Desimal to Bitwise")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(a,tempBits[0]))
tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(b,tempBits[0]))

#Bitwise SHIFT LEFT
print(50*"=")
print("SHIFT LEFT << ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
temp = (a<<1); tempBits[1] = bin(temp); tempBits[1] = tempBits[1][2:];
print("[>]{} = {} <SHIFT.LEFT(1)>  {} = {}".format(a,tempBits[0],temp,tempBits[1]))

tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
temp = (b<<2); tempBits[1] = bin(temp); tempBits[1] = tempBits[1][2:];
print("[>]{} = {} <SHIFT.LEFT(2)> {} = {}".format(b,tempBits[0],temp,tempBits[1]))

#Bitwise SHIFT RIGHT
print(50*"=")
print("SHIFT RIGHT >> ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
temp = (a>>1);    tempBits[1] = bin(temp); tempBits[1] = tempBits[1][2:];
print("[>]{} = {} <SHIFT.LEFT(1)> {} = {}".format(a,tempBits[0],temp,tempBits[1]))

tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
temp = (b>>2); tempBits[1] = bin(temp); tempBits[1] = tempBits[1][2:];
print("[>]{} = {} <SHIFT.LEFT(2)>  {} = {}".format(b,tempBits[0],temp,tempBits[1]))

#Bitwise OR
print(50*"=")
print("BITWISE OR | ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(a, tempBits[0]))
tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(b, tempBits[0]))
print((15*"-") + "(|)")
temp = (a|b)
tempBits[0] = bin(temp); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(temp, tempBits[0]))

#Bitwise AND
print(50*"=")
print("BITWISE AND & ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(a, tempBits[0]))
tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(b, tempBits[0]))
print((15*"-") + "(&)")
temp = (a&b)
tempBits[0] = bin(temp); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(temp, tempBits[0]))

#Bitwise XOR
print(50*"=")
print("BITWISE XOR ^ ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(a, tempBits[0]))
tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(b, tempBits[0]))
print((15*"-") + "(^)")
temp = (a^b)
tempBits[0] = bin(temp); tempBits[0] = tempBits[0][2:];
print("[>]{} = {}".format(temp, tempBits[0]))

#Bitwise NOT
print(50*"=")
print("BITWISE NOT ~ ")
tempBits[0] = bin(a); tempBits[0] = tempBits[0][2:];
temp = (~a);    tempBits[1] = bin(temp); tempBits[1] = tempBits[1][3:];
print("[>]{} = {} <NOT> {} = {}".format(a,tempBits[0],temp,tempBits[1]))

tempBits[0] = bin(b); tempBits[0] = tempBits[0][2:];
temp = (~b); tempBits[1] = bin(temp); tempBits[1] = tempBits[1][3:];
print("[>]{} = {} <NOT>  {} = {}".format(b,tempBits[0],temp,tempBits[1]))
