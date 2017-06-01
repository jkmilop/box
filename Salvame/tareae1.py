print ("Ingrese 0 para -p o -q y cualquier otro numero para p o q\nIngrese primero p y luego q\n")

t1 = "VVFF" # p
t2 = "VFVF" # q
t3 = "FFVV" #-p
t4 = "FVFV" #-q


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

def negacion(s):

    if s[0]==False:
        print("F   V\n\nV   F\n")
    else:
        print("V   F\n\nF   V\n")

def disyuncion(s):
    
    

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

def conjuncion(s):
    
    

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
        if tmp1[i] == "V" and tmp2[i] == "V":
            tmp3+="V"
        else:
            tmp3+="F"
        i+=1

    j = 0
    
    while j <4:
        t=tmp1[j]+"   "+tmp2[j]+"   "+tmp3[j]

        print("%s\n"%t)
        j+=1

def condicional(s):
    
    

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
        if tmp1[i] == "V" and tmp2[i] == "F":
            tmp3+="F"
        
        else:
            tmp3+="V"
        i+=1

    j = 0
    
    while j <4:
        t=tmp1[j]+"   "+tmp2[j]+"   "+tmp3[j]

        print("%s\n"%t)
        j+=1
def bicondicional(s):
    
    

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
        if tmp1[i] == tmp2[i]:
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
    s = valorPyQ(0,0)

    p = "p"
    q = "q"

    if s[0] == 0:
        p = "-p"
    if s[1] == 0:
        q = "-q"

    
    if p == "p":
        print("p  -p\n")
    
    if p == "-p":
        print("-p  p\n")
    negacion(s)
    print ("a = %s v %s\n%s  %s   a\n"%(p,q,p,q))
    disyuncion(s)
    print ("a = %s y %s\n%s  %s   a\n"%(p,q,p,q))
    conjuncion(s)
    print ("a = %s -> %s\n%s  %s   a\n"%(p,q,p,q))
    condicional(s)
    print ("a = %s <-> %s\n%s  %s   a\n"%(p,q,p,q))
    bicondicional(s)
menu()
          
