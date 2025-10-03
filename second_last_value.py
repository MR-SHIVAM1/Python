# uaing sort()
a=[12,34,54,54,43,23,99]

b=list(set(a))

b.sort()

print(b[-2])



# using loop 

a=[12,32,12,3,43,67,89]

first=second=-9999

for num in a:
    if num>first:
        second=first
        first=num
    elif first>num>second:
        second=num
print(second)
 


