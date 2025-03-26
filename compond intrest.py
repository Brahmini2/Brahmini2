def calculate_compond_intrest(principal,rate,time):
""
    calculate the compund intrest.
    :param principal:the inital amount of money(float or int).
    :param rate:the annual intrest rate(float or int).
    :param time:the no of periods of the money is invested for (float or int).
    :return:the compound intrest(float).
    """
#convert rate from the percentage to decimal
rate_decimal=rate/100

# caculate the compound intrest amount=principal*(1+rate_decimal)**time
compound_intrest=amount-principal
return compound_intrest

#input values
principal=foat(input("enter the principal amount:"))
rate=float(input("enter the annual intrest rate(in percentage):"))
trime=float(input("enter the number of periods:"))

#calculate compound intrest
intrest=calculate_compound_intrest(principal,rate,time)

#output the result
print(f"the compound imtrest is:
{intrest:.2f}")
