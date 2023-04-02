
def get_total(dict):
    total_=0
    for k,v in dict.items():
        total_+=v
    return total_




food_bill={
    'chicken':200,
    'drink':40,
    'salad': 30
}


print(get_total(food_bill))

