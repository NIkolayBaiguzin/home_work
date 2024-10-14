# break оператор останавливаект цикл
# continue

while True:
    num = int(input('please input number: '))
    if num % 2 == 0 :
        print(f'the number {num} is even')
        break # Прекращает цикл
    else:
        print(f'{num} not even')

print('End cycle')
