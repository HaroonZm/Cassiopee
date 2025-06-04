while True:
    am = input().split()
    if am == ['0', '0']:
        break
    pm = input().split()
    stores = ['A', 'B', 'C', 'D', 'E']
    total_sales = {}
    # lire les 5 stores
    am_sales = [int(x) for x in am]
    pm_sales = [int(x) for x in pm]
    for i in range(5):
        total_sales[stores[i]] = am_sales[i] + pm_sales[i]
    for _ in range(4):
        am = input().split()
        pm = input().split()
        am_sales = [int(x) for x in am]
        pm_sales = [int(x) for x in pm]
        for i in range(5):
            total_sales[stores[i]] += am_sales[i] + pm_sales[i]
    # trouver le store avec le max
    max_store = max(total_sales, key=total_sales.get)
    print(max_store, total_sales[max_store])