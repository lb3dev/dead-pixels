import tkinter
from collections import deque

colors = deque(['black', 'white', 'red', 'green', 'blue'])


def navigate_right(root):
    colors.rotate(-1)
    root.configure(background=colors[0])


def navigate_left(root):
    colors.rotate(1)
    root.configure(background=colors[0])


if __name__ == '__main__':
    root = tkinter.Tk()

    root.attributes('-fullscreen', True)
    root.configure(background=colors[0])

    # A and Left Arrow keys to navigate left
    root.bind('a', lambda x: navigate_left(root))
    root.bind('<Left>', lambda x: navigate_left(root))

    # D, Right Arrow, and Left Click to navigate right
    root.bind('d', lambda x: navigate_right(root))
    root.bind('<Right>', lambda x: navigate_right(root))
    root.bind('<Button-1>', lambda x: navigate_right(root))

    # Right Click and Escape to exit
    root.bind('<Button-3>', lambda x: root.destroy())
    root.bind('<Escape>', lambda x: root.destroy())

    root.mainloop()
