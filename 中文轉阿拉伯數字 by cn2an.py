#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import cn2an     
         
dfA = pd.read_csv('./A_lvr_land_A.csv').drop(0, axis = 0)
dfB = pd.read_csv('./B_lvr_land_A.csv').drop(0, axis = 0)
dfE = pd.read_csv('./E_lvr_land_A.csv').drop(0, axis = 0)

df = pd.concat([dfA, dfB, dfE], axis = 0, ignore_index = True)

#選取需要的欄位
x = df.iloc[:,10].fillna(0)

y = []
#將“層”字去除
for i in x:    
    if i == 0:
        y.append(0)        
    else:
        y.append(i[:-1])

z = []
#將中文轉為阿拉伯數字
for s in y:
    if s == 0:
        z.append(0)        
    else:
        z.append(cn2an.cn2an(s))
        
#轉DataFrame
s = pd.DataFrame(z, columns=['總樓層數'])  

#合併DataFrame
result = pd.concat([s, df.iloc[:,[0,11]]], axis = 1)

#存檔
result.to_json('results.json', orient = "records")

