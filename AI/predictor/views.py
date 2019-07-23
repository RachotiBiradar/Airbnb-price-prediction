import pandas as pd
import numpy as np

from scipy.spatial import distance
from django.http import HttpResponse
from django.shortcuts import render

from .models import Data

#dc_listings = pd.read_csv('data.csv')

def index(request):
    return render(request, 'predictor/index.html',context=None)

def predict(request):
    features = {'accommodates':0, 'bedrooms':0, 'bathrooms':0, 'beds':0, 'price':0, 'minimum_nights':0, 'maximum_nights':0, 'number_of_reviews':0}
    f1 = features['accommodates'] = int(request.POST['f1'])
    f2 = features['bedrooms'] = int(request.POST['f2'])
    f3 = features['bathrooms'] = int(request.POST['f3'])
    f4 = features['beds'] = int(request.POST['f4'])
    f5 = features['price'] = int(request.POST['f5'])
    f6 = features['minimum_nights'] = int(request.POST['f6'])
    f7 = features['maximum_nights'] = int(request.POST['f7'])
    f = [f1,f2,f3,f4,f5,f6,f7]
    dc_listings = pd.read_csv('predictor/data.csv')
    dc_listings['price'] = dc_listings.price.str.replace("\$|,",'').astype(float)
    #train_df = dc_listings.copy().iloc[:2792]
    #test_df = dc_listings.copy().iloc[2792:]
    train_df = dc_listings.copy().iloc[:]
    def predict_price_multivariate(new_listing_value,feature_columns):
        temp_df = train_df
        temp_df['distance'] = distance.cdist(temp_df[feature_columns],[new_listing_value[feature_columns]])
        temp_df = temp_df.sort_values('distance')
        knn_5 = temp_df.price.iloc[:5]
        predicted_price = knn_5.mean()
        return (predicted_price)
    cols = []
    d = {}
    for item in list(features.keys()):
        if features[item] != 0:
            d[item] = [int(features[item]),]
            cols.append(item)
    print(cols)
    print(d)
    df = pd.DataFrame(d)
    df['predicted_price'] = df[cols].apply(predict_price_multivariate, feature_columns=cols, axis=1)

    #return HttpResponse(df['predicted_price'])
    return render(request, 'predictor/result.html', context={'price':float(df['predicted_price'])})