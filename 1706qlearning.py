import numpy as np 
from numpy import random


def factorial (x,n):  #para saber cuantas permutacion
    if (n>0):
            x=factorial(x,n-1)
            x=x*n   
    else:
        x=1
    return x

def permute(l):
    n = len(l)
    tot= factorial(1,n)-1
    #print("Numero factorial",tot)
    result = []
    mio=[]
    cont=0
    c = n * [0]
    
    result.append(l)

    i = 0;
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                tmp = l[0]
                l[0] = l[i]
                l[i] = tmp
                #print ("holi")
            else:

                tmp = l[c[i]]
                l[c[i]] = l[i]
                l[i] = tmp
            
            #print ("wow",result) #imprime cada uno muchas vecss
            
            result.append(l)
           #print(result)
            #print ("Primer num de result", result[1])
            #mio.append(result[1], axis=0)
            mio=np.concatenate((mio,result[1]),axis=0)
            cont=cont+1
            #print ("mio",mio)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    #print ("mio",mio)
    #print(len(mio))
    if (n>1):
        lista=mio.reshape((tot,n))
    else:
        lista=1  ############problema si hay 0 personas la lista tambien es 1
    print("lista final",lista)
    return lista,tot

def permtotal(permactual,people):
    ini=people+1 #people+1 
    camino=permactual  ###permutacionactual
    larg=len(camino)+2
    caaaminotot=np.zeros(larg)

    for i in range (larg):
        if (i==0):
            caaaminotot[i]=ini
            print("if 1",i)
        if ((i>=1) and (i<larg-1)):
            caaaminotot[i]=camino[i-1]
            print("if 2",i)
        if (i==larg-1):
            caaaminotot[i]=ini
            print("if 3",i)

    print("Camino con vector inicio y fin",caaaminotot)
    return caaaminotot

def originalmatrix(peoplepos, people, obs_list, obs):
    if people>=len(obs_list):
        maxim=people
    if len(obs_list)>people:
        maxim=len(obs_list)
    for i in range (maxim):
        print("I", i, "people", people, "")
        print("peoplepos", peoplepos, "obslist",obs_list)
        print("matrix so far",matrix)
        if ((i+1) <= people):
            print("entró en if 1 con i", i)
            print("peoplepos 0", peoplepos[i][0], "peoplepos 1",peoplepos[i][1])
            matrix[int(peoplepos[i][0])][int(peoplepos[i][1])]=1
        if (i<=len(obs_list)) : #la persona goal no se ubica para que en la de adyacencia no la vea como ubn obstaculo
            print("entró en if 2 con i", i)
            matrix[int(obs_list[i][0])][int(obs_list[i][1])]=-1
    print ("matrix", matrix)
    return matrix

def matrixindex(matrix):
    cont=0
    matindex = np.zeros((matrix.shape[0],matrix.shape[1]))
    for i in range (matrix.shape[0]):
        for y in range(matrix.shape[1]):
            matindex[i][y]=cont
            cont=cont+1
    return matindex 

def rewmatrix(adymatrix,estadofinal):
    rewmatrix = np.zeros((adymatrix.shape[0],adymatrix.shape[1]))
    for i in range (adymatrix.shape[0]):
        for y in range(adymatrix.shape[1]):
            if (adymatrix[i][y]==1 and estadofinal!=y):
                rewmatrix[i][y]=0.1
            if (estadofinal==y):
                rewmatrix[i][y]=10
    Q=np.zeros((rewmatrix.shape[0],rewmatrix.shape[1]))
    return rewmatrix, Q

