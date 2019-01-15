#=============INSTRUCTIONS===============================#
#1 Rewrite your code so that it calculates all the above for each location
#(don't do this manually, but instead have Python read the station codes
#from the CSV).

#2 Calculate the relative precipitation over the whole year compared to the
#other stations_ident (i.e. what percentage of all the measured rain fell in Seat-
#tle?).
#==========================================================#


#~~~~~~~~Read Data~~~~~~~~~~~~~~~~~#
import json

#Open CSV and manually store as dict
with open('stations.csv') as file:
    stations_ident = {}
    next(file, None)
    for line in file:
        (location, state, station) = line.strip().split(',')
        stations_ident[location] = {
            'state' : state,
            'station' : station
        }

#>>>print(stations_indent)
#{'Cincinnati': {'state': 'OH', 'station': 'GHCND:USW00093814'}, 
#'Seattle': {'state': 'WA', 'station': 'GHCND:US1WAKG0038'}, 'Maui': {'state': 'HI', 'station': 'GHCND:USC00513317'}, 
# 'San Diego': {'state': 'CA', 'station': 'GHCND:US1CASD0032'}}

#Open Json, this is a list of dicts
with open('precipitation.json') as file:
   precipitation_all = json.load(file)


#~~~~~~~~~~~Part One Code~~~~~~~~~~~~~~~~~#
#Note, go through afterwards and rename variables
#properly

#Create Empty list then assign Seattle data
#Will be list of dictionaries

all_stations_rainf = {}

#Looping through all stations. 
#station in loop is location key for 
#stations_idents dict.
for station in stations_ident:
    
    #~~~~~Rainfall For Station~~~~~~~#
    station_data = []

    for data_entry in precipitation_all:
        if data_entry['station'] == stations_ident[station]['station']:
            station_data.append(data_entry)

    #Converting dates in Seattle data to datetime format
    #Return clone of station_data with 'date' split by 
    #- into a list

    for data_entry in station_data:
        data_entry ['date'] = data_entry['date'].split('-')

    #Create a list of dictionaries of form {month:'m','PRCP':'sum'}
    rainf_month ={} 

    #Iterate through station_data, adding rainfall to month in 
    #rainf_month

    for indx, data_entry in enumerate(station_data):
        current_month = station_data[indx]['date'][1]
        if current_month in rainf_month:
            rainf_month[current_month] += station_data[indx]['value']
        else:
            rainf_month[current_month] = station_data[indx]['value']

    #for month in rainf_month:
    #    print(f'for the {month} month, the total rainfall was {rainf_month[month]}.')

    #~~~~~~~Rain in a Month
    y_total_rainf = 0

    #iterate through rain fall dict, summing for year total
    for month in rainf_month:
        y_total_rainf +=  rainf_month[month]
    
    #~~~~~Rel Rain fall
    #Initialize rel rainfall dict
    rel_rainf = {}

    #Calculate percentage and add to dict
    for entry in rainf_month:
        rel_rainf[entry] = 100*rainf_month[entry]/y_total_rainf
        
    all_stations_rainf[station] = {
        'monthly rainfall': rainf_month,
        'total rainfall local': y_total_rainf,
        'rel monthly rainfall': rel_rainf
    }

    with open('rain_fall_' + station + '.json','w') as file:
        json.dump(rainf_month, file, indent=4, sort_keys=True)
    #~~~~~~~~~Rel Precipitation~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~Rel Rainfall All~~~~~~~~~~~~~~~~##

#Get total yearly rainfall for all stations
y_total_rain_all = 0

for station in  all_stations_rainf:
    y_total_rain_all += all_stations_rainf[station]['total rainfall local']
    print(y_total_rain_all)


for station in all_stations_rainf:
    local_rain = all_stations_rainf[station]['total rainfall local']
    all_stations_rainf[station]['rel rainfall all'] = 100*local_rain/y_total_rain_all

for station in all_stations_rainf:
    print(f'The reltive % rainfall at station {station} is {all_stations_rainf[station]["rel rainfall all"]}.')

with open('all_stations_processed.json','w') as file:
    json.dump(all_stations_rainf, file, indent=4, sort_keys=True)
