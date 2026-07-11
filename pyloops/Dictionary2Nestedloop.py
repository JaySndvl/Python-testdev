name = input("Enter file name: ")
handle = open(name)

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

bigcount = None
bigword = None
for word, cnt in count.items():
    if bigcount is None or cnt > bigcount:
        bigword = word
        bigcount = cnt
        
        print(bigword, bigcount)