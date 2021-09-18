import  os

print("Datei: %s" % __file__)
def f(*args,**kwarg):
    """
    EINFACH NUR EIN TEXT!!!
    :param args: steck was rein :o
    :return: Gibt zurück was du reinsteckst :) ;)

    """
    d = f
    print(kwarg['b'])
    # /print(args[2])
    return kwarg
print(f.__doc__)
# obj = {"name":'rudolf','age':88,'flist':{'name':'peter','age':77}}
obj = {'b':10, 'c':'lee','flist':[{'name':'peter','age':88},{'name':'ralf','age':99}]}
print(f)
li = [1,2,3]
print(f(li,**obj))

def mysum(*args,**kwargs):
    s = sum(list(args))
    return s
def callFunction(fun,*normalargs,**keyvargs):
    return fun(*normalargs,**keyvargs)
print( callFunction(mysum,1,2,3,4) )
print( callFunction(f,1,2,3,4,**obj))

# for key in obj:
#     print(key,obj[key])

