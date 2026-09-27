import requests

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.metrics import dp


class ResultScreen(BoxLayout):

    def __init__(self, image_path, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(20),
            **kwargs
        )

        self.image_path = image_path

        # Title
        self.title = Label(
            text="SCAN RESULT",
            font_size="26sp",
            size_hint_y=None,
            height=dp(50)
        )

        self.add_widget(self.title)

        # Captured image
        self.image = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=True
        )

        self.add_widget(self.image)

        # Result
        self.result_label = Label(
            text="Analyzing image...",
            font_size="20sp",
            size_hint_y=None,
            height=dp(50)
        )

        self.add_widget(self.result_label)

        # Confidence
        self.confidence_label = Label(
            text="Confidence: --",
            font_size="18sp",
            size_hint_y=None,
            height=dp(40)
        )

        self.add_widget(
            self.confidence_label
        )

        # Information
        self.info_label = Label(
            text=(
                "Screening result only.\n"
                "This is not a medical diagnosis."
            ),
            font_size="14sp",
            size_hint_y=None,
            height=dp(60)
        )

        self.add_widget(
            self.info_label
        )

        # New scan button
        self.new_scan_button = Button(
            text="NEW SCAN",
            size_hint_y=None,
            height=dp(50)
        )

        self.add_widget(
            self.new_scan_button
        )

        # Start API request
        self.get_prediction()

    def get_prediction(self):

        api_url = "http://127.0.0.1:5000/predict"

        try:

            with open(
                self.image_path,
                "rb"
            ) as image:

                files = {
                    "image": (
                        "captured_skin.jpg",
                        image,
                        "image/jpeg"
                    )
                }

                response = requests.post(
                    api_url,
                    files=files,
                    timeout=30
                )

            if response.status_code != 200:

                self.result_label.text = (
                    "Unable to get result"
                )

                return

            data = response.json()

            prediction = data.get(
                "prediction"
            )

            confidence = data.get(
                "confidence"
            )

            self.result_label.text = (
                f"Prediction: {prediction}"
            )

            self.confidence_label.text = (
                f"Confidence: "
                f"{confidence * 100:.2f}%"
            )

        except Exception as error:

            self.result_label.text = (
                "Connection error"
            )

            self.confidence_label.text = (
                str(error)
            )