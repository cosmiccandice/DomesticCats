import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from alerce.core import Alerce
alerce = Alerce()

filename = input("Enter Name of YSE Query File: ")
RFC_prediction = pd.read_csv(filename)

print (RFC_prediction)

alerce_class,alerce_probability = [],[]
for i in range(0,len(RFC_prediction)):

    detections = alerce.query_probabilities(RFC_prediction['name'][i],format="pandas")
    
    detection_probability = detections['probability']
    max_probability_index = detection_probability.idxmax()
    
    highest_prob_class = detections['class_name'][max_probability_index]
    probability = detection_probability[max_probability_index]
    
    
    alerce_class.append(highest_prob_class)
    alerce_probability.append(probability)


RFC_prediction['Alerce Class'] = alerce_class
RFC_prediction['Alerce Probability'] = alerce_probability

RFC_prediction.to_csv(filename, sep=',',index=False)
print (RFC_prediction)
