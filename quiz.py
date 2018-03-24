from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            source: 'images.jpeg'
            pos: self.pos
            size: self.size
        FloatLayout:
            Button:
                size_hint: None, None
                text: 'Start'
                pos:100, 75
                width: '250sp'
                font_size: '40sp'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'game'
            Button:
                size_hint: None, None
                pos:450, 75
                width: '250sp'
                font_size: '40sp'
                text: 'Quit'
                on_press: root.dismiss()

<SettingsScreen>:
    FloatLayout:  
        Button:
            size_hint: None, None
            text: 'Back to menu'
            pos:520, 475
            width: '250sp'
            font_size: '20sp'
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'

""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='game'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()