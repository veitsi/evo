def leaves(dictionary):
  for k, v in dictionary.items():
    if type(v) is not dict:
      print (k, v)
      dictionary[k]=None
    else:
      leaves(v)
  
# except KeyError:


p = {'meaning':42, 'meta': { 'author':'Doug','year':1970} }
print(p)
print (type(p) is dict)
leaves(p)
print(p)
