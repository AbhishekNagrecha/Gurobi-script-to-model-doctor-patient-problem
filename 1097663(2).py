# here I need to Import all the essential libraries needed
from gurobipy import *
import numpy as np

#these are Value of  Time requirements (in minutes) for doctors to attend patients at ER at the hospital as told in the problem
#these were filled randomly as explained in the problem statement

data = [
   [75,66,85,99,55,58],
    
    [72,69,88,80,60,77],
    
    [100,122,126,136,140,142],
    
    [130,95,118,117,101,104],
    
    [118,83,103,81,148,141],
    
    [52,56,65,108,111,136]
]
dataArray = np.array(data)
matrixRowNumber = dataArray.shape[0]
matrixColumnNumber = dataArray.shape[1]

m = Model('matrix model')


#define variables
#now I have Initialized 36 (6*6) variables which are binary as its shown in the problem statement table 1 
#variable is matrixRowNumber array at size matrixColumnNumber : 
#6 array of size 6
#if selected 1 otherwise 0
selectVar = []

for index in range(matrixRowNumber):
    tempVar=m.addVars(
        matrixColumnNumber,
        lb=0,
        ub=1,
        vtype=GRB.BINARY,
        name='cell[{0}]'.format(index))
    selectVar.append(tempVar)


#define objective function:
#now i have to Set the objective function for the problem statement which in this case the overall
# summation of all the rows and columns needs to be minimized in order to find 
#the optimal time spent by one doctor to their individual patients.   
#Minimize(one to one product of selectVar * dataArry)  
objFunction = 0
#SUM(variable[i,j]*Data[i,j])  
#         for i=(0,len(rows)) & j=(0,len(columns))
for rowIndex in range(matrixRowNumber):
    for colIndex in range(matrixColumnNumber):
        objFunction += selectVar[rowIndex][colIndex] * dataArray[rowIndex,colIndex]
m.setObjective(objFunction, GRB.MINIMIZE)


#define Constraint
# these are the below mentioned constrains
#for the problem 2 statement wrt the table 1
# first we need to get the overall summation  of all selected variables in each rows and each columns to be 1
#sum of each row of variables = 1 
# sum(selectVar[0]) = 1,sum(selectVar[1]) = 1 , ....
for element in selectVar:
    m.addConstr(quicksum(element[i] for i in range(matrixColumnNumber)) == 1, 'rowsConstraint')

#sum of each columns of variables = 1 
# sum(selectVar[:][0]) = 1,sum(selectVar[:][1]) = 1 , ....
for colIndex in range(matrixColumnNumber):
    tempConstraint = 0
    for rowIndex in range(matrixRowNumber):
        tempConstraint += selectVar[rowIndex][colIndex]
    m.addConstr(tempConstraint == 1, 'columnsConstraint')


#now here we need to Optimize the given problem statement 
m.optimize()


#get the row and column of variable elemet
def getMatrixIndices(index):
    row=index//matrixRowNumber
    col=index % matrixColumnNumber
    return(row,col)
#get respected value in dataArray
def getDataValue(index):
    row , col = getMatrixIndices(index)
    return(dataArray[row,col])


#print Selected cells
for a in m.getVars():
    if(a.x != 0.0):
        print(a.varName,' : ', getDataValue(a.index) )






