from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Halo! Ini aplikasi Android dari Python")
        button = Button(text="Klik Saya")

        button.bind(on_press=self.ganti_text)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def ganti_text(self, instance):
        self.label.text = "Tombol sudah diklik!"

if __name__ == "__main__":
    MyApp().run()
