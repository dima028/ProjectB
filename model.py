import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

data = pd.read_csv("Data-Part1.csv")
data = data.dropna()

data_trunc = data.loc[:,'Vehicle Traffic':'Percent of Youth']
#data_trunc_array=data_trunc.values
#data_trunc_TSNE = TSNE(n_components=2).fit_transform(data_trunc)

data_k = KMeans(n_clusters=80, random_state=0).fit(data_trunc)

def predict(inputs = [10000,1212,19,50850,0.130348259,5.3]):
    # inputs = [veh, ped, age, income, kid, youth]
    num = data_k.predict([inputs])[0]

    return num
