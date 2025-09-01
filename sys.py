import sys
tot=0
k=len(sys.argv)
print(k)
print(sys.argv[0])
for i in range(1,k):
    tot=tot+int(sys.argv[i])
print(tot)