from collections import deque


numbers = deque(input().split(" "))
# reverse_num = reversed(numbers)
# print(*reverse_num)
while numbers:
    print(numbers.pop(), end=" ")