def adyMatrix(matrix2,goalx,goaly):
    matrix3 = np.zeros((matrix2.shape[0],matrix2.shape[1]))
    matrixAdy=[]
    #print("matrix 2 para ady matrix",matrix2)
    for i in range(matrix2.shape[0]):
        for l in range(matrix2.shape[1]):
            matrix3 = np.zeros((matrix2.shape[0],matrix2.shape[1]))
            #print("shape 0", matrix2.shape[0],"shape 1",matrix2.shape[1])       
            value=matrix2[i][l]
            # Caso #1 Two neighbours    ESQUINAS
            #print("valor de i", i, "valor de y", y)
            if ((i==0) or (i==matrix3.shape[0]-1)) and ((l==0) or (l==matrix3.shape[1]-1)):  
                #print("primer if L", l, "matrix shape 1 -1",matrix3.shape[1]-1,"matrix shape 1 -2",matrix3.shape[1]-2,"i es ",i)
                if (i==0) and (l==0):
                    if (matrix2[i][l+1]==0)  or ((i==goalx) and (l+1==goaly)):
                        matrix3[i][l+1]=1
                    if (matrix2[i+1][l]==0)  or ((i+1==goalx) and (l==goaly)): 
                        matrix3[i+1][l]=1
                elif ((i==0) and (l==matrix3.shape[1]-1)):
                    if (matrix2[i][l-1]==0)  or ((i==goalx) and (l-1==goaly)):
                        matrix3[i][l-1]=1
                    if (matrix2[i+1][l]==0)  or ((i+1==goalx) and (l==goaly)): 
                        matrix3[i+1][l]=1
                elif(i==matrix3.shape[0]-1) and (l==0):
                    if (matrix2[i-1][l]==0) or ((i-1==goalx) and (l==goaly)):
                        matrix3[i-1][l]=1
                    if (matrix2[i][l+1]==0)  or ((i==goalx) and (l+1==goaly)): 
                        matrix3[i][l+1]=1
                elif(i==matrix3.shape[0]-1) and (l==matrix3.shape[1]-1):
                    if (matrix2[i][l-1]==0)  or ((i==goalx) and (l-1==goaly)):
                        matrix3[i][l-1]=1
                    if (matrix2[i-1][l]==0) or ((i-1==goalx) and (l==goaly)): 
                        matrix3[i-1][l]=1
            #caso 2 Three neighbours   BORDES
            if ((l>0) and (l!=matrix3.shape[1]-1)) or ((i>0) and (i!=matrix3.shape[0]-1)):
                #print("segundo if L", l, "matrix shape 1 -1",matrix3.shape[1]-1,"matrix shape 1 -2",matrix3.shape[1]-2,"i es ",i)
                if(l==matrix3.shape[1]-1):#right edge
                    if(matrix2[i+1][l]==0) or ((i+1==goalx) and (l==goaly)):
                        matrix3[i+1][l]=1
                    if(matrix2[i-1][l]==0) or ((i-1==goalx) and (l==goaly)):
                        matrix3[i-1][l]=1
                    if(matrix2[i][l-1]==0) or ((i==goalx) and (l-1==goaly)):
                        matrix3[i][l-1]=1
                if(i==matrix3.shape[0]-1):#bottom edge
                    if(matrix2[i][l+1]==0)  or ((i==goalx) and (l+1==goaly)):
                        matrix3[i][l+1]=1
                    if(matrix2[i-1][l]==0)  or ((i-1==goalx) and (l==goaly)):
                        matrix3[i-1][l]=1
                    if(matrix2[i][l-1]==0) or ((i==goalx) and (l-1==goaly)):
                        matrix3[i][l-1]=1
                if(i==0):                   #upper edge
                    if(matrix2[i][l+1]==0) or ((i==goalx) and (l+1==goaly)):
                        matrix3[i][l+1]=1
                    if(matrix2[i+1][l]==0) or ((i+1==goalx) and (l==goaly)):
                        matrix3[i+1][l]=1
                    if(matrix2[i][l-1]==0) or ((i==goalx) and (l-1==goaly)):
                        matrix3[i][l-1]=1
                if(l==0) and (i!=0) and (i!=matrix3.shape[0]-1):                   #left edge
                    if(matrix2[i+1][l]==0) or ((i+1==goalx) and (l==goaly)):
                        matrix3[i+1][l]=1
                    if(matrix2[i-1][l]==0) or ((i-1==goalx) and (l==goaly)):
                        matrix3[i-1][l]=1
                    if(matrix2[i][l+1]==0) or ((i==goalx) and (l+1==goaly)):
                        matrix3[i][l+1]=1
            #caso 3 Four neighbours     LOS DEL CENTRO
            if (l>0) and (l<matrix3.shape[1]-1) and (i>0) and (i<matrix3.shape[0]-1):
                #print("tercer if L", l, "matrix shape 1 -1",matrix3.shape[1]-1,"matrix shape 1 -2",matrix3.shape[1]-2,"i es ",i)
                #print("matrix2",matrix2)
                #print("goalx",goalx,"goaly",goaly)
                if (matrix2[i-1][l]==0) or ((i-1==goalx) and (l==goaly)):
                   # print("matrix if1",matrix2[i-1][l]==0, (i-1==goalx) and (l==goaly))
                    matrix3[i-1][l]=1
                   # print("------if1",matrix3, "i-1",i-1,"l",l)
                if (matrix2[i][l-1]==0) or ((i==goalx) and (l-1==goaly)):
                   # print("matrix2 if2",matrix2[i-1][l]==0, (i==goalx) and (l-1==goaly))
                    matrix3[i][l-1]=1
                   # print("------if 2",matrix3, "i",i,"l-1",l-1)
                if (matrix2[i+1][l]==0) or ((i+1==goalx) and (l==goaly)):
                   # print("matrix2 if3",matrix2[i-1][l]==0, (i+1==goalx) and (l==goaly))
                    matrix3[i+1][l]=1
                   # print("------if 3",matrix3, "i+1",i+1,"l",l)
                if (matrix2[i][l+1]==0) or ((i==goalx) and (l+1==goaly)):
                   # print("matrix2 if4",matrix2[i-1][l]==0, (i==goalx) and (l+1==goaly))
                    matrix3[i][l+1]=1
                   # print("------if 4",matrix3, "i",i,"l+1",l+1)
           # if (i==goalx) and (l==goaly):
