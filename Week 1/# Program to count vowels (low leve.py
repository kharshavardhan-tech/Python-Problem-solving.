# Program to count vowels (low level)

string = input("Enter a string: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for ch in string:
    if ch == 'a' or ch == 'A':
        a = a + 1
    elif ch == 'e' or ch == 'E':
        e = e + 1
    elif ch == 'i' or ch == 'I':
        i = i + 1
    elif ch == 'o' or ch == 'O':
        o = o + 1
    elif ch == 'u' or ch == 'U':
        u = u + 1

print("Number of vowels:")
print("a =", a)
print("e =", e)
print("i =", i)
print("o =", o)
print("u =", u)
