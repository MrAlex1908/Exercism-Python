"""Generate verses from "The Twelve Days of Christmas" song."""


def recite(start_verse, end_verse):
    """Return the requested range of verses from the Christmas song."""
    days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


    gifts = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]
    start = "On the "
    middle = " day of Christmas my true love gave to me: "
    
    verses = []
    for day in range(start_verse-1, end_verse):
        verse = start + days[day] + middle
        for gift in range(day, -1, -1):
            if gift == 0 and day != 0:
                verse += "and "
            verse += gifts[gift]
            if gift != 0:
                verse += ", "
        verses.append(verse + ".")
    return verses