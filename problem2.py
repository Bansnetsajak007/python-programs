import random
with open('petsname.txt','r') as f:
    content=f.read()
    print(content)
    content=content.split("\n")
    print(type(content))

    rand_name=random.choice(content)
    print(rand_name)

    