def mc():
    ml=3
    cl=3
    mr=0
    cr=0
    while(mr!=0 and cr!=0):
        if ((ml == 3) & (cl == 3)):
            cl=cl-2
            cr=cr+2
            print(ml,cl)
            print(mr,cr)
        elif((ml == 3) & (cl == 1)):
            cl = cl - 2
            cr = cr + 2
            print(ml, cl)
            print(mr, cr)
mc()