import pandas as pd
path=pd.read_excel("C:\\Users\\Admin\\Downloads\\student_marks.xlsx")
print(path)
df5=pd.DataFrame(path)
print(df5)
df5["total"] = df5["English"] + df5["Maths"]+df5["Science"]++df5["Social"]
print(df5)
#To drop the total Column
df5=df5.drop(columns=["total"])
print(df5)
print(df5[["Name","English"]])
#Handling Missing data
print(df5.dropna)
print(df5)
print(df5[["Name","English"]].dropna())
print(df5)

