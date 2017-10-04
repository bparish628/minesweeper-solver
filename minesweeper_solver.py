################################################################################
# Version 1
################################################################################

import tkinter
import functools

class Minesweeper(tkinter.Frame):

    @classmethod
    def main(cls, width, height):
        app = tkinter.Tk() # Create the GUI of the application
        app.resizable(False, False) # Don't allow the screen size to be changed.
        app.title('Minesweeper') # Title of the GUI
        window = cls(app, width, height) # invoke the classes init function
        app.mainloop() # Entry point for tkinter

    def __init__(self, master, width, height):
        super().__init__(master)
        self.__width = width
        self.__height = height
        self.__generate_board()
        self.grid()

    def __generate_board(self):
        self.__buttons = []
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                # Create each of the buttons of the grid
                button = tkinter.Button(self, text='', command=functools.partial(self.__on_click, x, y))
                button.grid(column=x, row=y)
                row.append(button)
            self.__buttons.append(row)

    def __on_click(self, x, y):
        print('Cords: ({},{})'.format(x, y))

if __name__ == '__main__':
    Minesweeper.main(9, 9)
