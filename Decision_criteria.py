import json
def VMPFC(si,a,m,p,e): #si:Stimulus, a:Hidonic, m:Magnitude, p:Probability, e:salience
    r = []
    mayor = []
    action = DLPPFC()# take the disponible actions from DLPFC function
    experience = VLPFC(si) #Use the historial associacions from VLPFC fuction  
   
    k=0.4 #volatil variable
    c =0.3 #volatil variable
    Pv = (k*(a*m*p))+(c*e)/(k+c) #Utility stabelized 
    print("Pv:",Pv)
    labelo = [Valorations(a),Valorations(m),Valorations(p),Valorations(e),Valorations(Pv)] #Label of status string 
    #rule
    if(experience !=0):
        if (Pv >= experience["Utility"]): #compare only the stimulus selected
            #labelo.append(Valorations(Pv)) #add the label to labels array
            r = [si,action,Pv] #crate tuple stimulus, action, Utility
        else:
            all=VLPFC(1) #incert "1" to obtain all the historial
            for i in all:
                mayor.append(i["Utility"])
                aa=max(mayor) #obtain the biggest utility from the historial
            for i in all:
                if aa == i["Utility"]: #look for the associasion corresponding with the biggest ulility
                    si = str(i["if"])
            r=[si, action,aa]    #append the new biggest associasion
    


    return labelo, r


def VLPFC(si):#Assosiations historial
    historial = ""
    memory_association = ({"Id":0,"if":"A" ,"then":1,"Utility":0.64},{"Id":1,"if":"B" ,"then":1,"Utility":0.23},
    {"Id":2,"if":"C" ,"then":1,"Utility":0.54},{"Id":3,"if":"D" ,"then":1,"Utility":0.70})
    a = json.dumps(memory_association)
    memory_association = json.loads(a)
    for i in memory_association:
        if(i["if"] == si):
            historial = i 
            print(historial)
    if(si == 1):
        historial = memory_association
    return historial

def DLPPFC():#disponible actions
    act = "selecto"
    return act


def Valorations(num): #Label Hidonic states
    val = []
    layer = ""
    if num >= 0.87:
        layer = "Excelente"
    elif num < 0.87 and num >= 0.55:
        layer = "Very_good"
    elif num < 0.55 and num >= 0.35:
        layer = "Good"
    elif num < 0.35 and num >= 0.15:
        layer = "More_less_good"
    elif num < 0.15 and num >= 0.01:
        layer = "Few_good"
    elif num == 0:
        layer = "Neutral"
    elif num > -0.15 and num <= -0.01:
        layer = "Few_bad"
    elif num > -0.35 and num <= -0.15:
        layer = "More_less_bad"
    elif num > -0.55 and num <= -0.35:
        layer = "Bad"
    elif num > -0.87 and num <= -0.55:
        layer = "Very_bad"
    elif num <= -0.87:
        layer = "Horrible"
    val.append(layer)

    return val

print(VMPFC("A", -0.53,0.57,1,-0.87)) #incert (stimulus, hidonic-value, reward-magnitude, reward-probability, incentive-salience)