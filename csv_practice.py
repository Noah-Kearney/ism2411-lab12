import csv
from datetime import datetime

print("--- Exercise 2 ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



print("--- Exercise 3 ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"Header: {header}")

    for row in reader:
        print(row)



print("--- Exercise 4 ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")



print("--- Exercise 5 ---")

total_rows = 0
cleaned_rows = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_rows += 1

print(f"Rows written: {cleaned_rows}")
print(f"Original rows: {total_rows}")



print("--- Exercise 6 ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

# csv.reader accesses information using column positions.
# DictReader uses column names, which makes it easier to identify specific information.



print("--- Exercise 7 ---")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")



print("--- Exercise 8 ---")

timestamp = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated.")
