print ("Ingrese 0 para -p o -q y cualquier otro numero para p o q\nIngrese primero p y luego q\n")


def valorPyQ(p,q):
    p1 = False
    q1 = True
    s = []
    if p != 0:
        p1 = True
    if q == 0:
        q1 = False
    s.append(p1)
    s.append(q1)

    return (s)

def pvq(s):
    
    t1 = "VVFF" # p
    t2 = "VFVF" # q
    t3 = "FFVV" #-p
    t4 = "FVFV" #-q

    tmp1 = t1
    tmp2 = t2
    tmp3 = ""

    
    #La t es la tabla de verdad
    
    if s[0]==False:
        tmp1 = t3

    if s[1]==False:
        tmp2 = t4

    i = 0
    while i <4:
        if tmp1[i] == "V" or tmp2[i] == "V":
            tmp3+="V"
        else:
            tmp3+="F"
        i+=1

    j = 0
    
    while j <4:
        t=tmp1[j]+"   "+tmp2[j]+"   "+tmp3[j]

        print("%s\n"%t)
        j+=1


def menu():
    s = valorPyQ(1,1)
    print ("  p v q:\n")
    pvq(s)
menu()
          
