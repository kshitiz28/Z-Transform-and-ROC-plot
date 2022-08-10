# required imports
import numpy as np
from plot_zplane import zplane

# initialize empty list to store coefficients
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

#Making numerator and denominator polynomial using coefficients
numerator_poly=np.poly1d(a[::-1]) #Have to reverse the list to arrange degree
denominator_poly = np.poly1d(b[::-1])

#Calculate poles and zeros
zeros=numerator_poly.r
poles=denominator_poly.r
print(zeros,poles)

#ploting poles and zeros
zplane(zeros,poles)