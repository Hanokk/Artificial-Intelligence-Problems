a=raw_input("Enter predicate1: ")
b=raw_input("Enter predicate2: ")
a=a.split(' ')
b=b.split(' ')
if a[0]!=b[0]:
    print "Can't be unified"
else:
    a=a[1:]
    b=b[1:]
    a_num=len(a)
    b_num=len(b)
    print a
    print b
    if a_num==b_num:
        length=a_num
        count=0
        for i in range(length):
            if a==b:
                print "Unified"
                break
            if a[i]!=b[i]:
                p=b[i]
                q=a[i]
                print "Replace ",a[i]," with ",b[i]
                for j in range(length):
                    if a[j]==q:
                        a[j]=p
                    if b[j]==q:
                        b[j]=p
                print a
                print b
    else:
        print "Can't be Unified"


        
