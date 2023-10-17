print("Hello\nWelcome to the tip calculator.")

try:
    total_bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    number_split = float(input("How many people to split the bill? "))
    
    if tip == 10:
        print("Each person should pay: $", "{:.2f}" .format(float(total_bill) / float(number_split) * 1.10))
    elif tip == 12:
        print("Each person should pay: $", "%.2f" % (float(total_bill) / float (number_split) * 1.12))
    elif tip == 15:
        print("Each person should pay: $", "%.2f" % (float(total_bill) / float (number_split) * 1.15))
    else:
        print("you did not enter a correct percentage")
except: 
    print("you did not enter a valid character")