dict1 ={'a':1,'b':2,'v':22}
try:
    x= dict1['n']
except LookupError:
    print("查询错误")
except KeyError:
    print('键错误')
else:
    print(x)