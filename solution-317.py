from enum import Enum

class Orientation(Enum):
    BOTTOM_LEFT     = 1
    TOP_LEFT        = 2
    TOP_RIGHT       = 3
    BOTTOM_RIGHT    = 4

    def is_right(self):
        return self == Orientation.TOP_RIGHT or self == Orientation.BOTTOM_RIGHT

def show_triangle(size, orientation):

    if orientation == Orientation.TOP_RIGHT or orientation == Orientation.BOTTOM_LEFT:
        height_range = reversed(range(0, size))
    else:
        height_range = range(0, size)

    for h in height_range:
        for w in range(0, size):
            if (orientation.is_right() and w + 1 >= size - h) or (not orientation.is_right() and w + 1 <= size - h):
                print('*', end='')
            elif orientation.is_right():
                print(' ', end='')
        print('\n', end='')

show_triangle(10, Orientation.BOTTOM_LEFT)
print('\n', end='')
show_triangle(10, Orientation.TOP_LEFT)
print('\n', end='')
show_triangle(10, Orientation.TOP_RIGHT)
print('\n', end='')
show_triangle(10, Orientation.BOTTOM_RIGHT)