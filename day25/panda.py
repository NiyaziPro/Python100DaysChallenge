import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(round(average, 2))

print(data["temp"].mean())
print(data["temp"].min())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print((monday.temp * 1.8) + 32)

# Create a data frame from scratch
data_dict = {
    "students": ["Any", "Jack", "Mery"],
    "scores": [77, 55, 97]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_data.csv")
