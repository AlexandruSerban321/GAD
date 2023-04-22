# Ex1

# def your_function(*args, **kwargs):
#     kwargs.clear()
#     n = 0
#     for i in args:
#         if type(i) == int:
#             n += i
#     return n
#
#
# print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
# print(your_function())
# print(your_function(2, 4, 'abc', param_1=2))


# Ex2

# def suma(lst):
#     if len(lst) == 0:
#         return [0, 0, 0]
#     else:
#         [suma_totala, suma_pare, suma_impare] = suma(lst[1:])
#         if lst[0] % 2 == 0:
#             return [suma_totala + lst[0], suma_pare + lst[0], suma_impare]
#         else:
#             return [suma_totala + lst[0], suma_pare, suma_impare + lst[0]]
#
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(suma(lista))


# Ex3

# def citire(nr):
#     try:
#         return int(nr)
#     except ValueError:
#         print(ValueError)
#         return 0
#
#
# print("Introduceti un numar:")
# print("Numarul tau este : " + str(citire(input())))
