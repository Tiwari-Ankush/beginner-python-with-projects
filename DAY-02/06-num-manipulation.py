# we can round off the upto that, we want by round function 
# ie. significant figure

a=223
b=9
print(a/b)
print(type(a/b))

print(round(a/b))
print(type(round(a/b)))

# num manipulation >>
a-=b
b+=2
b*=a
a+=b
a/=b
print(a,b)