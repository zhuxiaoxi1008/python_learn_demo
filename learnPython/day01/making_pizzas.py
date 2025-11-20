# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


def p(size, **t):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    print(t)

p(16,  location='princeton', field='physics')
    