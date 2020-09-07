import gurobipy as gp
from gurobipy import GRB
try:
 m=gp.Model("problem 1")
# Add variables
 x14 = m.addVar(vtype=GRB.BINARY, name="x14") # initialize variable x14
 x24 = m.addVar(vtype=GRB.BINARY, name="x24") # initialize variable x24
 x15 = m.addVar(vtype=GRB.BINARY, name="x15") # initialize variable x15
 x25 = m.addVar(vtype=GRB.BINARY, name="x25") # initialize variable x25

# Set objective function
 m.setObjective(130*x14 + 95*x24 + 118*x15 + 83*x25, GRB.MINIMIZE) #this is the function to be minimized as explained in ans 1

# Add constraints 
 c1 = m.addConstr(x14 + x15 >= 1) #sum of first column must be 1
 c2 = m.addConstr(x14 + x24 >= 1) #sum of first row must be 1
 c3 = m.addConstr(x24 + x25 >= 1) #sum of second column must be 1
 c4 = m.addConstr(x15 + x25 >= 1) #sum of second row must be 1
# Solve model 
 m.optimize()

except gp.GurobiError as e:
 print ('Error code ' + str(e.errno) + ':' + str(e))

except AttributeError:
 print ('Encountered an attribute error')  
