
def square(x):
    result = []
    for i in x:
        result.append(i * i)
    return result

def square_gen(x):
    for i in x:
        yield i * i

nums_lit = [1, 2, 3, 4, 5]
print(dir(nums_lit))
num = iter(nums_lit)
print(dir(num))
print(next(num))
print(list(num))
#list comprehension
square_comprahension = [x*x for x in nums_lit]
print(square_comprahension)

# generator expression
square_gen_expression = (x*x for x in nums_lit)
print(square_gen_expression)
print(next(square_gen_expression))


# print(square(nums_lit))
# square_nums = square_gen(nums_lit)
# print(square_nums)
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))