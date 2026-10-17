numbers =[]
for i in range(5):
    n = int(input("Enter integer: "))
    numbers.append(n)
    if len(numbers) != len(set(numbers)):
        print("DUPLICATES")
    else:
        print("ALL UNIQUE")
