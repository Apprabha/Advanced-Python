import pandas as pd
import numpy as np
s1=pd.Series([1,2,3,4,5])
print(s1)
s2=pd.Series(["a","b","c","d","e"], index=[1,2,3,4,5])
print(s2)
l1 = ["a","b","c","d","e","f"]
s3=pd.Series(l1, index=np.arange(1,len(l1)+1))
print(s3)
