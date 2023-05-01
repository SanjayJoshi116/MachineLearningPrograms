nums = []

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fnum = float(num)

    except:
        print("Invalid input")
        continue

    nums.append(fnum)

largest = max(nums)
smallest = min(nums)

print("Maximum is", largest)
print("Minimum is", smallest)