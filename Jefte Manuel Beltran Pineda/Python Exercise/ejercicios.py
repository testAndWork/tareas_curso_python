# '\n'
file = 'Sesion12/lorem.txt'

with open(file) as f:
    lines = f.read().splitlines()
    print(lines)