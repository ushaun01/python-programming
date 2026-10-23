import string
a="Hello,Usha! How are you doing?"
b=""
for i in a:
    if i not in string.punctuation:
        b=b+i
print(b)



import string

print(string.punctuation)
