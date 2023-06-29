import numpy as np
import pandas as pd

#data used
data = pd.read_excel("C:/Users/33789/OneDrive/Desktop/THESIS/data/Dataset_May2022_RD.xlsx")

#preprocesing into numeric only, 4 chemical properties are kept
d = data
# ratio of polymerB
d = d.replace({'impurityXc': {'PURE': 0}})
#POLYFINE VS NON POLYSINE
d = d.replace({'Matrix_family': {'Polyolefin': 0, 'Non-Polyolefin': 1}})
d = d.replace({'Contaminant_family': {'Polyolefin': 0, 'Non-Polyolefin': 1}})

# Branched or linear topology
d = d.replace({'Matrix_topology': {'Branched': 0, 'Linear': 1}})
d = d.replace({'Contaminant_topology': {'Branched': 0, 'Linear': 1}})

# crystlainity, amorphous shoudl be the lowest
#  1 is high so should be casted to 2; amorphous 0, and low to 1
d= d.replace({'Matrix_crystallinity': {1 :2}})
d = d.replace({'Matrix_crystallinity': {'Low': 1, 'Amorphous': 0}})
d= d.replace({'Contaminant_crystallinity': {1 :2}})
d = d.replace({'Contaminant_crystallinity': {'Low': 1, 'Amorphous': 0}})

# SCB
d = d.replace({'Matrix_SCB': {'None': 0, 'High': 1}})
d = d.replace({'Contaminant_SCB': {'None': 0, 'High': 1}})

# LCB
d = d.replace({'Matrix_LCB': {'None': 0, 'Low' :1, 'High': 2}})
d = d.replace({'Contaminant_LCB': {'None': 0, 'Low': 1, 'High': 2}})

d['Matrix_crystallinity'].unique()
# dropping series number and name and reeks
d = d.drop(['NAAM', 'SERIE', 'Reeks' ], axis=1)

# theoretical estimations
d = d.drop(['gammaABWu', 'Ddeltad2', 'Ddeltap2', 'Ddeltah2'], axis=1)
# Kims classes
d = d.drop(['Matrix Class','Impurity Class', 'Class Combo', 'POL', 'POK', 'NOK', 'NOA'], axis=1)
# ratios
d = d.drop(['EblendOpEmatrix', 'STRENGTHblendOpSTRENGTHmatrix',
       'StrainbreakblendOpStrainbreakmatrix', 'ImpactblendOpImpactmatrix' ], axis=1)

#only encode the type of polymer
h1D = pd.get_dummies(d, columns = ['MajorityPolymer', 'MinorityPolymer'])

#partitioning
#crystallinity
low = h1D[h1D['Matrix_crystallinity'] == 1]
high = h1D[h1D['Matrix_crystallinity'] == 2]
amor = h1D[h1D['Matrix_crystallinity'] == 0]
#topology
branched = h1D[h1D['Matrix_topology'] == 0]
linear = h1D[h1D['Matrix_topology'] == 1]

poly = h1D[h1D['Matrix_family'] == 0]
non_poly = h1D[h1D['Matrix_family'] == 1]

# SAVING DATA FILE
#set file location
folder_to_export_path = ""
branched.to_csv(folder_to_export_path+'data_reduced_branched_topo.csv', index=False)
linear.to_csv(folder_to_export_path+'data_reduced_linear_topo.csv', index=False)
low.to_csv(folder_to_export_path+ 'data/data_reduced_low_crys.csv', index= False)
amor.to_csv(folder_to_export_path+ 'data/data_reduced_amorp_crys.csv', index= False)
high.to_csv(folder_to_export_path+ 'data/data_reduced_high_crys.csv', index= False)
poly.to_csv(folder_to_export_path+'data_reduced_p.csv', index=False)
non_poly.to_csv(folder_to_export_path+'data_reduced_np.csv', index=False)