import os
import sys

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    project_root
)

from kivy.app import App

from mobile.camera_screen import ResultScreen


class TestApp(App):

    def build(self):

        image_path = os.path.join(
            project_root,
            "mobile",
            "captured_skin.jpg"
        )

        return ResultScreen(
            image_path=image_path
        )


if __name__ == "__main__":
    TestApp().run()