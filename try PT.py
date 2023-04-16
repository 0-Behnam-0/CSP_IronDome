from prettytable import PrettyTable

x = PrettyTable()
# x.header = False
x.field_names = ["1", "2", "3"]
x.add_row([1, 2, 3])
x.add_row([4, 5, 6])
x.add_row([7, 8, 9])

y = str(x)

y = y.replace('|', '¦')

print(y)
