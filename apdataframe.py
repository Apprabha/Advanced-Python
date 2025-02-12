import pandas as pd
dic1={"name":["ab","bc","cd"], "age":[30,31,32], "marks":[90,80,70]}
df=pd.DataFrame(dic1,index=["student1","student2","student3"])
print(df)
df2=pd.DataFrame()
print(df2)
df3=pd.DataFrame(columns=["name","age","marks"],index=["student1","student2","student3"])
print(df3)
df3["name"]=["ab","bc","cd"]
print(df3)
df3["age"]=[30,31,32]
print(df3)
df3["marks"]=[90,80,70]
print(df3)
df3=df3._append({"name": "newname","age":30,"marks":90}, ignore_index=True)
print(df3)
