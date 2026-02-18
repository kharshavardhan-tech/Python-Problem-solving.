# Program to merge characters of 2 strings by taking characters alternatively- Input-"abcdefg", Input 2- "1234567" output- a1b2c3d4e5f6g7

s1 = "abcdefg"
s2 = "1234567"

i,j=0,0
output=" "
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)