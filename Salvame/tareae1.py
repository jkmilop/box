print ("Ingrese 0 para -p o -q y cualquier otro numero para p o q\nIngrese primero p y luego q\n")


def valorPyQ(p,q):
    p = False
    q = True
    s = []
    if p != 0:
        p = True
    if q == 0:
        q = False
    s.append(p)
    s.append(q)

    return pvq(s)

def pvq(s:list):
    p = s[0]
    q = s[1]

    t1 = ["V","V","F","F"]#p
    t2 = ["V","F","V","F"]#q
    t3 = ["F","F","V","V"]#-p
    t4 = ["F","V","F","V"]#-q

    tmp1 = t1
    tmp2 = t3
    tmp3 = []

    t=[]
    
    #La t es la tabla de verdad

    n = 0

    
    if s[0]==False:
        tmp1 = t3

    if s[1]==True:
        tmp2 = t4

    for i in tmp1:
        if tmp1[i] == V or tmp2[i] == V:
            tmp3.append(V)
        else:
            tmp3.append(F)

    for i in tmp3:
        t.append(tmp1[i])
        t.append(tmp2[i])
        t.append(tmp3[i])

    for i in t:
        print("t[i]\n")


def menu():
    s = valorPyQ(1,1)
    pvq(s)
menu()
            
        
            
            
            
        

        
       
