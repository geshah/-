immutable_var='карандаш',11,22,'ручка',[2,2],False
print(immutable_var)
print(type(immutable_var))
#immutable_var[3]=15 # 'tuple' object does not support item assignment.Кортеж('tuple')-неизменяем

mutable_list=['карандаш',11,22,'ручка',[2,2],False]
print(mutable_list)
mutable_list[3]='тетрадь'
print(mutable_list)
mutable_list.append('ученик')
print(mutable_list)