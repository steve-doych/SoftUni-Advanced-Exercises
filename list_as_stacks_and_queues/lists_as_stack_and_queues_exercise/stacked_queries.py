number = int(input())
stack = []


for current_num in range(number):
    command = input().split(" ")

    if command[0] == "1":
        stack.append(int(command[1]))
    elif stack:
        if command[0] == "2":
            stack.pop()
        elif command[0] == "3":
            print(max(stack))
        elif command[0] == "4":
            print(min(stack))
print(', '.join([str(x) for x in reversed(stack)]))