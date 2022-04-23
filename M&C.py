def mc():
        m=3
        c=3
        while((m!=0)&(c!=0)):
             if(( m== 3) & (c == 3)):
                c = c - 2
                print(m,c)
             if((m == 3) & ( c == 1)):
                  c = c-1
                  print(m,c)
             if((m == 3) & (c == 0)):
                 c = c+1
                 print(m,c)
             if((m == 3) & (c == 1)):
                 m = m-1
                 c = c+1
                 print(m,c)
             if((m == 2) & (c == 2)):
                  m = m-2
                  c = c+1
                  print(m,c)
             if((m == 0) & (c == 3)):
                  c = c-1
                  print(m,c)
             if((m == 0) & (c == 2)):
                  c = c - 2
                  print(m,c)
mc()