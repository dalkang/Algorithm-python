T = int(input())
numbers = []

for t in range(T):
    numbers.append(int(input()))

for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

for number in numbers:
    print(number)