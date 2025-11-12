add funcao giovanni(par1, par2);

add fuction Predo
def calculate_bill(pizza_size, toppings, drink=None):
    prices = {
        "small": 20,
        "medium": 30,
        "large": 40,
        "topping": 3,
        "drink": 8
    }

    total = prices[pizza_size] + prices["topping"] * len(toppings)
    if drink:
        total += prices["drink"]
        print(f"🧾 Order: {pizza_size} pizza with {', '.join(toppings)} and a {drink}")
    else:
        print(f"🧾 Order: {pizza_size} pizza with {', '.join(toppings)}")

    print(f"💰 Total: R${total},00")

# Exemplo de uso
calculate_bill("medium", ["bacon", "onion", "olives"], drink="guaraná")