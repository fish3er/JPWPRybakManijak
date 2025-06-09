import random
import time

import psutil
import os

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 ** 2  # RSS in MB
    return round(mem, 8)

brand_list  = ['Audi', 'BMW', 'Mercedes', 'Volkswagen', 'Porsche', 'Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']

print('Memory before: {} MB'.format(memory_usage_psutil()))

def random_cars(n):
    result = []
    for i in range(n):
        car = {
            'id': i,
            'Model': random.choice(brand_list),
            'Year': random.randint(2000, 2023),
            'Price': random.randint(30000, 200000)

        }
        result.append(car)
    return result

def random_cars_gen(n):
    for i in range(n):
        car = {
            'id': i,
            'Model': random.choice(brand_list),
            'Year': random.randint(2000, 2023),
            'Price': random.randint(30000, 200000)
        }
        yield car


numbers_of_cars = int(10e3)
t1= time.perf_counter()
cars = random_cars_gen(numbers_of_cars)
# cars = list(random_cars_gen(numbers_of_cars))
t2 = time.perf_counter()
print("Generartor function")
print('Memory after: {} MB'.format(memory_usage_psutil()))
print('Time elapsed: {} seconds'.format(t2-t1))

t1= time.perf_counter()
cars2 = random_cars(numbers_of_cars)
t2 = time.perf_counter()
print("'Standard' function")
print('Memory after: {} MB'.format(memory_usage_psutil()))
print('Time elapsed: {} seconds'.format(t2-t1))