#                matrix3[i][l]=1
            m3flat=matrix3.flatten()
            matrixAdy.append(matrix3.flatten())
#            print("para elcaso l", l, "los vecinos son",matrix3,"i es ",i)
    matrixAdy=np.array(matrixAdy)
    np.savetxt("matrizady.txt",np.array(matrixAdy),fmt="%s")
    print("matrixAdy",matrixAdy)
    return matrixAdy

def possiblenext(currents, matrixAdy, nstates):
    possnext=[]
    for i in range(nstates):
        if (matrixAdy[currents][i]==1):
            possnext.append(i)
    print("current state",currents,"number of states",nstates)
    print("possiblenext",possnext)
   # print("possible next de estado 10",possnext[10])
    return possnext

def randomnext(currents, matrixAdy, nstates):
    possnext=possiblenext(currents,matrixAdy,nstates)
    print("possnext", possnext, "currents", currents, "nstates", nstates)
    nextstate=possnext[(np.random.randint(0,len(possnext)))]
    print("current state",currents,"number of states",nstates)
    print("random next",nextstate)
    return nextstate

def train(matrixAdy, rewmatrix, Q, gamma, lr, nstates, epochs, goal): #goal es la prs 1 2 3 4 ol 5
    vpasos=[]
    for i in range (0, epochs):
        currents=np.random.randint(0,nstates)
        print("currents",currents)
        print("epocaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", i)
        pasos=0
        while(True):
            nextstate=randomnext(currents,matrixAdy,nstates)
            possnextnext=possiblenext(nextstate,matrixAdy,nstates)
            
            maxq=-9999.99
            for j in range(len(possnextnext)):
                nns=possnextnext[j]
                q=Q[nextstate,nns]
                if q>maxq:
                    maxq=q
            Q[currents][nextstate]= ((1-lr)*Q[currents][nextstate])+(lr*(rewmatrix[currents][nextstate]+(gamma*maxq)))
            pasos=pasos+1
            print("calculo de Q y nuevo estado",nextstate,Q)
            print("currents",currents,"goal",goal,"--------------------------------")
            currents=nextstate
            if currents==goal:
                break
            print("el numero de pasos en esta epoca fué*******************",pasos)
        vpasos.append(pasos) #vector de pasos
        print("epoca actual",i,"epocas totales",epochs)
        np.savetxt("matrizq.txt",np.array(Q),fmt="%s")
    return Q,vpasos

