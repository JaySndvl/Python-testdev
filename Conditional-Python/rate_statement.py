hrs = input("Enter Hours:")
rt = input("Enter Rate:")
hours = float(hrs)
rate = float(rt)
if hours > 40 :
    reg_pay = 40 * float(rate)
    otp_pay = (float(hrs) - 40) * (float(rate) * 1.5)
    t_pay = reg_pay + otp_pay
elif hours < 40 :
    t_pay = float(hrs) * float(rate)
print(t_pay)