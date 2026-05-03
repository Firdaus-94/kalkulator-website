from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcLayout(BoxLayout):
    def calculate(self, expression):
        try:
            return str(eval(expression))
        except:
            return "Error"

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

CalculatorApp().run()
