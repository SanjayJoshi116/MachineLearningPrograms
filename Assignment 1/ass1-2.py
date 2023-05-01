amt = int(input("Enter an Amount:"))
if(amt>20000):
    comm = amt * 0.05
    print("Amount: ",amt)
    print("Commission: ",comm)
else:
    print("No Commission")