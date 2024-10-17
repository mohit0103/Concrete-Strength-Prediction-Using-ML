import numpy as np 
import pandas as pd
import pickle

# Loading the saved model
loaded_model = pickle.load(open('trainedModel.sav', 'rb'))

Cement = float(200)
Blast_Furnace = float(20)
Fly_Ash = float(40)
Water = float(230)
Superplasticizer = float(120)
Coarse_Aggregate = float(800)
Fine_Aggregate = float(400)
Age = float(28)

specific_features = np.array([Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age])
specific_features = specific_features.reshape(1, -1)
predicted_strength = loaded_model.predict(specific_features)

print(f"Predicted Concrete Strength: {predicted_strength[0]}")