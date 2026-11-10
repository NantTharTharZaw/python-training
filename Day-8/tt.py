import pandas as pd

print(pd.__version__)

# Series

import pandas as pd

marks = pd.Series(
    [40, 65, 80, 90], index=["aye", "su", "ne", "thar"], name="python_marks"
)

print(marks)
print(marks.iloc[1])
print(marks.loc["aye"])
print(marks.loc[["aye", "su"]])
print(marks >= 80)
print(marks[marks >= 80])
print(marks.mean())
print(marks.max())
print(marks.min())

print(marks.sort_values())
print(marks.sort_values(ascending=False))


# Data frame

students = pd.DataFrame({"name": ["aye", "su", "thar"], "marks": [30, 30, 40]})

print(students)
print(students.shape)
print(students["name"])
print(students[["name","marks"]])
print(students.loc[0,"marks"])
print(type(students))
print(type(students).__name__)

one_column = students["marks"]
one_column_table = students[["marks"]]

print(type(one_column.shape).__name__)
print(type(one_column_table.shape).__name__)
print(one_column.shape)
print(one_column_table.shape)

