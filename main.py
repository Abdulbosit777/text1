from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


Config.set("graphics", "resizable", 1)
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 400)


class Applicastion(App):

    def click(self, instance):
        self.label.text = "Raxmat knopkalarni bosganingiz uchun!!"



    def build(self):

        but_together = BoxLayout()
        grid = GridLayout(cols=1)

        my_but = Button(text="Meni tez bos!!!", font_size=30, background_color="cyan", on_press=self.click)
        think_of_name = Button(text="Meni bosma!!!", font_size=30, background_color="cyan")
        self.label = Label(text="So'z", font_size=30)



        but_together.add_widget(my_but)
        but_together.add_widget(think_of_name)

        grid.add_widget(but_together)
        grid.add_widget(self.label)

        return grid




if __name__=="__main__":
    Applicastion().run()