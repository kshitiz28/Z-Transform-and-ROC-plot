#required imports
# from sympy import *
# from sympy import roots, solve_poly_system
# x=symbols('x')

#initialize empty list to store coefficients
a = []
b = []


#Function for cofficients calculation
def cofficients(q, name):
    if name == 'numerator':
        for i in range(q+1):
            a.append(int(input(f'input the {i}th cofficient of {name}')))
    elif name == 'denominator':
            for i in range(q+1):
                b.append(int(input(f'input the {i}th cofficient of {name}')))
    else:
        print('Input Error')


# Degree of polynomial for numerator and denominator
(n,m)=map(int, input('Degree of polynomial of numerator and denominator').split())


#cofficients of numerator and denominator
cofficients(n,'numerator')
cofficients(m,'denominator')





    