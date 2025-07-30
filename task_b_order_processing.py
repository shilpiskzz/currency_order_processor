# task_b_order_processing.py

def parse_products(product_list):
    products = {}
    for p in product_list:
        name, price, currency = p.strip().split(',')
        products[name] = (float(price), currency)
    return products

def process_orders(orders, products, currency_graph):
    results = []
    for idx, order in enumerate(orders, 1):
        *items, target_currency = order.strip().split(',')
        total = 0.0
        for item in items:
            if item not in products:
                raise ValueError(f"Unknown product: {item}")
            price, curr = products[item]
            rate = currency_graph.convert(curr, target_currency)
            if rate is None:
                raise ValueError(f"No conversion path from {curr} to {target_currency}")
            total += price * rate
        results.append(f"Order {idx}: {round(total, 2)} {target_currency}")
    return results
