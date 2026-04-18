import numpy as np
marks = np.array([78,85,62,90,55,88])
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
pass_students = marks[marks >= 60]
fail_students = marks[marks < 60]
grades = np.where(marks >= 75, "A", np.where(marks >= 60, "B","C"))
print("Grades:" ,grades)
print("pass:", marks[marks >= 60])
print("fail:", marks[marks < 60])

