import json


 #Object is a list of dictionaries Individual entries
 #are individual measurments for different cities
with open('precipitation.json') as file:
    all_city_data = json.load(file)


#Create Empty list then assign Seattle data
#Will be list of dictionaries
seattle_data = []

for data_entry in all_city_data:
    if data_entry['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(data_entry)

#Converting dates in Seattle data to datetime format
#Return clone of seattle_data with 'date' split by 
#- into a list

for data_entry in seattle_data:
    data_entry ['date'] = data_entry['date'].split('-')

#Create a list of dictionaries of form {month:'m','PRCP':'sum'}
rainf_month ={} 

#Iterate through seattle_data, adding rainfall to month in 
#rainf_month

for indx, data_entry in enumerate(seattle_data):
    current_month = seattle_data[indx]['date'][1]
    if current_month in rainf_month:
        rainf_month[current_month] += seattle_data[indx]['value']
    else:
        rainf_month[current_month] = seattle_data[indx]['value']

#for month in rainf_month:
#    print(f'for the {month} month, the total rainfall was {rainf_month[month]}.')

with open('rain_fall_dict.json','w') as file:
    json.dump(rainf_month, file, indent=4, sort_keys=True)

#If I have time, I will add in code that can do the same thing as a list
#with if-else to select between the two