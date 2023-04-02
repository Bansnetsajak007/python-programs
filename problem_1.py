li=[200,30,1000,900,100]
n=len(li)
li_2=[]
i= 0
greatest= 0
while(i<n):

    if greatest<li[i]:
        greatest=li[i]

    else:
        greatest=greatest

    i+=1
    li.pop(2)

print( li)


