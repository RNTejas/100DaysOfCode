import pandas

data = pandas.read_csv('weather_data.csv')
# getting a COLUMN
temparatures = data['temp']
print(data)
print(temparatures)


data_dict = data.to_dict()      # converting DataFrame to dict
print(data_dict)

# pythonic way
temp_list = data['temp'].to_list()    # converting Series to list 
print(sum(temp_list) / len(temp_list))  # avarage

# Pandas way
print(data['temp'].mean())  # avarage
print(data['temp'].max())   # getting the max


# data['temp']  OR data.temp       both are same

# getting a ROW
row = data[data.day == 'Monday']
row = data[data.temp == data['temp'].max()]
print(row)


# if you have a python dictionary you can execute that in Pandas and create CSV
example_dict = {
    'name': ['Tejas', 'Andy', 'Angela', 'Jonas'],
    'scores': [67, 89, 98, 99]
}

data_csv = pandas.DataFrame(example_dict)
print(data_csv)
data_csv.to_csv('data.csv')
