#!/usr/bin/env python
# coding: utf-8

# In[3]:


import geopandas as gpd


# In[13]:


import os


# In[14]:


pwd


# In[23]:


gdf = gpd.read_file('Downloads/parcels_shp_dbf_Ocean/OceanCountyParcels.shp')


# In[24]:


gdf.head(n=5)


# In[29]:


gdf.dtypes


# In[33]:


gdf['MUN']=gdf['MUN'].astype(float)
gdf['BLOCK']=gdf['BLOCK'].astype(float)


# In[35]:


gdf_20 = gdf.head(n=20)
gdf_20.plot.bar(x='MUN', y='BLOCK', rot=0)


# In[ ]:




