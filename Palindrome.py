#palindrome string
s="aabaa"
rev=""
for i in s:
    rev=i+rev
print(rev)
if s==rev:
    print("Its palindrome")
else:
    print("Not Palindrome")

#palindrome using def
def palindrome(a):
    r=""
    for i in a:
        r=i+r
    if a==r:
        print("YES")
    else:
        print("NO")
palindrome("rushi")