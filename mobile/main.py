from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from camera_screen import CameraScreen


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=30
        )

        title = Label(
            text="Skin Screening",
            font_size=32,
            size_hint=(1, 0.25)
        )

        description = Label(
            text="Capture an image of a skin lesion\n"
                 "for screening analysis.",
            font_size=20,
            size_hint=(1, 0.30)
        )

        start_button = Button(
            text="START SCAN",
            font_size=22,
            size_hint=(1, 0.20)
        )

        start_button.bind(
            on_press=self.start_scan
        )

        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def start_scan(self, instance):

        self.manager.current = "camera"


class CameraScreenWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.camera_screen = CameraScreen()

        self.add_widget(
            self.camera_screen
        )


class SkinScreeningApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(name="home")
        )

        manager.add_widget(
            CameraScreenWrapper(name="camera")
        )

        return manager


if __name__ == "__main__":
    SkinScreeningApp().run()