immutable_var = 1 , 2 , 'гласные' , 'согласные'
print(immutable_var)
#immutable_var [0] = 7
# print(immutable_var) #Нельзя изменять кортеж,в отличие от списка. Он остается не изменным
immutable_var = ([1 , 2] , "гласные","согласные")
immutable_var [0][1] = 7
print(immutable_var)