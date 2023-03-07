from pizza_order.pizza_order import PizzaOrder

obj = PizzaOrder()


def test_calculate_bill():
    size = "S"
    pepperoni = "N"
    extra_cheese = "N"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 15

    size = "S"
    pepperoni = "Y"
    extra_cheese = "Y"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 18

    size = "M"
    pepperoni = "N"
    extra_cheese = "N"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 20

    size = "M"
    pepperoni = "Y"
    extra_cheese = "Y"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 24

    size = "L"
    pepperoni = "N"
    extra_cheese = "N"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 25

    size = "L"
    pepperoni = "Y"
    extra_cheese = "N"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 28

    size = "L"
    pepperoni = "Y"
    extra_cheese = "Y"
    assert obj.calculate_bill(size, pepperoni, extra_cheese) == 29
