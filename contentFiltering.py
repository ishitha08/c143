from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('final2.csv')
df = df[df['soup'].notna()]

count = CountVectorizer(stop_words='english')
count_metrics = count.fit_transform(df['soup'])
cosine_sim = cosine_similarity(count_metrics,count_metrics)
df = df.reset_index()
indices = pd.Series(df.index,index = df['title'])

def getRecommendation(title):
    idx = indices[title]
    simscores = list(enumerate(cosine_sim[idx]))
    simscores = sorted(simscores,key = lambda x:x[1],reverse=True)
    simscores = simscores[1:11]
    movie_indices = [i[0]for i in simscores]
    return df[['title','poster_link','release_date','runtime','vote_average','overview']].iloc[movie_indices].values.tolist()
