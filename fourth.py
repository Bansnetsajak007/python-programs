from logging import exception


def divide(div_num):
    try:
        return 60/ div_num

    except Exception as E:
        print(E)
        



# print(divide(2))
# print(divide(3))
print(divide(0))
# print(divide(6))

