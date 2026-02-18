#  Write a Program To REVERSE order of words present in the given string

s= " python is a easy to leran"
l=s.split( )
l1=l[ :: -1]
l2=" ".join(l1)
print(l2)