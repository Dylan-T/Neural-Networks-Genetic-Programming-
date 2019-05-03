from gplearn.genetic import SymbolicRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.utils.random import check_random_state
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
# import graphviz


""" Samples are the given data aka 20 given points, these can be used for both training and testing????"""

"""Since it’s a fairly small dataset, we can probably use a large population since training time will still be pretty 
fast. We’ll evolve 20 generations unless the error falls below 0.01."""

"""he default function set of addition, subtraction, multiplication and division will cover us"""

""" Load in regression.txt into 2d array """
inText = open("regression.txt", "r")
inText = inText.read().splitlines()
xtrain = []
ytrain = []

for i in range(2, len(inText)):
    tokens = inText[i].split()
    xtrain.append([float(tokens[0])])
    ytrain.append(float(tokens[1]))

print(xtrain)
print(ytrain)

est_gp = SymbolicRegressor(population_size=5000,
                           generations=20, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0)


est_gp.fit(xtrain, ytrain)





print(est_gp._program)  # Print the best program

"""Test data"""


"""Print program tree"""
# graph = pydotplus.graphviz.graph_from_dot_data(est_gp._program.export_graphviz())
# Image(graph.create_png())
