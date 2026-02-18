#Program to check whether the given two strings are anagrams or not?

str1=input('string1:')
str2=input('string2:')
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)

if sorted_str1 == sorted_str2:
    print('given string are anagram')
else:
    print('given string are not anagram')
        