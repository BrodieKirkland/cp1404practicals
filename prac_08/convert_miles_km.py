from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKm(App):
    """Convert miles to kilometres Kivy App"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_miles_to_km(self):
        """Convert miles to kilometres"""
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(kilometres)

    def get_valid_miles(self):
        """Get miles, return 0 on error"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, increment):
        """Change mile input by increment"""
        incremented_mile = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(incremented_mile)
        self.handle_convert_miles_to_km()


ConvertMilesToKm().run()
