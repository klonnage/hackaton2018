from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("quiz2.kv")

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()