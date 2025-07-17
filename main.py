def times_table():
    print("Enter a number to generate it's multiplication table")
    num = int(input('Enter a number: '))
    for i in range(1, 13):
        product = num * i
        print(f'{num} * {i} = {product}')
        continue
    print(f'There is your multiplication table for {num}')


times_table()

