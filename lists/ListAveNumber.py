numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value =  float(inp)
    numlist.append(value)
    
averate = sum(numlist) / len(numlist)
print("Average:", averate)
      