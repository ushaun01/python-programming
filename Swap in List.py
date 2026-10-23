#swap first and last number in list

a=[1,23,5,8,9,17]

a[0], a[-1] = a[-1], a[0]
print(a)

a[0], a[-2] = a[-2], a[0]
print(a)