def computepay(h, r):
    if h > 40:
        reg = r * h
        otp = (h - 40) * (r * 0.5)
        pay = reg + otp
    else:
        pay = r * h
    return pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs), float(rate))
print("Pay", p)