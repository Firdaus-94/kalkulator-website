from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcLayout(BoxLayout):
    def tambah(self, nilai):
        self.ids.input.text += nilai

    def hitung(self):
        try:
            self.ids.input.text = str(eval(self.ids.input.text))
        except:
            self.ids.input.text = "Error"

    def hapus(self):
        self.ids.input.text = ""

class KalkulatorApp(App):
    def build(self):
        return CalcLayout()

KalkulatorApp().run()
