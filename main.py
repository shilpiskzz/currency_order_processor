# main.py

from task_a_currency_conversion import parse_conversion_rates
from task_b_order_processing import parse_products, process_orders

if __name__ == "__main__":
    print("Script started ✅")

    # Input data
    conversion_rates = [
        "USD,EUR,0.9",
        "EUR,INR,88.5",
        "USD,JPY,110.0",
        "JPY,INR,0.65"
    ]

    products = [
        "productA,100,USD",
        "productB,85,EUR",
        "productC,5000,JPY"
    ]

    orders = [
        "productA,productB,INR",
        "productC,USD"
    ]

    # Task A: Build graph
    currency_graph = parse_conversion_rates(conversion_rates)

    # Task B: Process orders
    product_dict = parse_products(products)
    results = process_orders(orders, product_dict, currency_graph)

    # Output results
    for res in results:
        print(res)
