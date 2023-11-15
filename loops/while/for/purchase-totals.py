def purchases_100(sales):
    total = 0
    customers_over = 0
    for customer in sales:
        total = sum(customer)
        print('Sum of customer at index: ' + str(sales.index(customer)) + ' is ' + str(total))
        if total >= 100:
            customers_over += 1
    return customers_over

sales = [[2.75], [50.0, 50.0], [150.46, 200.12, 111.30]]
print('Customer\'s with purchase total of $100 or more: ' + str(purchases_100(sales)))
