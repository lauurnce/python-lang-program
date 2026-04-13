# Simple Polymorphism Example in Python - F1 Drivers

class F1Driver:
    def introduce(self):
        return "I am an F1 driver"

class MercedesDriver(F1Driver):
    def introduce(self):
        return "I drive for Mercedes"

class FerrariDriver(F1Driver):
    def introduce(self):
        return "I drive for Ferrari"

class RedBullDriver(F1Driver):
    def introduce(self):
        return "I drive for Red Bull"

# Demonstrating polymorphism
drivers = [MercedesDriver(), FerrariDriver(), RedBullDriver(), F1Driver()]

for driver in drivers:
    print(f"{driver.__class__.__name__}: {driver.introduce()}")

# Output:
# MercedesDriver: I drive for Mercedes
# FerrariDriver: I drive for Ferrari
# RedBullDriver: I drive for Red Bull
# F1Driver: I am an F1 driver