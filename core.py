from CSP_assistant import *

targets = int(input("Enter number of Targets: "))
sensors = int(input("Enter number of Sensors: "))

matrix = []
row_list = []
for y in range(sensors):
    for x in range(targets):
        row_list.append("-1")
    matrix.append(row_list.copy())
    row_list.clear()

pretty_matrix(matrix)