def my_print(Q, dec):
    rows = len(Q); cols = len(Q[0])
    print("Q",Q,"rows",rows)
    print("       0      1      2      3      4      5      6      7      8      9      10     11     12     13     14     15    16    17    18    19    20")
    for i in range(rows):
        print("%d " % i, end="")
        if i < 10: print(" ", end="")
        for j in range(cols): print(" %6.2f" % Q[i,j], end="")
        print("")
    print("")

def walk(people, indexes, permactual, Qcaminos):
    caminata=[]
    for f in range (people+1):
        #para que cuando inicie se ubique en el robot (que es el ultimo en people pos)
        inicio=permactual[f] 
        print("f",f,"inicio",inicio,"people_pos",people_pos,"permactual",permactual)
        startstate=indexes[int(people_pos[(inicio-1)][0])][int(people_pos[(inicio-1)][1])]
        curr = startstate
        print(str(curr) + "->", end="")
        goal=permactual[f+1]
        estadogoal=indexes[int(people_pos[(goal-1)][0])][int(people_pos[(goal-1)][1])]
        print("inicio en",inicio,"el obajetivo es",goal,"osea voy del estado",startstate,"al estado",estadogoal)
        while curr != estadogoal:
            print("curr",curr)
            row = Qcaminos[f,int(curr),:]
            next = np.argmax(row)
            caminata.append(curr)
            print(str(next) + "->", end="") 
            curr = next
            np.savetxt("caminata.txt",caminata,fmt="%s")
    print("el numero de pasos de la caminata fue",len(caminata))
    print("el camino recorrido fue",caminata)
    print("done")


##################################################################################################################################
mm=0
people=0
l=[]
xcuad=20
ycuad=14
lr=0.5
gamma=0.5
epochs=1000


while ((mm==0) or (people>5)):
    print ("Number of people between 0 and 5")
    people = int(input())
    mm=1

for i in range(0,people):
    l.append(i+1) #vector para poder hacer las permutaciones

print("Vector of people",l)

while ((xcuad>18 or ycuad>12)):
    print ("Size of the room -rows-")
    xcuad = int(input())
    print ("Size of the room -columns-")
    ycuad = int(input())
    matrix=np.zeros((xcuad,ycuad)) ##crear la matriz principal, llena de ceros
    nstates=xcuad*ycuad

people_pos=np.zeros((people+1,2)) #es people+1 para incluir el punto del robot en esa misma matriz
pepos=np.zeros((people+1,2))
people_coord=[np.array((0,0)) for x in range(people+1)]
for i in range(people+1):         #ubicaciones de las personas Y del punto de inicio   
    print("i",i)
    print("people",people)
    if (i<people):        #coordenadas de las personas
        pp=0
        while (pp==0): #para hacer que no se puedan poner dos personas en una misma coordenada
            print ('Type coordinates of person #', i+1)
            print ('Row =')
            people_pos[i][0] = int(input()) #coordenada de la persona en fila
            print ('Column =')
            people_pos[i][1] = int(input()) #coordenada de la persona en columna
            people_coord[i]=np.array((people_pos[i][0],people_pos[i][1]))
            if (any((pepos[:]==people_coord[i]).all(1))==False):
                pp=1
            if (any((pepos[:]==people_coord[i]).all(1))==True):
                print("This value is already used, please try another")
            if (people_pos[i][0]>=xcuad):
                pp=0
                print("The row value is higher than the limit of the room, please try another ")
            if (people_pos[i][1]>=ycuad):
                pp=0
                print("The column value is higher than the limit of the room, please try another ")
        pepos[i][0]=people_pos[i][0]
        pepos[i][1]=people_pos[i][1]
        #matrix[people_pos[i][0]][people_pos[i][1]]= 1  #en las coordenadas de x y Y de la persona, la ubico en la matriz principal
        people_coord[i]=np.array((people_pos[i][0],people_pos[i][1]))
    
    if (i==people):        #coordenada de inicio y fin
        pp=0
        while (pp==0):   #para no poner el robot en el mismo punto que alguna persona
            print ('Type START Row coordinate of the robot ')
            people_pos[i][0] = int(input())
            print ('Type START Column coordinate of the robot ')
            people_pos[i][1] = int(input())
            people_coord[i]=np.array((people_pos[i][0],people_pos[i][1]))
            if (any((pepos[:]==people_coord[i]).all(1))==False):
                pp=1
            if (any((pepos[:]==people_coord[i]).all(1))==True):
                print("This value is already used, please try another")
            if (people_pos[i][0]>=xcuad):
                pp=0
                print("The Row value is higher than the limit of the room, please try another ")
            if (people_pos[i][1]>=ycuad):
                pp=0
                print("The Column value is higher than the limit of the room, please try another ")
        pepos[i][0]=people_pos[i][0]
        pepos[i][1]=people_pos[i][1]
        people_coord[i]=np.array((people_pos[i][0],people_pos[i][1]))

    print ("coordenadas de las personas",people_coord[i])

