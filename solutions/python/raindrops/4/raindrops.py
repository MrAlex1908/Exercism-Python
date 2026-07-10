"""Convert numbers into raindrop sounds."""
class Rule: 
    """Represent one raindrop conversion rule."""
    def __init__(self, divisor, sound):
        self.divisor = divisor
        self.sound = sound
    def applies_to(self, number):
        return number % self.divisor == 0

"""Rules how to convert"""
rules = [
    Rule(3, "Pling"),
    Rule(5, "Plang"),
    Rule(7, "Plong")
]
    
def convert(number):
    """This function converts numbers to sounds of rain."""
    result = ""

    for rule in rules:
        if rule.applies_to(number):
            result += rule.sound

    if result == "":
        result = str(number)

    return result