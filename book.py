
for i in range(1,51):
    if i in[11,21,31,41]:
        print()
    print(i,end='\t')
print(lst)
book=int(input("no of seats"))
if (book < 6 and book >0):
    print("checking")
    for i in range(book):
        seatno=int(input("seat no"))
        if (seatno in lst):
            bookno.append(seatno)
                
        else:
            print("other seat")
            continue
    print(bookno)
    for i in bookno:
        lst[i-1]="BK"
    print(lst)
    
else:
    print("between 1-5")
    




