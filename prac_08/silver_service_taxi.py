from prac_08.taxi import Taxi
import random

class SilverServiceTaxi(Taxi):
    flagfall=4.5

    def __init__(self, name, fuel, fanciness):
       super().__init__(name, fuel)
       self.fanciness=fanciness
       self.price_per_km=self.price_per_km*fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${}".format(super().__str__(),
                                                             self.flagfall)

    def get_fare(self):
        return super().get_fare()+self.flagfall

