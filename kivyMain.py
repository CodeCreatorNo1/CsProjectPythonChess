import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

kivy.require('2.1.0')

# Builder.load_file('Chess.kv')         # use only when kv is not found


class Wind(Widget):                  # Stands for window
    def __init__(self):
        super().__init__()


class ChessBoard(GridLayout):
    # white = ColorProperty([0.91, 0.92, 0.81, 1.0])
    # green = ColorProperty([119/256, 149/256, 86/256, 1.0])
    white = get_color_from_hex('e2e2ac')
    green = get_color_from_hex('5bea27')
    boardSize = 800
    @staticmethod
    def click(x=-1, y=-1):
        if x == -1 or y==-1:
            return
        print('I was clickd at {}, {}'.format(x, y))


class ChessApp(App):
    @staticmethod
    def setvar():
        colr = get_color_from_hex('9a9aa0')
        Window.clearcolor = colr
        Window.size = (1000, 800)
    def build(self):
        self.title = 'CHESS'
        self.icon = 'img\\bn.png'
        self.setvar()
        return Wind()


if __name__ == '__main__':
    ChessApp().run()
