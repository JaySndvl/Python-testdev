fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    line_words = line.split()
    for word in line_words:
        if word not in words:
            words.append(word)

words.sort()
print(words)