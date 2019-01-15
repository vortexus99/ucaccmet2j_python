import json

#Open file
with open('rain_fall_dict.json') as file:
    rain_fall_dict = json.load(file)

#initialize total rainfall variable
y_total_rainf = 0

#iterate through rain fall dict, summing for year total
for month in rain_fall_dict:
    y_total_rainf +=  rain_fall_dict[month]

print(f'The yearly total rainfall is {y_total_rainf}.')

#Initialize rel rainfall dict
rel_rainf = {}

#Calculate percentage and add to dict
for entry in rain_fall_dict:
    rel_rainf[entry] = 100*rain_fall_dict[entry]/y_total_rainf
    print(f'The percentage of yearly rainfall in month {entry} is {rel_rainf[entry]}.')



