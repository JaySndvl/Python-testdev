fname = input("Enter file name: ")
fh = open(fname)

counts = {}
with fh:
	for line in fh:
		if not line.startswith("From "):
			continue
		words = line.split()
		time = words[5]
		hour = time.split(":")[0]
		counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
	print(hour, counts[hour])