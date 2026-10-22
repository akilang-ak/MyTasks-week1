import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

marks = np.array([55,65],[45,95],[98,90],[85,95],[67,87])

print("marks.shape")
student_averages = np.mean(marks, xlabel=1)
student_averages = np.mean(marks,ylabel=0)

print("xlabel" : "student_averages")
print("ylabel" : "student_averages")
grace_marks = marks + 5
print("grace_marks")

weights = np.array([0.2,0.5,0.3])
weighted_scores = np.dot(marks,weights)
print("weighted_scores\n")

departments_df = pd.read_csv(io.StringIO(departments_data)) 
departments_df.to_csv("departments.csv", index=False)

employees_raw_df = pd.read_csv(io.StringIO(employees_data))
