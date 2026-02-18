# Write a Program To REVERSE content of the given String by using while loop

a = "Harshavardhan"
output= " "
i=len(a)-1
while i>=0:
    output=output+a[i]
    i=i-1
print(output)