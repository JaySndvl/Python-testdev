fname = input("Enter file:")
fh = open(fname)
counts = {}
with fh:
	for line in fh:
		if not line.startswith("From "):
			continue
		words = line.split()
		email = words[1]
		counts[email] = counts.get(email, 0) + 1

best_email = None
best_count = None
for email, count in counts.items():
	if best_count is None or count > best_count:
		best_email = email
		best_count = count

print(best_email, best_count)