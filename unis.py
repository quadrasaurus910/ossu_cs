# Showcase lists, mutability, object id, aliasing

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print('Univs =', Univs) 
print('Univs1 =', Univs1) 
print(Univs == Univs1)

print(Univs == Univs1) #test value equality 
print(id(Univs) == id(Univs1)) #test object equality 
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))
print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1])) 
print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))

Techs.append('RPI')

print('Univs =', Univs) 
print('Univs1 =', Univs1)