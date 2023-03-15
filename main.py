from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.clock import Clock


class WindowManager(ScreenManager):
    pass


class Loading(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.switch_screen, 3)

    def switch_screen(self, dt):
        self.manager.current = "login"

class Login(Screen):
    pass

class Register(Screen):
    pass
class Contents(Screen):
    pass


class Completed(Screen):
    pass



class AdvancedHIVApp(App):
    print(WindowManager.current)





if __name__ == "__main__":
    AdvancedHIVApp().run()