import json

#create a list containing the dictionaries in precipitation.json, and then one only including measurements with the station in question.
data = []
seattle = []

with open('precipitation.json', 'r') as file:
    data = json.load(file)
    for measurement in data: 
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seattle.append(measurement)

#split the date value and create a new 'month' entry in the dictionaries          
for point in seattle:
    split_date = point['date'].split("-")
    month = split_date[1]
    point['month'] = int(month)
    
    
for line in seattle:
    print(line)

#for each month, add all precipitation values
total_precip = [0] * 12 
month = 0
for i in range(12):
    month += 1
    for point in seattle:
        if point['month'] == month:
            total_precip[month - 1] += point['value']


print(total_precip)

with open('monthly_precip.json', 'w') as monthly_precip:
    json.dump(total_precip, monthly_precip, indent=4)