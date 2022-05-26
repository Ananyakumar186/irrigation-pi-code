import pickle as pkl

def preprocess(l):
    inp=[]
    inp.append(l[1])
    inp.append(l[2])
    inp.append(l[3])
    inp.append(1)
    if l[4]=='clay':
        inp=inp+[1,0,0]
    elif l[4]=='silt':
        inp=inp+[0,1,0]
    else:
        inp=inp+[0,0,1]

    if l[6]>0 and l[6]<11:
        inp=inp+[1,0,0]
    elif l[6]>10 and l[6]<31:
        inp=inp+[0,1,0]
    else:
        inp=inp+[0,0,1]
    print(inp)
    return inp


    

def predict(l):
    inp=preprocess(l)
    if l[5]=='areca':
       mod=pkl.load(open('ml/model_areca.sav','rb'))
    else:
       mod=pkl.load(open('ml/model_coconut.sav','rb'))
    y_pred=mod.predict([inp])
    p=y_pred[0]
    if p<0:
        p=0
    print(p)
    return p
