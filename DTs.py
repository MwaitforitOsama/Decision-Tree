
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

dataset = pd.read_csv('Pig_Diseases_Training.csv')
# print(dataset)
X = dataset.iloc[:, 1:].values





attribute = ['Skin lesions', 'Coughing', 'Diarrhea', 'Diarrhea with blood', 'Itching', 'Dermatitis', 'Vomiting', 'Loss of apetite','Higher Body temperature','Reduced milk production','Blood in dung','redness or blue blotching of the skin on ears, nose and limbs','nasal and eye discharges','pneumonia','arthritis','Reduced Growth Rate','Scratching']
# print(X)

class Node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.childs = None


def findEntropy(data, rows):
    yes = 0
    no = 0
    ans = -1
    idx = len(data[0]) - 1
    
    entropy = 0
    for i in rows:
        if data[i][idx] == 'Swine dysentery' or 'Proliferative enteropathy (PE)(ileitis)' or 'Sarcoptic mange' :
            yes = yes + 1
            # print(yes)

        if data[i][idx] == 'Proliferative enteropathy (PE)(ileitis)' or 'Sarcoptic mange' :
            yes = yes + 1
            # print(yes)    

        if data[i][idx] == 'Sarcoptic mange' :
            yes = yes + 1
            # print(yes)


        if data[i][idx] ==  'Farrowing sickness (mastitis, metritis, agalactia - MMA)' :
            yes = yes + 1
            # print(yes)    


        if data[i][idx] ==  'Internal Parasites (worms)' :
            yes = yes + 1
            # print(yes)  
        if data[i][idx] == 'Gastric ulceration' :
            yes = yes + 1
            # print(yes) 
        if data[i][idx] == 'Erysipelas' : #'Exudative epidirmitis' or 'Gastric ulcers' or 'African Swine Fever'
            yes = yes + 1
            # print(yes)
        if data[i][idx] == 'Exudative epidirmitis':
            yes = yes + 1
            # print(yes)
        if data[i][idx] == 'Gastric ulcers':
            yes = yes + 1
            # print(yes) 
        if data[i][idx] == 'African Swine Fever':
            yes = yes + 1
            # print(yes)             
                      
        else:
            no = no + 1

    x = yes/(yes+no)
    y = no/(yes+no)
    if x != 0 and y != 0:
        entropy = -1 * (x*math.log2(x) + y*math.log2(y))
    if x == 1:
        ans = 1
    if y == 1:
        ans = 0
    return entropy, ans


def findMaxGain(data, rows, columns):
    maxGain = 0
    retidx = -1
    entropy, ans = findEntropy(data, rows)
    if entropy == 0:
        """if ans == 1:
            print("Yes")
        else:
            print("No")"""
        return maxGain, retidx, ans

    for j in columns:
        mydict = {}
        idx = j
        for i in rows:
            key = data[i][idx]
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] = mydict[key] + 1
        gain = entropy

        # print(mydict)
        for key in mydict:
            yes = 0
            no = 0
            for k in rows:
                if data[k][j] == key:
                    if data[k][-1] == '1':
                        yes = yes + 1
                    else:
                        no = no + 1
            # print(yes, no)
            x = yes/(yes+no)
            y = no/(yes+no)
            # print(x, y)
            if x != 0 and y != 0:
                gain += (mydict[key] * (x*math.log2(x) + y*math.log2(y)))/10
        # print(gain)
        if gain > maxGain:
            # print("hello")
            maxGain = gain
            retidx = j
            

    return maxGain, retidx, ans


def buildTree(data, rows, columns):

    maxGain, idx, ans = findMaxGain(X, rows, columns)
    root = Node()
    root.childs = []
    # print(maxGain
    #
    # )
    if maxGain == 0:
        if ans == 1:
            root.value = 'Yes'
        else:
            root.value = 'No'
        return root

    root.value = attribute[idx]
    mydict = {}
    for i in rows:
        key = data[i][idx]
        if key not in mydict:
            mydict[key] = 1
        else:
            mydict[key] += 1

    newcolumns = copy.deepcopy(columns)
    newcolumns.remove(idx)
    for key in mydict:
        newrows = []
        for i in rows:
            if data[i][idx] == key:
                newrows.append(i)
        # print(newrows)
        temp = buildTree(data, newrows, newcolumns)
        temp.decision = key
        root.childs.append(temp)
    return root


def traverse(root):
    print(root.decision)
    print(root.value)

    n = len(root.childs)
    if n > 0:
        for i in range(0, n):
            traverse(root.childs[i])


def calculate():
    rows = [i for i in range(0, 10)]
    columns = [i for i in range(0, 17)]
    root = buildTree(X, rows, columns)
    root.decision = 'Start'
    traverse(root)


calculate()





# or  or 