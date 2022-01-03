#LOGIKA

print(50*"=")
print("LOGIKA OR")
a = False
b = False
c = (a or b)
print("[>](%s or %s) = %s"%(a,b,c))
a = False
b = True
c = (a or b)
print("[>](%s or %s) = %s"%(a,b,c))
a = True
b = False
c = (a or b)
print("[>](%s or %s) = %s"%(a,b,c))
a = True
b = True
c = (a or b)
print("[>](%s or %s) = %s"%(a,b,c))

print(50*"=")
print("LOGIKA AND")
a = False
b = False
c = (a and b)
print("[>](%s and %s) = %s"%(a,b,c))
a = False
b = True
c = (a and b)
print("[>](%s and %s) = %s"%(a,b,c))
a = True
b = False
c = (a and b)
print("[>](%s and %s) = %s"%(a,b,c))
a = True
b = True
c = (a and b)
print("(%s and %s) = %s"%(a,b,c))

print(50*"=")
print("LOGIKA NOT")
a = False
c = not a
print("[>](not %s) = %s"%(a,c))
a = True
c = not a
print("[>](not %s) = %s"%(a,c))
print(50*"=")