def data_types():

    a = 10                     # int
    b = "Hello, World!"        # str
    c = 3.14                   # float
    d = True                   # bool
    e = [1, 2, 3]              # list
    f = {"key": "value"}       # dict
    g = (1, 2, 3)              # tuple
    h = {1, 2, 3}              # set

    types=[type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h)]

    # Способ с i.__name__
    types_str = str(types)
    type_names_replace = types_str.replace('<class ', '').replace('>', '').replace('\'', '').strip("[]")

    # Способ с .replace
    type_names = [i.__name__ for i in types]
    type_names_str = str(type_names).replace('\'', '').strip("[]")

    print("Способ с .replace \n", type_names_replace, '\n')
    print("Способ с i.__name__ \n", type_names_str)

if __name__ == '__main__':
    data_types()