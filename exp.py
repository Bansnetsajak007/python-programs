try:
    with open('reading.txt','r') as file:
       content= file.read(10)
       print(content)

except FileExistsError as e:
    print(e)