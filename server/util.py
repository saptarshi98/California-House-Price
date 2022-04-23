import pickle
import pandas as pd
import numpy as np


global __model
with open("./server/artifacts/norm.pickle", 'rb') as fl:
    norm = pickle.load(fl)

cols = ['longitude',
 'latitude',
 'housing_median_age',
 'total_rooms',
 'total_bedrooms',
 'population',
 'households',
 'median_income',
 'total_rooms_per_house',
 'total_bedrooms_per_house',
 'population_per_house',
 'ocean_proximity_INLAND',
 'ocean_proximity_ISLAND',
 'ocean_proximity_NEAR BAY',
 'ocean_proximity_NEAR OCEAN']
def get_predicted_price(long, lat, age, room, bedroom, population, household, income, proximity):      
    X = [long, lat, age, room, bedroom, population, household, income, room/household, bedroom/household, population/household ]
    if proximity == "INLAND":
        X.extend([1,0,0,0])
    elif proximity == "ISLAND":
        X.extend([0,1,0,0])
    elif proximity == "NEAR BAY":
        X.extend([0,0,1,0])
    elif proximity == "NEAR OCEAN":
        X.extend([0,0,0,1])
    else:
        X.extend([0,0,0,0])
    X = np.array(X)
    X = pd.DataFrame(np.reshape(X, (1, len(X))), columns = cols)
    X  = norm.transform(X)
    with open("./server/artifacts/california_house_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    predicted_price = __model.predict(X)
    return predicted_price[0]



if __name__ == '__main__':
    
    print(get_predicted_price(-118.83, 34.14, 16, 1316, 194, 450, 173, 3.4698, "NEAR OCEAN"))
