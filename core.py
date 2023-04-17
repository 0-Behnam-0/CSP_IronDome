from CSP_assistant import *

targets = int(input("Enter number of Targets: "))
sensors = int(input("Enter number of Sensors: "))

matrix = []
row_list = []
for i in range(sensors):
    for j in range(targets):
        row_list.append("0")
    matrix.append(row_list.copy())
    row_list.clear()


pretty_matrix(matrix)