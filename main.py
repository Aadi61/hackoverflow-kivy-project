from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget
Config.set('graphics','width','349')
Config.set('graphics','height','600')

class MainWindow(Screen):

    pass


class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class GridLayoutEx(GridLayout):
    pass
class MainWidget(Widget):
    pass
class TheLabApp(App):
    pass

class BoxLayoutEx(BoxLayout):
    pass
#kv= Builder.load_file("Hack.kv")

TheLabApp().run()


