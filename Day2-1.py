# r=range(1, 100)
# #print(r)

# l=list(r)
# #print(l)
# r=range(1, 100, 2)
# print(r)
# l=list(r)
# #print(l)

#d={'a' : [1,2,3,.....50], 'b': [1,2,3.....20]}
#if the key is 'a' print values > 25 if not print(no values)
#if the key is 'b' print values < 10 if not dont do anything

a=range(1,51)
#print(a)
l1=list(a)
#print(l1)
b=range(1,21)
#print(b)
l2=list(b)
#print(l2)
d=(l1,l2)

# ra= list(range(1,50))
# rb= list(range(1,20))
# d={'a' : ra, 'b' : rb}
# d={'a': list(range(1,50)), 'b': list(range(1,20))}
# print(d)
# for k,v in d.items():
#     if k=='a':
#         for i in v:
#             if i>25:
#                 print(i)
#             else:
#                 print('no values')
#     if k== 'b':
#         for i in v:
#             if i<10:
#                 print(i)

# print(d['a'])
# l=[]

# for i in d['a']:
#     if i>25:
#         l.append(i)

# print(l)

# print(d['a'])


# for i in d['a']:
#     l=[]
#     if i>25:
#         l.append(i)

# print(l)


# FUNCTIONS

def my_function():
    '''
    This function prints something
    This function does not need parameters
    '''
    print('Hi Python')
#my_function()

#print(help(my_function))

# def my_function2(s):
#     print(s)

# my_function2('Roiter')

# name='Roiter'
# def my_function3(name, age=30):
#     print(name, age)

# my_function3(name)


# name='Roiter'
# def my_function3(name='Roiter', age=30):
#     print(name, age)

# my_function3(name)


def multiply(x,y):
    result=(x*y)
    print(result)
# multiply(10,35)

l=[10,2,3,50]

#multiply(l[0],l[2]) # if I add only l then type error b-s there should be 2 nums to multiply

# def multiply2(*args):
#     v=1
#     for i in args:
#         v= v * i
#     print(v)

# multiply2(1,30,90,4,3)
# multiply2(*l)
# multiply2(l) # Check this

# def multiply2(*args):
#     v=1
#     for i in args:
#         v= v * i
#     return v
# mynumber=multiply2(*l)
# print(mynumber)




def rect_area(width,height):
    calculation= width*height

    return calculation

my_area= rect_area (100,40)
print(my_area)



def shape_area(shape,width,height):

    if shape == 'rectangle':

        calculation = width * height
        

    if shape == 'triangle' :

        calculation= width + height / 2

    else:
        print('I do not know the shape')

    return calculation

area = shape_area('triangle', 100,5)


# faherenheit=(celsius*9/5)+32

def faherenheit(celsius):
    calculation= (celsius*9/5)+32
    return calculation

conversion=faherenheit(0)
print(conversion)



lc=[10,0,100,50]
def faherenheit2(*args):

    lf=[]
    
    for c in args:
        calculation = (c*9/5) + 32
        lf.append(calculation)

    return lf

my_f =faherenheit2(10,0,100,30)
print(my_f)
my_f2=faherenheit2(*lc)
print(my_f2)

    







