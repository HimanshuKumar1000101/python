def TOH(n , starting, end, between):
    if n==1:
       print ("Move disk 1 from source",starting,"to destination",end)
       return
    TOH(n-1, starting, between, end)
    print ("Move disk",n,"from source",starting,"to destination",end)
    TOH(n-1, between, end, starting)

TOH(4,"01","03","02")