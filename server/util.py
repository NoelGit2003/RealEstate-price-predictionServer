import json
import pickle
import numpy as np

__locations = None
__data_colomns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_colomns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_colomns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
         
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def get_location_names():
    return __data_colomns

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_colomns
    global __locations
    global __model
    
    with open("./artifacts/columns.json", 'r') as f:
        __data_colomns = json.load(f)['data_columns']
        # __locations = [column for i, column in enumerate(__data_colomns) if i >= 3]
        __locations = __data_colomns #first 3 are sqft, bath and bhk are removed
    
    if __model is None:  
        with open("./artifacts/linear_re_estate_predict_model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")
    
    
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    