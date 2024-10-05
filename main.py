def common_products_in_all_shops(shops):
    if len(shops) > 0:
        common_products = shops[0]

        for shop_products in shops[1:]:
            common_products = common_products.intersection(shop_products)

        if common_products:
            print("Товари, що є у всіх магазинах:", common_products)
        else:
            print("Спільних товарів немає, результат порожня множина.")
    else:
        print("Список магазинів порожній.")


n = int(input("Введіть кількість товарів у наборі: "))
products = input(f"Введіть {n} товарів через пробіл: ").split()

m = int(input("Введіть кількість магазинів: "))
shops = []

for i in range(m):
    shop_products = set(input(f"Введіть асортимент товарів магазину {i + 1} через пробіл: ").split())
    shops.append(shop_products)

common_products_in_all_shops(shops)
