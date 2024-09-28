with open("Data/portfolio.dat") as portfolio:
    total = 0
    for line in portfolio:
        stock, qty, price = line.split()
        total += int(qty) * float(price)
print(f"Total portfolio cost {total}")
