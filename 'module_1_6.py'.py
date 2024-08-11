my_dict={'denis':1997,'masha':1991}
print(my_dict)
print(my_dict['masha'])
print(my_dict.get('katya'))
my_dict.update({'ignat':2011,'baba':1982})
b_a=my_dict.pop('baba')
print(b_a)
print(my_dict)

my_set=22,'game',2.1,22,'head',35,'game'
my_set=set(my_set)
print(my_set)
my_set.update({'fool',4.2})
my_set.remove('fool')
print(my_set)