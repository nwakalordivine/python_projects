import pandas
#
# data = pandas.read_csv("weather-data.csv")
# # data_list = data.temp.max()
# # print(data_list)
# # average = sum(data_list)/len(data_list)
# # print(round(average, 2))
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# F = (monday_temp * 9/5) + 32
# print(F)


s_data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray = len(s_data[s_data["Primary Fur Color"] == "Gray"])
cinnamon = len(s_data[s_data["Primary Fur Color"] == "Cinnamon"])
black = len(s_data[s_data["Primary Fur Color"] == "Black"])


dict_color = {
    "fur color": ["Grey", "Cinnamon",  "Black"],
    "count": [gray, cinnamon, black]
}

reformed_data = pandas.DataFrame(dict_color)
reformed_data.to_csv("squirrel_count.csv")
