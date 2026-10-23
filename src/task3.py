import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

marks = np.array([
    [75, 82, 90], 
    [58, 65, 70],
    [88, 91, 85],
    [45, 52, 60]]
)


print(f"Shape of marks array: {marks.shape}")


student_averages = np.mean(marks, axis=1)
subject_averages = np.mean(marks, axis=0)
print(f"Student Averages (axis=1): {student_averages}")
print(f"Subject Averages (axis=0): {subject_averages}")


grace_marks = marks + 5
print(f"Marks after adding 5 grace marks:\n{grace_marks}")


weights = np.array([0.3, 0.4, 0.3])
weighted_scores = np.dot(marks, weights)
print(f"Weighted Scores: {weighted_scores}\n")

departments_data = """department,head,budget
Sales,Alice,50000
HR,Bob,40000
IT,Charlie,80000
Finance,Diana,60000
Marketing,Evan,30000"""


employees_data = """emp_id,name,department,salary
1,John,Sales,55000
2,Jane,Sales,58000
3,Mike,HR,
4,Emily,HR,45000
5,Alex,IT,75000
6,Sam,IT,
7,Tom,IT,72000
8,Anna,Finance,62000
8,Anna,Finance,62000"""  

departments_df = pd.read_csv(io.StringIO(departments_data)) 
departments_df.to_csv("departments.csv", index=False)

employees_raw_df = pd.read_csv(io.StringIO(employees_data))
employees_raw_df.to_csv("employees.csv",index=False)

employees_df = pd.read_csv("employees.csv")
print("\n--- df.info() ---")

employees_df.info()
print("\n--- df.describe() ---")
print(employees_df.describe(include="all"))


print("\nUsing .loc (First 3 rows, name and salary columns):")
print(employees_df.loc[0:2, ["name", "salary"]])

print("\nUsing .iloc (Row indices 1 to 3, column indices 0 to 2):")
print(employees_df.iloc[1:4, 0:3])

print("\nFiltering employees with salary > 60000:")
print(employees_df[employees_df["salary"] > 60000])

print("\nCleaning Data...")

employees_df = employees_df.drop_duplicates()


median_salary = employees_df["salary"].median()
employees_df["salary"] = employees_df["salary"].fillna(median_salary)

employees_df["salary"] = employees_df["salary"].astype(int)
print("Cleaned Employees DataFrame:")
print(employees_df)


print("\nGroupby Department Metrics:")
grouped_summary = (
    employees_df.groupby("department")
    .agg(
        headcount=("emp_id", "count"),
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
    )
    .reset_index()
)

print(grouped_summary)

departments_df = pd.read_csv("departments.csv")

inner_merge = pd.merge(employees_df, departments_df, on="department", how="inner")
left_merge = pd.merge(employees_df, departments_df, on="department", how="left")
outer_merge = pd.merge(employees_df, departments_df, on="department", how="outer")


no_emp_dept = outer_merge[outer_merge["emp_id"].isna()]["department"].values[0]
print(f"\nOuter join target: Department with no employees is '{no_emp_dept}'.\n")


fig, axis = plt.subplots(2, 2, figsize=(12, 8))
axis[0, 0].bar(
    grouped_summary["department"],
    grouped_summary["headcount"],
    color="skyblue",
    label="Employee Count",
)
axis[0, 0].set_title("Employee Headcount by Department")
axis[0, 0].set_xlabel("Department")
axis[0, 0].set_ylabel("Headcount")
axis[0, 0].legend()


axis[0, 1].hist(
    employees_df["salary"], bins=5, color="lightgreen", edgecolor="black", label="Salary"
)
axis[0, 1].set_title("Salary Distribution of Employees")
axis[0, 1].set_xlabel("Salary Range")
axis[0, 1].set_ylabel("Frequency")
axis[0, 1].legend()


merged_summary = pd.merge(grouped_summary, departments_df, on="department")
axis[1, 0].scatter(
    merged_summary["budget"],
    merged_summary["max_salary"],
    color="coral",
    s=100,
    label="Depts",
)
axis[1, 0].set_title("Department Budget vs Max Salary")
axis[1, 0].set_xlabel("Budget ($)")
axis[1, 0].set_ylabel("Max Salary ($)")
axis[1, 0].legend()


axis[1, 1].plot(
    grouped_summary["department"],
    grouped_summary["avg_salary"],
    marker="o",
    color="orchid",
    linewidth=2,
    label="Avg Salary",
)

axis[1, 1].set_title("Average Salary Trend Across Departments")
axis[1, 1].set_xlabel("Department")
axis[1, 1].set_ylabel("Average Salary ($)")
axis[1, 1].legend()

plt.tight_layout()
plt.savefig("department_insights.png")

print("Visualizations successfully saved as 'department_insights.png'.")

print("\n--- Visual Insights ---")
print(
    "1. Bar Chart: The IT department holds the largest headcount with 3 active employees, while Finance has the least."
)
print(
    "2. Histogram: Most employee salaries fall mid-range within the $55,000 to $65,000 cluster due to imputation."
)
print(
    "3. Scatter Plot: There is a positive correlation trend indicating departments with higher budgets command a higher ceiling for peak salaries."
)
print(
    "4. Line Chart: The IT department commands the highest average salary line while HR possesses the lowest baseline average budget."
)

