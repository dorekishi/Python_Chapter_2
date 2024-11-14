import car

my_mustang = car.Car('ford','mustang',2024) # module_name.Class(attribute/s)
print(my_mustang.get_descriptive_name())    # .method()

my_leaf = car.ElectricCar('nissan','leaf', 2024)
print(my_leaf.get_descriptive_name())