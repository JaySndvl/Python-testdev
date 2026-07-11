text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
number = float(text[start:])
print(number)