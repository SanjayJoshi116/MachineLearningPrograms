ecode = input("Enter an ECode:")
ename = input("Enter the Name:")
basic = int(input("Enter the Basic Salary:"))
ecode1 = ecode[0:1]
ecode2 = int(ecode[1:4])
ecode3 = ecode[4:7]

if(ecode1 == 'A' or ecode1 == 'B' or ecode1 == 'C'):
    if(ecode2>000 and ecode2<=999):
        if(ecode3 == 'PRD' or ecode3 == 'SLS' or ecode3 == 'ACC'):
            if(ecode3 == 'PRD'):
                comm = basic * 0.13
            elif(ecode3 == 'SLS'):
                comm = basic * 0.08
            else:
                comm = basic * 0.05
            if(ecode1 == 'A'):
                comm = comm + 300
            elif(ecode1 == 'B'):
                comm = comm + 200
            else:
                comm = comm + 100
            print("ECode: ",ecode)
            print("EName: ",ename)
            print("Grade: ",ecode1)
            print("EmpNo: ",ecode2)
            print("Department: ",ecode3)
            print("Commission: ",comm)
        else:
            print("Invalid Department")
    else:
        print("Invalid EmpNo")
else:
    print("Invalid Grade")
