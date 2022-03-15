#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pyspark.sql import SparkSession
from functools import reduce
from pyspark.sql import DataFrame

spark = SparkSession.builder.appName('data_processing').getOrCreate()

#讀取檔案
df_A = spark.read.csv('A_lvr_land_A.csv', header=True)
df_B = spark.read.csv('B_lvr_land_A.csv', header=True)
df_E = spark.read.csv('E_lvr_land_A.csv', header=True)
df_F = spark.read.csv('F_lvr_land_A.csv', header=True)
df_H = spark.read.csv('H_lvr_land_A.csv', header=True)

#合併檔案
dfs = [df_A, df_B, df_E, df_F, df_H]
df_complete = reduce(DataFrame.unionAll, dfs)
df_complete.show()

#篩選資料
df_result = df_complete.filter(
                               (df_complete['主要用途']=='住家用')&
                               (df_A['建物型態']=='住宅大樓(11層含以上有電梯)')
                              )

#存成json檔
df_result.to_json(path = "df_results.json")

