#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import moudles
from pyspark.sql import SparkSession
import pyspark.sql.functions as fn
from pyspark.sql.types import StringType,DoubleType,IntegerType


# In[2]:


# Set spark session
spark=SparkSession.builder.appName('data_processing').getOrCreate()


# In[3]:


spark.sparkContext.appName


# In[54]:


# Load data
df_A=spark.read.csv('./A_lvr_land_A.csv', inferSchema=True, header=True, encoding='UTF-8')
df_A.createOrReplaceTempView("df_ATable")


# In[55]:


df_A.printSchema()


# In[68]:


df_A.select(
    fn.col('主要用途'))\
.show(3)


# In[84]:


df_A.filter((df_A['主要用途']=='住家用')&(df_A['建物型態']=='住宅大樓(11層含以上有電梯)')&(df_A['總樓層數'] >= 13)).show()

