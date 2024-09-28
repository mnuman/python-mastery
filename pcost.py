def portfolio_cost(fname: str) -> float:
    with open(fname) as portfolio:
        total = 0
        for line in portfolio:
            fields = line.split()
            try:
                qty = int(fields[1])
                price = float(fields[2])
                total += qty * price
            except ValueError as ve:
                print(f"Couldn't parse {line}")
                print(ve)
    return total


print(portfolio_cost("Data/portfolio3.dat"))