print ('Type number of obstacles:')               
obs = int(input())
obs_list = np.zeros((obs,2))
obst=np.zeros((obs,2))
obstacles=[np.array((0,0)) for x in range(obs)]
for i in range(obs):
    pp=0
    while (pp==0):   #para no poner el robot en el mismo punto que alguna persona
        print ('Type coordinates of obstacle #',i+1)
        print ('Row =')
        obs_list[i][0] = int(input())
        print ('Column =')
        obs_list[i][1] = int(input())
        obstacles[i]=np.array((obs_list[i][0],obs_list[i][1]))
        if ((any((obst[:]==obstacles[i]).all(1))==False) and(any((pepos[:]==obstacles[i]).all(1))==False )):
            pp=1
        if ((any((obst[:]==obstacles[i]).all(1))==True) or(any((pepos[:]==obstacles[i]).all(1))==True )):
            print("This value is already used, please try another")
        if (obs_list[i][0]>xcuad):
            pp=0
            print("The X value is higher than the limit of the room, please try another ")
        if (obs_list[i][1]>ycuad):
            pp=0
            print("The Y value is higher than the limit of the room, please try another ")
    #matrix[obs_list[i][0]][obs_list[i][1]]= -1 # en las coordenadas de x y Y, ubico un -1 que representa los obstaculos
    obst[i][0]=obs_list[i][0]
    obst[i][1]=obs_list[i][1]


lista,tot= permute(l)
if (type(lista)!=int): ## no debe ser general porque esto no aplica para cuando solo hay una persona y lista no es una lista
    lista=lista.astype(np.int64)
    print("intento", lista[0]) 
    distanciapermutacion=np.zeros(tot)

    ###########################################################

    for i in range (tot):  ###para que se haga tantas veces como permutaciones de los caminos
        permactual=lista[i]
        permactual=permtotal(permactual,people)
        permactual=permactual.astype(np.int64)
        print("permutacion actual ",permactual)
        for y in range(people+3):
            if (y<(people+2-1)): #para que no intente hacerlo con el ultimo vs el siquiente
                print("people",people+3, "y",y)
                print ("valor numero",y ," en la permutacion", i, "es ",permactual[y]) #y es la persona 1 
                primero=permactual[y] 
                segundo=permactual[y+1]
                print("primero",primero, "coordenadas", people_coord[primero-1], "segundo",segundo, "coordenadas", people_coord[segundo-1])
                distpareja=np.linalg.norm(people_coord[primero-1]-people_coord[segundo-1])
                distanciapermutacion[i]=distanciapermutacion[i]+distpareja  #distancia camino =distancia camino + distancia pareja
                print("la distancia entre", primero, "y", segundo,"es", distpareja) 
                print("distancia de la permutacion total es ", distanciapermutacion[i])
        if (i==0):
            distmin=distanciapermutacion[i]  #numero de permutacion en la que esta el valor minimo
            permin=i         #Valor de distancia minimo
        if (distanciapermutacion[i]<distmin):
            distmin=distanciapermutacion[i]
            permin=i

        
        print ("distancia de permutacion ",i,"es ",distanciapermutacion[i])
        print ("La distancia minima hasta el momento es", distmin, "de la permutacion ", permin)
        print ("Siguiente permutacion de personas")

    perminima=lista[permin]
    print("la permutacion de personas con la minima distancia recorrida fue ",perminima)

