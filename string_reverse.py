def rev(string):
    c=[]
    a=string
    j=0
    b=len(string)-1
    for i in a:
        c.append(a[b-j])
        j+=1
    return c



name= input("Enter any string: ")

li=rev(name)

result=''.join(li)
print(result)
