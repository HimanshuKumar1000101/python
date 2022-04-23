def Water_Fill():
    jug = int(input("choose the jug in which the water to be filled first 4L and 3L "))
    jug1=0
    jug2=0

    if(jug==4):
      while(jug1!=2):
        if((jug1==0)&(jug2==0)):
            jug1=jug1+4
            print(jug1,jug2)
        elif((jug1==4)&(jug2==0)):
            jug1=jug1-3
            jug2=jug2+3
            print(jug1,jug2)
        elif((jug1==1)&(jug2==3)):
            jug2=jug2-3
            print(jug1,jug2)
        elif((jug1==1)&(jug2==0)):
            jug1=jug1-1
            jug2=jug2+1
            print(jug1,jug2)
        elif((jug1==0)&(jug2==1)):
            jug1=jug1+4
            print(jug1,jug2)
        elif((jug1==4)&(jug2==1)):
            jug1=jug1-2
            jug2=jug2+2
            print(jug1,jug2)
    else:


            while (jug1 != 2):
                if ((jug1 == 0) & (jug2 == 0)):
                    jug2 = jug2 + 3
                    print(jug1, jug2)
                elif ((jug1 == 0) & (jug2 == 3)):
                    jug2 = jug2 - 3
                    jug1 = jug1 + 3
                    print(jug1, jug2)
                elif ((jug1 == 3) & (jug2 == 0)):
                    jug2 = jug2 + 3
                    print(jug1, jug2)
                elif ((jug1 == 3) & (jug2 == 3)):
                    jug1 = jug1 + 1
                    jug2 = jug2 - 1
                    print(jug1, jug2)
Water_Fill()