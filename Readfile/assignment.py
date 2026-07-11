fname = input("Enter file name: ")

try:
    with open(fname) as fh:
        print(fh.read().rstrip().upper())
except OSError:
    print("File cannot be opened:", fname)
    exit()

