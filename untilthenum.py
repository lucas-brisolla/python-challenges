number = int(input("Type a number: "))
sequence = 0

while sequence < number:
    sequence += 1
    print(sequence)
    if sequence == number:
        break
