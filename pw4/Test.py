import numpy as np

dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype)       # create a structured array

if __name__ == '__main__':
    print(values)
    b = []
    for elements in a:
        # elements[0].decode('UTF-8')
        # print(type(elements[0]))
        # print(type(elements[0].decode()))
        new_entity = (elements[0].decode(), elements[1], elements[2])
        b.append(new_entity)
    print(a)
    print(b)
    # print(b'somestring'.decode('UTF-8'))
    # print(type(b'somestring'))
    # print(type(b'somestring'.decode('UTF-8')))