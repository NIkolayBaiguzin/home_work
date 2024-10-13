
for num in range(1,21):
    print(num)


numbers = [num for num in range(1,1_000_001)]

for num in numbers[80:500]:
    print(num)

print(min(numbers), max(numbers))

print(sum(numbers))