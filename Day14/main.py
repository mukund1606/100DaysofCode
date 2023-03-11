# with open("weather_data.csv") as data_file:
#     print(data_file.readlines())


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp = data["temp"]
# temp_list = temp.to_list()
# print(temp_list)
# avg = sum(temp_list) / len(temp_list)
# print(f"Average is {avg}")
# print(f"Average is {temp.mean()}")
# print(f"Max is {temp.max()}")


# Get data in col

# print(data["condition"])
# print(data.condition)


# Get data in row
# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print((monday.temp * 9 / 5) + 32)


# Create a dataframe from scartch

data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
