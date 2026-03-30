unit = int(input("enter the unit:"))

if unit<=50:
    bill = unit * 0.50
elif unit<=150:
    bill = (50*0.50) + ((unit - 50)*0.75)
elif unit<=250:
    bill = (50*0.50) + (100*0.75) + ((unit - 150)*1.20)
else:
    bill = (50*0.50) + (100*0.75) + (100 * 1.20) + ((unit-250)*1.50)

extra_charge = bill*0.20
total_bill = bill + extra_charge

print(total_bill)