
def calculatePie(n):
    pie =0
    i =1
    for i in range(n):
        x =4*i*i
        y= 4*i*i -1
        z=float(x)/float(y)
        if(i==1):
                pie =1
                pie =pie*z
        else:
                pie =pie*z        
    newpie=2*pie
    print newpie    
    
calculatePie(5)    