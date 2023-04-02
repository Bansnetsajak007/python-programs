# Starter code
# items = [1,2,3,4,5]

# try:
#     item = items[3]
#     print(item)

# except:
#     print("Index is out of range!")


try:
    with open('sample.txt','rb') as f:
        print(f.read())

except:
    print("something went wrong..")