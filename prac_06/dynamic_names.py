from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicNamesApp(App):
    status_text = StringProperty()

    def __init__(self, **tyler):
        super().__init__(**tyler)
        self.names = ['Bob', 'Cyan', 'Me']

    def build(self):
        self.title = "Dynamic Names"
        self.root = Builder.load_file('dynamic_names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.id
        self.status_text = "{}".format(name)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicNamesApp().run()

