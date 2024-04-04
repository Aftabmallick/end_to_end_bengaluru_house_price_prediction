import json
import pickle
import os
import numpy as np
__locations = None
__data_columns = None
__model = None
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_indes = -1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    z=round(__model.predict([x])[0],2)
    #print(z)
    return z

def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  

    global __model
    if __model is None:
        with open("server/artifacts/bengaluru_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))