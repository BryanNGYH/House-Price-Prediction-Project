import pickle
import json
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location, availability, total_sqft, balcony, rooms):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = availability
    x[1] = total_sqft
    x[2] = balcony
    x[3] = rooms
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model

    # load the columns of features used to predict
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[4:]

    # load the model
    with open("./artifacts/banglore_house_price_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    # get_location_names()
    # print(get_location_names())
    # print(get_estimated_price('1st Block Jayanagar',0,1235,2,4))
    # print(get_estimated_price('Vijayanagar',1000,2,2))