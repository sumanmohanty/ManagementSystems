gangtok_seat=20
g_seat=0
tadong_seat=20
t_seat=0
ch=1
filename1="bus.txt"
while(ch==1):
        print("***SMIT BUS SERVICE***")
        x=int(input("Choose from the following options\n1.Teaching Staff\n2.Non-Teaching Staff\n>>>"))
        if(x==1):
            emp_id=int(input("Enter ID:"))
            filename="database.txt"
            to_store=[]
            with open(filename,'r') as filehandle:
                currentline=1
                for line in filehandle:
                    if currentline==emp_id:
                        to_store.append(line.split('#'))
                        break
                    currentline+=1
            ids=int(to_store[0][0])
            if emp_id==ids:
                y=int(input("Choose your route:\n1.Gangtok\n2.Tadong\n>>>"))
                if(y==1):
                    fare=60
                    if(gangtok_seat>0):
                        gangtok_seat-=1
                        sal=int(to_store[0][4])
                        fare=sal-(fare*30)
                        g_seat+=1
                        print("Salary after deduction:",fare)
                        print("Seats left:",gangtok_seat)
                        to_store[0].pop(5)
                        to_store[0].append(60*30)
                        to_store[0].append(1)
                        to_store[0].append(g_seat)
                        print("Tostore:",to_store)
                        with open(filename1,'a') as filehandle:
                            filehandle.write(str(to_store[0])+'\n')
                            # filehandle.write("\n")
                    else:
                        print("Seats not available,Please try for another route")
                elif(y==2):
                    fare=50
                    if(tadong_seat>0):
                        tadong_seat-=1
                        sal=int(to_store[0][4])
                        fare=sal-(fare*30)
                        t_seat+=1
                        print("Salary after deduction:",fare)
                        print("Seats left:",tadong_seat)
                        to_store[0].pop(5)
                        to_store[0].append(50*30)
                        to_store[0].append(1)
                        to_store[0].append(t_seat)
                        print("Tostore:",to_store)
                        with open(filename1,'a') as filehandle:
                            filehandle.write(str(to_store[0])+'\n')
                            # filehandle.write("\n")
                    else:
                        print("Seats not available,Please try for another route")
                else:
                    print("Incorrect input for route selection!!!\n")
            else:
                print("Incorrect Employee ID")
        elif(x==2):
            emp_id=int(input("Enter ID:"))
            filename="database1.txt"
            to_store=[]
            with open(filename,'r') as filehandle:
                currentline=1
                for line in filehandle:
                    if currentline==emp_id:
                        to_store.append(line.split('#'))
                        break
                    currentline+=1
            ids=int(to_store[0][0])
            if emp_id==ids:
                y=int(input("Choose your route:\n1.Gangtok\n2.Tadong\n>>>"))
                if(y==1):
                    fare=40
                    if(gangtok_seat>0):
                        gangtok_seat-=1
                        sal=int(to_store[0][4])
                        fare=sal-(fare*30)
			g_seat+=1
                        print("Salary after deduction:",fare)
                        print("Seats left:",gangtok_seat)
                        to_store[0].pop(5)
                        to_store[0].append(40*30)
                        to_store[0].append(1)
                        to_store[0].append(g_seat)
                        print("Tostore:",to_store)
                        with open(filename1,'a') as filehandle:
                            filehandle.write(str(to_store[0])+'\n')
                            # filehandle.write("\n")
                    else:
                        print("Seats not available,Please try for another route")
                elif(y==2):
                    fare=30
                    if(tadong_seat>0):
                        tadong_seat-=1
                        sal=int(to_store[0][4])
                        fare=sal-(fare*30)
			t_seat+=1
                        print("Salary after deduction:",fare)
                        print("Seats left:",tadong_seat)
                        to_store[0].pop(5)
                        to_store[0].append(30*30)
                        to_store[0].append(1)
                        to_store[0].append(t  _seat)
                        print("Tostore:",to_store)
                        with open(filename1,'a') as filehandle:
                            filehandle.write(str(to_store[0])+'\n')
                            # filehandle.write("\n")
                    else:
                        print("Seats not available,Please try for another route")
                else:
                    print("Incorrect input for route selection!!!\n")
            else:
                print("Incorrect Employee ID")
        else:
            print("Incorrect input for Employee-type,try again")
        ch=int(input("Another booking(1/0):"))
