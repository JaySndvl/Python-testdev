largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        int_num = int(num)
    except ValueError:
        print("Invalid Output")
        continue
    if largest is None:
        largest = int_num
    elif int_num > largest:
        largest = int_num

    if smallest is None:
        smallest = int_num
    elif int_num < smallest:
        smallest = int_num
        

print("Maximum is", largest)
print("Minimum is", smallest)