def print_given(*args,**kwargs):
    for i in args:
        print(i,type(i))

    for name,value in sorted(kwargs.items()):
         print(name,value,type(kwargs[name]))


print_given()