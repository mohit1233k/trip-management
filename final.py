import sys
def finalmain():
    print("*"*20,"WELCOME TO TRAVEL PERK MAINTAINED BY ADVENTURE NATON","*"*20)
    print("\t\t\tHIGHEST RATED TRIP HOTEL,FLIGHT AND TREKKING BOOKING PLATFORM IN INDIA")
    print("\t\tWHAT WOULD YOU LIKE TO BOOK:\n")
    print("\t\t1) HOTELS\n\t\t2) FLIGHTS\n\t\t3) TREKKING ACTIVITIES\n\t\t4) EXIT")
    c=int(input("ENTER YOUR CHOICE:\n"))
    if c==1:
        hotelmain()
    elif c==2:
        flightmain()
    elif c==3:
        trekkingmain()
    elif c==4:
        print("THANKYOU FOR VISITING US.......\nWE WILL SEE YOU SOON.......")
        sys.exit()
    else:
        print("INVALID ENTERY")
        finalmain()
        
def hotelmain():
    import random
    import csv
    import datetime
    print("\t\t\t\tWELCOME TO HOTEL BOOKING SYSTEM MAINTAINED BY ADVENTURE NATION........\n")
    name=input("ENTER YOUR NAME:\n")
    phoneno=int(input("ENTER YOUR PHONE NUMBER\n "))
    orderid=random.randint(11,999999999)
    print("here is your order id",orderid)
    list1=[]
    
    def hoteljk():
        print("\t1. Hari Market")
        print("\t2. Pahalgam")
        print("\t3. Sofiyan")
        c=int(input("Enter Your Choice: : "))
        if c==1:
            print("Hari Market")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Pahalgam")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("Sofiyan")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")

    
    def hotelgoa():
        print("\t1. Panaji")
        print("\t2. Calingute")
        print("\t3. South Goa")
        c=int(input("Enter Your Choice: : "))
        if c==1:
            print("Panaji")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Calingute")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("South Goa")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")

    
    def hoteldelhi():
        print("\t1. Central Delhi")
        print("\t2. Gurugram")
        print("\t3. Noida")
        c=int(input("ENTER YOUR CHOICE: : "))
        if c==1:
            print("Central Delhi")
            with open('Hotel1.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Gurugram")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                            
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("Noida")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
    
    
    def hotelmumbai():
        print("\t1. Bandra")
        print("\t2. Navi-Mumbai")
        print("\t3. Nashik")
        c=int(input("ENTER YOUR CHOICE: : "))
        if c==1:
            print("Bandra")
            with open('Hotel1.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Navi Mumbai")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("Nashik")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
    
    def hotelhydrabad():
        print("\t1. Charminar")
        print("\t2. Hitech city")
        print("\t3. GachiBowli")
        c=int(input("Enter Your Choice: : "))
        if c==1:
            print("Charminar")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Hitech city")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("Gachibowli")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Types Of Rooms Do You Want:"))
                for i in range(n):
                    nn = int(input("Enter Your Choice:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("No of Days: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")

    
    
    
    def hotelbangalore():
        print("\t1. Banglore Palace")
        print("\t2. Commercial Street")
        print("\t3. Electronic city")
        c=int(input("ENTER YOUR CHOICE: : "))
        if c==1:
            print("Banglore palace")
            with open('Hotel1.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 3000
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==2:
            print("Commercial Street")
            with open('Hotel2.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2400
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2900
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
        elif c==3:
            print("Electronic City")
            with open('Hotel3.csv', 'r') as csv_file:
                read = csv.reader(csv_file)
                print('S.no\tName \t\t\t\tPrice')
                for i in read:
                    print(i[1] + '\t\t' + i[0], i[2])
                n = int(input("How Many Rooms  Do You Want:"))
                for i in range(n):
                    nn = int(input("ENTER YOUR CHOICE:"))
                    if nn == 1:
                        price = 1300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 2:
                        price = 1700
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 3:
                        price = 2300
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    elif nn == 4:
                        price = 2800
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
                        
                    elif nn == 5:
                        price = 3500
                        q = int(input("NO OF DAYS: "))
                        t = price * q
                        list1.append(t)
    
                    else:
                        print("INVALID ENTRY")
    
    
    def bill(name,phoneno):
        print("\t" * 10 + "Total Bill\n")
        print("*" * 80)
        print()
        e = datetime.datetime.now()
        print("Date :                       ",e.strftime("%Y-%m-%d %H:%M:%S"))
        print()
        print("Customer Name :              ", name)
        print("OrderId :                    ", orderid)
        print("PhoneNo :                    ", phoneno)
        print("*" * 80)
        s = sum(list1)
        print("Total Billing Amount :                  ", s.__round__())
        print("*" * 80)
        print("Thankyou , Come Visit Again......")
        print()
        print("You will receive and sms for your valuable Feedback. You can Give reviews on our website too...")
        print()
        print("PRESS ENTER TO CONTINUE ON MAIN MENU")
        u=input()
        finalmain()
    
    def mainmenu():
        print("\t\t\tYou Can Choose City from the Below Options for Hotel Booking")
        print()
        print("\t\t1. Delhi ")
        print()
        print("\t\t2. Mumbai ")
        print()
        print("\t\t3. Bangalore ")
        print()
        print("\t\t4.Goa ")
        print()
        print("\t\t5.Hydrabad")
        print()
        print("\t\t6.Jammu and Kashmir ")
        print()
        print("\t\t7. Bill")
        print()
        ch=int(input("ENTER YOUR CHOICE: "))
        if ch==1:
            hoteldelhi()
        elif ch==2:
            hotelmumbai()
        elif ch==3:
            hotelbangalore()
        elif ch==4:
            hotelgoa()
        elif ch==5:
            hotelhydrabad()
        elif ch==6:
            hoteljk()
        elif ch==7:
            bill(name, phoneno)
        else:
            print("INVALID ")
            
        inp=input("Do you want to Continue : (Y/N):\n")
        if inp=='Y' or inp=='y':
            mainmenu()
        else:
            bill(name,phoneno)
        
    
    
    mainmenu()

def flightmain():
    import random
    import datetime
    import csv
    
    def flight():  
        print("\t\t\tWELCOME TO FLIGHT BOOKING SYSTEM MAINTAINED BY ADVENTURE NATION")    
        E=input("ENTER YOUR EMAILID:")
        p=int(input("ENTER YOUR MOBILE NUMBER:"))
        print()
        print("note:ONCE YOU FLIGHT IS BOOKED  , YOU CANNOT CANCEL THE FLIGHT")
        print("DO YOU WANT TO CONTINUE?")
        print()
        print("PRESS ENTER TO CONTINUE:")
        s=input()
        if s==" " or "":
            main()
            
        else:
            print("try again")
            flight()
    
     
    def main():
        with open('Flight prices.csv','r') as csvfile:
            data=csv.reader(csvfile)
            print(".......ENTER THE ASKED DETAILS.......")
            city1=input("FROM :")
            city2=input("TO : ")
            date = int(input('Enter a date:'))
            month = int(input('Enter a month:'))
            year = int(input('Enter a year:'))
            hour=random.randint(1,23)
            minute=random.randint(1,60)
            date1=datetime.datetime(year, month, date, hour, minute)
            charge=0
            fare=1
            if hour>12:
                charge=845
    
            for i in data:
                if city1==i[0] and city2==i[1]:
                    fare=int(i[2])*0.018+int(i[2])+charge
                
            print("YOUR FLIGHT FROM",city1,"TO",city2,"IS BOOKED.""\nTotal price is : ₹",fare,"(including 18% GST.)\n  ON",date1)
            print("*******FOLOWING INFORMATION ABOUT YOUR FLIGHT WILL BE DELIVERED TO YOUR EMAIL ACCOUNT*******\nFOR FURTHER INFORMATION OR QUERY YOU CAN ALSO VISIT OUR WEBSITE www.adventurenation.co.in\n ")            
            print()
            print("PRESS ENTER TO CONTINUE ON MAIN MENU")
            t=input()
            finalmain()
    flight()



def trekkingmain():
    import csv
    import datetime
    def trekking():
        print("......HERE ARE SOME OF THE FAMOUS TREKS IN INDIA......")
        print("\t\t1)kasol to kheerganga\n\t\t2)triund trek in himachal pradesh\n\t\t3)everest basr camp trek\n\t\t4)anaapurna base camp trek\n\t\t5)hampta pass with spiti valley trek")
        d=int(input("ENTER YOUR CHOICE:"))
        if d==1:
            kasol()
        elif d==2:
            triund()
        elif d==3:
            everest()
        elif d==4:
            annapurna()
        elif d==5:
            hampta()
        else:
            print("INVALID INPUT")   
            trekking()
    
    def info():
        print("*****ENTER YOUR PERSONAL DETAILS HERE FOR CONVENNIENCE*****")
        name=input("ENTER YOUR NAME:\n")
        print()
        phno=int(input("ENTER YOUR PHONE NO:\n"))
        print()
        altno=int(input("ENTER ALTERNATIVE PHONE NUMBER(REQUIRED):\n"))
        print()
        emilid=input("ENTER EMAIL ID:\n")
        print()
        day = int(input('ENTER DATE:\n'))
        print()
        month = int(input("ENTER MONTH:\n"))
        print()
        year = int(input("ENTER YEAR:\n"))
        print()
        date1=datetime.datetime(year, month,day)
        age=int(input("ENTER YOUR AGE:\n"))
        print()
        wght=float(input("ENTER YOUR WEIGHT IN KGs:\n"))
        print()
        hgt=float(input("ENTER YOUR HEIGHT IN MTRs:\n"))
        print()
        bmi=wght/(hgt**2)
        print("YOUR BODY MASS INDEX(BMI) IS",int(bmi))
        print()
        if bmi>=14 and bmi<=30:
            print("CONGRATS",name,"YOU ARE ELIGIBLE FOR THE TREK")
        else:
            print(name,"SORRY!!!YOU ARE NOT ELIGIBLE FOR THE TREK")
        print()
        print("YOUR BOOKING IS DONE FOR",date1,"\nFURTHER DETAILS WILL BE FORWARDED TO YOUR EMAIL ID AT",emilid,)
        print()
        print("FOR MORE DETAILS OR QUERIES YOU CAN MAIL US AT adventernation@org.in\n\nOR YOU CAN VISIT OUR WEBSITE www.AdventureNation.co.in ")
        print()
        print("THANKYOU FOR YOUR PRECIOUS TIME")
        print()
        print("PRESS ENTER TO CONTINUE ON MAIN MENU")
        t=input()
        finalmain()
    def kasol():
        c=open("kasol.txt","r")
        read=c.readlines()
        for i in read:
            print()
            print(i)
            print()
        print("HERE ARE THE DETAILS OF THE TREK MENTIONED ABOVE")
        print("IF YOU LIKE TO BOOK THE TREK PRESS A \nIF YOU WANT TO EXPLORE SOME OTHER TREK PRESS B")
        m=input()
        if m=="A" or m=="a":
            print("FOR BOOKING,KINDLY ENTER YOUR DETAILS:")
            info()
        else:
            trekking()
    def triund():
        c=open("triund.txt","r")
        read=c.readlines()
        for i in read:
            print()
            print(i)
            print()
        print("HERE ARE THE DETAILS OF THE TREK MENTIONED ABOVE")
        print("IF YOU LIKE TO BOOK THE TREK PRESS A\nIF YOU WANT TO EXPLORE SOME OTHER TREK PRESS B")
        m=input()
        if m=="A" or m=="a":
            print("FOR BOOKING,KINDLY ENTER YOUR DETAILS:")
            info()
        else:
            trekking()
            
    def everest():
        c=open("everest.txt","r")
        read=c.readlines()
        for i in read:
            print()
            print(i)
            print()
        print("HERE ARE THE DETAILS OF THE TREK MENTIONED ABOVE")
        print("IF YOU LIKE TO BOOK THE TREK PRESS A\nIF YOU WANT TO EXPLORE SOME OTHER TREK PRESS B")
        m=input()
        if m=="A" or m=="a":
            print("FOR BOOKING,KINDLY ENTER YOUR DETAILS:")
            info()
        else:
            trekking()
    
    def annapurna():
        c=open("annapurna.txt","r")
        read=c.readlines()
        for i in read:
            print()
            print(i)
            print()
        print("HERE ARE THE DETAILS OF THE TREK MENTIONED ABOVE")
        print("IF YOU LIKE TO BOOK THE TREK PRESS A\nIF YOU WANT TO EXPLORE SOME OTHER TREK PRESS B")
        m=input()
        if m=="A" or m=="a":
            print("FOR BOOKING,KINDLY ENTER YOUR DETAILS:")
            info()
        else:
           trekking()
           
    def hampta():
        c=open("hampta.txt","r")
        read=c.readlines()
        for i in read:
            print()
            print(i)
            print()
        print("HERE ARE THE DETAILS OF THE TREK MENTIONED ABOVE")
        print("IF YOU LIKE TO BOOK THE TREK PRESS A\nIF YOU WANT TO EXPLORE SOME OTHER TREK PRESS B")
        m=input()
        if m=="A" or m=="a":
            print("FOR BOOKING,KINDLY ENTER YOUR DETAILS:")
            info()
        else:
            trekking() 
    
    trekking()

finalmain()
