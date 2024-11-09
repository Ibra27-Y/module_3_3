def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(5, 'три', False)
print_params(c= 7)
print_params(a='один', b='три')


print('-----------------------------------')

print_params(b = 25)
print_params(c = [1,2,3])

print('-----------------------------------')

values_list = [True, 27, 'один']
values_dict = {'a': True, 'b': 12, 'c': 'Привет'}
print_params(*values_list)
print_params(**values_dict)

print('-----------------------------------')

values_list_2 = ['Элемент', 30]
print_params(*values_list_2, 42)