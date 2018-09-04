n = int(input("Enter the length of the sequence: "))

a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
for i in range(n-3):
    d = a+b+c
    print(d)
    a = b
    b = c
    c = d