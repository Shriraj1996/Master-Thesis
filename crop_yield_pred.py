import pandas as pd
import copy
import numpy as N
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('E:/NEHA_PUNE/crop_yeald_prediction/Dataset/crop_yield.csv')
print(df)
#df.hist()
def get_unique(lst):
    res = N.array(lst)
    uels = N.unique(res)
    return uels
def get_area(lst1,lst2,item):
    total_area = 0.0
    for i in lst1:
        if (item == i):
            index = lst1.index(i)            
            total_area += float(lst2[index])
    return total_area
def make_plot(lst1,lst2,text):
    x = np.array(lst1)
    y = np.array(lst2)
    plt.title(text)
    plt.barh(x, y, height = 1.3)
    plt.show()
states = df['State_Name'].tolist()
districts = df['District_Name'].tolist()
cropyear = df['Crop_Year'].tolist()
seasons = df['Season'].tolist()
crops = df['Crop'].tolist()
areas = df['Area'].tolist()
production = df['production'].tolist()
# print(areas) 
unique_states = get_unique(states)
unique_districts = get_unique(districts)
unique_years = get_unique(cropyear)
unique_seasons = get_unique(seasons)
unique_crops = get_unique(crops)
unique_areas = get_unique(areas)
state_wide_areas = []
for state in unique_states:
    state_wide_areas.append(get_area(states,areas,state))
# print(state_wide_areas)
# print('---------------')
district_wide_areas = []
for district in unique_districts:
    district_wide_areas.append(get_area(districts,areas,district))    
# print(district_wide_areas)
make_plot(unique_states,state_wide_areas,"")
make_plot(unique_districts,district_wide_areas,"")
# print(len(cropyear))
# print(len(unique_states))
print(unique_states)
def statewise_croppred(states,crops,prodcutions,state_for_pred):
    crop_preds = []
    crop_values = []
    crop_values_temp = []
    top_five_crop_preds = []
    top_five_crop_values = []
    temp_pred = 0.0
    temp_crop = ""
    unique_crops = get_unique(crops)
    for state in states:
        if(state == state_for_pred):
            for crop in unique_crops:
                #top_five_crop_preds.append(crop) 
                for inner_crop in crops:                    
                    if(inner_crop == crop):
                        temp_crop = inner_crop
                        index = states.index(state)
                        temp_pred += float(prodcutions[index])                        
                crop_preds.append(temp_crop) 
                crop_values.append(temp_pred)    
        temp_pred = 0.0  
        temp_crop= "" 
        crop_values_temp = copy.copy(crop_values) 
        crop_values.sort(reverse = True)
        for value in crop_values_temp:
            index = crop_values.index(value) 
            top_five_crop_preds.append(crop_preds[index])
            top_five_crop_values.append(value)                
    return top_five_crop_preds[0:5],top_five_crop_values[0:5]

state_code = input("Enter state code between 1-27:")
print("country code is: " + state_code)
print(unique_states[int(state_code)-1])
state_topredict = unique_states[int(state_code)-1]
crops_preds , crops_values = statewise_croppred(states,crops,production,state_topredict)
# print(len(crops_preds))
# print(len(crops_values))
# print(crops_preds)
# print(crops_values)
make_plot(crops_preds,crops_values,"Crop yield predictios for the state: "+unique_states[int(state_code)-1])
print(unique_districts)
district_code = input("Enter District code between 1-307:")
district_topredict = unique_districts[int(district_code)-1]
print(district_topredict)
crops_preds , crops_values = statewise_croppred(districts,crops,production,district_topredict)
print(crops_preds)
print(crops_values)
make_plot(crops_preds,crops_values,"Crop yield predictios for the district: "+district_topredict)

