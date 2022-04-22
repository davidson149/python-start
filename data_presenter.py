cupcake = open('CupcakeInvoices.csv')

for rows in cupcake:
    print(rows)

for rows in cupcake:
    values = rows.split(',')
    print(values[2])

for rows in cupcake:
    values = rows.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

total = 0

for rows in cupcake:
    values = rows.split(',')
    total= total + (int(values[3]) * float(values[4]))
     
print(total)
    

cupcake.close()