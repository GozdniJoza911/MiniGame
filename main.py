from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MiniGame(App):

    def build(self):

        self.score = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.label = Label(
            text="Score: 0",
            font_size=40
        )

        button = Button(
            text="SCORE +1",
            font_size=30
        )

        button.bind(
            on_press=self.add_score
        )

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def add_score(self, instance):

        self.score += 1

        self.label.text = (
            f"Score: {self.score}"
        )


if __name__ == "__main__":
    MiniGame().run()
