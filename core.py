from CSP_assistant import *


matrix = []

t_cnt = 0
target = True
target_list = []
while target:
    t_cnt += 1
    target = input("["+ str(t_cnt) +"] Enter target(leave blank to exit): ")
    target_list.append(target)
target_list.pop(-1)
matrix.append(target_list)

s_cnt = 0
sensor = True
sensor_list = []
while sensor:
    s_cnt += 1
    sensor = input("["+ str(s_cnt) +"] Enter sensor(leave blank to exit): ")
    sensor_list.append(sensor)
sensor_list.pop(-1)

t_cnt = t_cnt - 1
sensor_list = [sensor_list[i:i + t_cnt] for i in range(0, len(sensor_list), t_cnt)]
for list in sensor_list:
    matrix.append(list)

pretty_matrix(matrix)