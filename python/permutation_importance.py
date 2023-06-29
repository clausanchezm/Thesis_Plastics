import os
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
os.getcwd()

#preprocess to  separte target and drop other properties
def drop_cols(data):
    xE = data.drop(['blendE', 'blendSTRENGTH', 'blendStrainbreak', 'blendImpact', 'impurityImpact', 'impuritySTRENGTH',
                    'impurityStrainbreak', 'matrixImpact', 'matrixSTRENGTH', 'matrixStrainbreak'], axis=1)
    yE = data[['blendE']]
    return xE, yE


def get_importances(x, y):
    # no need for splitting the data, its used as FS methd
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    rf = RandomForestRegressor()
    # Fit the model on the training data
    rf.fit(X_train, y_train)
    result = permutation_importance(
        rf, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
    )
    importances_mean = result.importances_mean
    sorted_importances_idx = importances_mean.argsort()[::-1][:10]
    return sorted_importances_idx


#set local path to save results
folder_to_export_path = ""
data = pd.read_csv('data/data_reduced.csv')
dataP = pd.read_csv('data/data_reduced_p.csv')
dataNP = pd.read_csv('data/data_reduced_np.csv')
dataLT = pd.read_csv('data/data_reduced_linear_topo.csv')
dataBT = pd.read_csv('data/data_reduced_branched_topo.csv')
dataLC = pd.read_csv('data/data_reduced_low_crys.csv')
dataAC = pd.read_csv('data/data_reduced_amorp_crys.csv')
dataHC = pd.read_csv('data/data_reduced_high_crys.csv')

xW, yW = drop_cols(data)
xP, yP = drop_cols(dataP)
xNP, yNP = drop_cols(dataNP)
xLT, yLT = drop_cols(dataLT)
xBT, yBT = drop_cols(dataBT)
xLC, yLC = drop_cols(dataLC)
xAC, yAC = drop_cols(dataAC)
xHC, yHC = drop_cols(dataHC)

perW = get_importances(xW, yW)
perP = get_importances(xP, yP)
perNP = get_importances(xNP,yNP)
perLT = get_importances(xLT,yLT)
perBT = get_importances(xBT,yBT)
perLC = get_importances(xLC,yLC)
perAC = get_importances(xAC,yAC)
perHC = get_importances(xHC,yHC)

#following the order of matlab
concatenated = pd.DataFrame([perW, perP, perNP, perLT, perBT, perLC, perAC, perHC])
print('indiced of whole ')
print(perW)
print('index of p ')
print(perP)
print(concatenated)


concatenated.to_csv(os.getcwd() + '/data/rf_permutation_partitions.csv', index=False)

# X_trainW, X_testW, y_trainW, y_testW = train_test_split(xW,yW, test_size=0.1, random_state=42)
# X_trainP, X_testP, y_trainP, y_testP = train_test_split(xP,yP, test_size=0.1, random_state=42)
# X_trainNP, X_testNP, y_trainNP, y_testNP = train_test_split(xNP,yNP, test_size=0.1, random_state=42)
# rf = RandomForestRegressor()
# # Fit the model on the training data
# rf.fit(X_trainW, y_trainW)
# print(rf.feature_importances_)
#
# resultW = permutation_importance(
#     rf, X_testW, y_testW, n_repeats=10, random_state=42, n_jobs=2
# )
# sorted_importances_idx = resultW.importances_mean.argsort()
# # Sort the importances DataFrame based on mean importance values
# print(sorted_importances_idx)
#
# importances = pd.DataFrame(
#     resultW.importances[sorted_importances_idx].T,
#     columns=xW.columns[sorted_importances_idx],
# )
# # get best 10
# sorted_importances = importances.mean().sort_values()
# top_10_features = sorted_importances.tail(10).index.tolist()
# print(top_10_features)
# print(importances)
# ax = importances.plot.box(vert=False, whis=10)
# ax.set_title("Permutation Importances (test set)")
# ax.axvline(x=0, color="k", linestyle="--")
# ax.set_xlabel("Decrease in accuracy score")
# ax.figure.tight_layout()
# ax.figure.show()
