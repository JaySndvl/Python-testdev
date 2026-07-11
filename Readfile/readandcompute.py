from pathlib import Path

fname = input("Enter file name: ")
file_path = Path(__file__).with_name(fname)

fh = open(file_path)
total = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    spam = line.find(":")
    num = float(line[spam + 1:])
    total += num
    count += 1

average = total / count
print("Average spam confidence:", average)
