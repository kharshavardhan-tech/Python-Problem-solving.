#remove duplicate characters from the given input String


s="a,d,c,c,b,b"
output=""
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