if (type(lista)==int): #para que funcione tambien si hay solo una persona
    perminima=lista
    permactual=np.array([people+1, perminima, people+1])
    print("parmactual",permactual,"perminima",perminima)

matrixq=np.zeros((nstates,nstates))

#para que visite cada persona, tiene que sumarse 1 a visitar cuando llegue donde la primera persona en el multimatriz, es como un contador de cuantos ha visitado
Qcaminos=np.zeros(((people+1),nstates,nstates))
goalss=[]

a=0
b=0
c=0
for k in range (people+1): #CICLO PARA CREAR LAS MATRICES Q NECESARIAS, para cada persona Y para el robot 
    matrixq=np.zeros((nstates,nstates))
    if (k<people) and (type(lista)!=int):
        nopersona=perminima[k] #no persona es el numero de la persona que va a visitar primero (prs 1 2 3 4 o 5) [4 2 1 3 5]
    if (type(lista)==int):
        nopersona=lista
    matrix=originalmatrix(people_pos, people, obs_list, obs)
    if k==people:  ##para el caso del robot
        nopersona=people+1
    numper=nopersona-1 #numper me dice el lugar en el vector de la persojna que voy a visitar primero porque en el vector van de 0 a 4 
    print("Tamaño people pos",len(people_pos),"no persona", nopersona, "peoplepos", people_pos,"en x",people_pos[numper][0])
    indexes=matrixindex(matrix)
    estadogoal=indexes[int(people_pos[numper][0])][int(people_pos[numper][1])]
    estadogoalx=int(people_pos[numper][0])
    estadogoaly=int(people_pos[numper][1])
    #print("estado",estadogoal,"goalx",estadogoalx,"goaly",estadogoaly)
    adymatrix=adyMatrix(matrix,estadogoalx,estadogoaly)
    goalss.append(estadogoal)
    #######coordgoal=[int(people_pos[numper][0]), int(people_pos[numper][1])]

    rewards, Q=rewmatrix(adymatrix,estadogoal)
    matrixq,vpasos=train(adymatrix, rewards, Q, gamma, lr, nstates, epochs, estadogoal)
    Qcaminos[k]=matrixq
    if k==0:
        a=1
        np.savetxt("Qcaminos1.txt",np.array(matrixq),fmt="%s")
    if k==1:
        b=1
        np.savetxt("Qcaminos2.txt",np.array(matrixq),fmt="%s")
    if k==2:
        c=1
        np.savetxt("Qcaminos3.txt",np.array(matrixq),fmt="%s")
    #print(vpasos,matrixq)

print("Qcaminos",Qcaminos)
for i in range (people+1):
    if i==0:
        np.savetxt("Qcaminoss1.txt",np.array(Qcaminos[i]),fmt="%s")
    if i==1:
        np.savetxt("Qcaminoss2.txt",np.array(Qcaminos[i]),fmt="%s")
    if i==2:
        np.savetxt("Qcaminoss3.txt",np.array(Qcaminos[i]),fmt="%s")
#    if i==3:
#        np.savetxt("Qcaminos4.txt",np.array(Qcaminos[i]),fmt="%s")
#    if i==4:
#        np.savetxt("Qcaminos5.txt",np.array(Qcaminos[i]),fmt="%s")
#    if i==5:
#        np.savetxt("Qcaminos6.txt",np.array(Qcaminos[i]),fmt="%s")
robot_s=indexes[int(people_pos[people][0])][int(people_pos[people][1])]#estado inicial del robot
print("estado robot",robot_s)
walk(people, indexes, permactual, Qcaminos)
print("goals",goalss)
print("obstaculos", obs_list)
print("personas",people_pos)
if (type(lista)!=int):
    print("permutacion",lista[permin])

