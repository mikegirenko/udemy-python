from pizza_order.pizza_order import PizzaOrder

obj = PizzaOrder()


def test_calculate_bill():
    assert obj.calculate_bill("S", "Y", "N") == 15


