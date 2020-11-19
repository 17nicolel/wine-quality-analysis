# YunXuan Liao
# ITP 449 Fall 2020
# HW7
# Q1

import pandas as pd
import os

#1. Read the dataset into a dataframe. Be sure to import the header. (2)
winedata=pd.read_csv('wineQualityReds(1).csv',header=0)

#2. Drop Wine from the dataframe. (1)
winedata.drop(['Wine'],axis=1,inplace=True)

#3. print(winedata.head())
print(winedata.head())

#4. Drop Quality from dataframe. (1)
quality=winedata['quality']
winedata.drop(['quality'],axis=1,inplace=True)

#5. Print the dataframe and Quality. (1)
print(winedata.head())
print(quality)

#6. Normalize all columns of the dataframe. Use the Normalizer class from sklearn.preprocessing.
from sklearn.preprocessing import Normalizer
mynormalizer=Normalizer()
winedatanorm=pd.DataFrame(mynormalizer.transform(winedata),columns=winedata.columns)

#7. Print the normalized dataframe. (1)
print(winedatanorm)

#8. Create a range of k values from 1:11 for k-means clustering. Iterate on the k values and store the
#inertia for each clustering in a list. (2)
from sklearn.cluster import KMeans
ks=range(1,11)
inertia=[]
for k in ks:
    model=KMeans(n_clusters=k)
    model.fit(winedatanorm)
    inertia.append(model.inertia_)

#9. Plot the chart of inertia vs number of clusters. (2)
import matplotlib.pyplot as plt
plt.plot(ks,inertia,'-o')
plt.xlabel('# of clusters (k)')
plt.ylabel('Inertia')
plt.xticks(ks)
plt.show()

#10. What K (number of clusters) would you pick for k-means? (1)
#I pick 6.

#11. Now cluster the wines into K clusters. Use random_state = 2020 when you instantiate the kmeans model.
#Assign the respective cluster number to each wine. Print the dataframe showing the cluster number for each wine. (2)
model=KMeans(n_clusters=6,random_state=2020)
model.fit(winedatanorm)
print(model.labels_)
winedatanorm['Clusters']=pd.Series(model.labels_)
print(winedatanorm)

#12. Add the quality back to the dataframe. (1)
winedatanormquality=pd.concat([winedatanorm,quality],axis=1)
print(winedatanormquality)

#13. Now print a crosstab (from Pandas) of cluster number vs quality. Comment if the clusters
#represent the quality of wine. (3)
print(pd.crosstab(winedatanormquality['quality'],winedatanormquality['Clusters']))
print(pd.crosstab(winedatanormquality['quality'],winedatanormquality['Clusters'],normalize='columns'))
#the clusters do not represent the quality of wine because for each cluster there is no obvious dominant number of a different quality.
#Most of the clusters are all focused on quality 6.
