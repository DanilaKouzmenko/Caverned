from objects import pos, Map

def draw_matrix(matrix : Map, _pos : pos):
    using = matrix.map_slice(_pos - pos(5, 4), 11, 9)
    for y, row in enumerate(using.content):
        for x, elem in enumerate(row):
            if y == 4 and x == 5:
                print('@@', end='')
            elif elem == 1:
                print('██', end='')
            else:
                print('..', end='')
        print()