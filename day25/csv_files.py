with open("weather_data.csv") as data:
    contents = data.readlines()
    print(contents)
    data.close()

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    data_file.close()
