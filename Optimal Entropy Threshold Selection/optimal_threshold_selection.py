# -*- coding: utf-8 -*-
"""Optimal_Threshold_Selection_Example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q49lIaXyDWVxo58qgSpkO_Z5LCaXnX0S
"""

# Find optimal entropy threshold that minimizes the Index of Union in ROC analysis (Unal, 2017)
# https://www.hindawi.com/journals/cmmm/2017/3762651/

# Given a true positive rate (tpr), false positive rate (fpr), and auc score (calculated along different
# threshold entropy values (thresh), we can find the optimal cut-point that minimizes the index 
import numpy as np 
import torch
tpr = [0. , 0. , 0.2, 0.2, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.9, 0.9, 1. , 1.]

fpr =   [0.        , 0.01030928, 0.01030928, 0.03092784, 0.03092784,
         0.04123711, 0.04123711, 0.07216495, 0.07216495, 0.21649485,
         0.21649485, 0.25773196, 0.25773196, 0.26804124, 0.26804124,
         0.43298969, 0.43298969, 1. ]

thresh = [2.59153576e+00, 1.59153576e+00, 1.22331687e+00, 1.06857835e+00, 
          9.41533179e-01, 9.19037569e-01, 8.86617051e-01, 6.03690206e-01,
          5.79343707e-01, 3.08493897e-01, 2.56220832e-01, 1.73363876e-01,
          1.42393021e-01, 1.40865165e-01, 1.37868911e-01, 2.52726638e-02,
          2.46056614e-02, 9.39088318e-08]

Spe = 1 - np.array(fpr)
Sen = np.array(tpr)

auc_score = 0.8628865979381444

IU = torch.abs(torch.tensor((Sen - auc_score))) + torch.abs(torch.tensor((Spe - auc_score)))
Diff = torch.abs(torch.tensor(Sen-Spe))
IU_minimum_index = np.where(IU == IU.min())
Diff_minimum_index = np.where(Diff == Diff.min())

if torch.numel(torch.tensor(IU_minimum_index)) == 1:
  optimal_threshold = thresh[torch.tensor(IU_minimum_index).item()]
else:
  optimal_threshold = thresh[torch.tensor(Diff_minimum_index).item()] 

print(optima_threshold)
