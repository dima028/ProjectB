import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

def ProjectB(veh, ped, age, income, kid, youth):
    data = pd.read_csv("Downloads\\Data-Part1.csv") 
    data = data.dropna()

    data_trunc = data.loc[:,'Vehicle Traffic':'Percent of Youth']
    #data_trunc_array=data_trunc.values
        
    #data_trunc_TSNE = TSNE(n_components=2).fit_transform(data_trunc)
        
    data_k = KMeans(n_clusters=80, random_state=0).fit(data_trunc)
    
    num = data_k.predict([[veh, ped, age, income, kid, youth]])[0]
    
    data_labels = pd.DataFrame(data_k.labels_)
    
    data_total = pd.concat([data_labels, data], axis=1)
    
    is_val = data_total[0]==num
    data_total_fin = data_total[is_val]
    return (data_total_fin['Intersection'].values)
