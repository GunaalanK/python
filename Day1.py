i=10
print(i)
ii=int(1.2)
print(ii)
f=1.4
print(f)
result=i*f
print(result)
ii=i-f
print(result)
s='my string'
ss='my other string'
print(s,ss)
s='backlash \\'
print(s)
s='Bob\'s cat'
print(s)
s="Bob's cat and Alice's dog"
print(s)
s='''my string' " '''
s='My name is \n Gunaalan'#\n bring in to new line
print(s)

name= 'Gunaalan'
complete_name = 'My name is %s' % name
print(complete_name)
complete_name = 'My name is {}'.format (name)
print(complete_name)
complete_name = f'My name is {name}' # modern string with f
print(complete_name)
name = 'Gunaalan'
surname = 'Kuddithamby'
age =30
information = f'''My complete name is {name} {surname} and I'm {age}''' # I\'m also could be used
print(information)

mybool = True
mybool2 = False

print(mybool, mybool2)
i= 1
print(str(i))
s = '1'
conv = int(s) # convert the string in to integer
s = 't'
print(bool(s)) # convert string into bool

i = 10
ii = 3
print(i/ii)
print(i%ii) #remains one 1

#list
l = [1,2,3,4,5]
print(type(l))
print(l)

ll = [1, 'A', 1.2,  True]
print(ll)

print(l == ll) # why double equal

print(l!=ll) # [!=] [~=] [==]

l1 = [1,2,3,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
print(l1)
s1=set(l1) # remove the repition
print(s1)
print(type(s1))

lclean = list(s1)
print(lclean)
print(type(lclean)) # convert set in to list

l1[0]
print(l1[0])

l1[0] ='A'
print(l1[-1])
print(l1[0:3])
#print(l1, len(l1))

l= [1,2,3,4,5,6,7,8,9,10]
print(l[0])
print(l[-1])
print(l[0:3])
#print(l[:-2])

l1=[1,2,3]
l2=[4,5,6,7,8]
lt=l1+l2
print(lt)
ltt=lt*4
#print(ltt)

lm=[l1,l2]
print(lm)
#print(lm[0][1])

#tuple
t =(1,2,3)
print(t)
#print(type(t))

# dictionary

d = {'name': 'Gunaalan', 'age' :30} # name, age  are the key
print(d)
d['name'] = 'Gunaalan'
#print(d['name'])

d= {'names': ['John', 'Roi','Gun']}
#print(d)











