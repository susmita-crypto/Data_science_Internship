print("Sales File Parser")

file = open("sales.txt", "r")

sales = []

for line in file:
    sales.append(float(line.strip()))

file.close()

print("Sales values:", sales)
print("Number of sales:", len(sales))
print("Total sales:", sum(sales))
print("Average sales:", sum(sales) / len(sales))
print("Highest sale:", max(sales))
print("Lowest sale:", min(sales))