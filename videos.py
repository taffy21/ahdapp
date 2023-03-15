from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
from kivy.metrics import dp

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        box2 = BoxLayout(size_hint_y = 0.08)
        self.add_widget(Label(text="Advanced HIV Disease", size_hint_y=0.10))
        video = VideoPlayer(source='AHD_Session 1_Overview of Advanced HIV Disease.mp4', state="play", size_hint_y = 0.70)
        self.add_widget(video)
        self.add_widget(box2)
        box2.add_widget(Button(text="Return Home"))
        box2.add_widget(Button(text="Proceed to Quiz"))
class MyVideosApp(App):
    def build(self):
        mw = MyWidget()
        return mw


if __name__ == "__main__":
    MyVideosApp().run()
