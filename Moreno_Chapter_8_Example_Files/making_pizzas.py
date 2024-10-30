import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    # module_name.function_name()

    # for specific functions
    # from module_name import function_name
        # for multiple functions
        # from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    # GIVING ALIAS TO FUNCTIONS ?!?

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

    # to import ALL functions in a module

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    # don't put spaces if a parameter uses a default value
    # def function_name(parameter_0, parameter_1='default value')
    #                                          ^^^
    # same should be used when calling a function

