from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresApp(App):
    def build(self):
        Window.size = (500, 400)
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('miles_kilometres.kv')
        return self.root

    def handle_calculate(self):
        try:
            result = int(self.root.ids.input_number.text) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, value):
        try:
            result = int(self.root.ids.input_number.text) + value
            self.root.ids.input_number.text = str(result)
        except ValueError:
            result = 0 + value
            self.root.ids.input_number.text = str(result)


MilesToKilometresApp().run()