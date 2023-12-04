num=int(input("Enter the number of rows"))
for i in range(1,num+1):
 for j in range(1,i+1):
    print("*",end=" ")
 print("")


rows=int(input("Enter the number of rows:"))
for i in range(1,rows+1):
     for j in range(1,i+1):
        print(j,end=" ")
     print("")
       
num=int(input("Enter the number of rows:"))
for i in range(1,num+1):
    for j in range(1,num+3):
        if j<=i:
          print("*",end=' ')
        else:
            print("*",end=' ')
    print("")    