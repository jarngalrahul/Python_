# '*args'
###############################################
# these type of args are also called as unilmited positional arguements
# Thus, '*' operator allows us to provide any number of arguements to the function
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# '**kwargs' - Many Keyworded Arguements
###########################################


def calculate(n, **kwargs):
    print(kwargs)  # This basically prints a dictionary
    print(n+kwargs['add'])
    print(n*kwargs['multiply'])


calculate(12, add=3, multiply=10)


# Making a class using **kwargs
#####################################
class Car:
    def __init__(self, **kwargs):
        # kwargs['name'] use .get method because if the key is not present it returns none
        self.name = kwargs.get('name')
        self.color = kwargs.get('color')
        self.model = kwargs.get('model')


car = Car(name="Nissan", model="GT-R")
print(car.color)  # None
print(car.name)
print(car.model)
