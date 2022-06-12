"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
KM_PER_MILE=1.60934

class ConvertMilesKm(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self,value,increment):
        #self.message = self.root.ids.user_input.text
        try:
            value = float(value)
        except ValueError:
            value=0

        value += increment
        self.root.ids.user_input.text = str(value)




    def handle_convert(self,value):
        #self.message = self.root.ids.user_input.text
        try:
            miles=float(value)
        except ValueError:
            self.message="Please enter valid miles."

        km= miles*KM_PER_MILE
        self.message=str(km)


# create and start the App running
ConvertMilesKm().run()
