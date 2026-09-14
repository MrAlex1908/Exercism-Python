"""Recite verses from the Ten Green Bottles song."""


def recite(start, take=1):
    """Return the requested number of verses starting from a given bottle count."""
    bottles = [
    "One green bottle",
    "Two green bottles",
    "Three green bottles",
    "Four green bottles",
    "Five green bottles",
    "Six green bottles",
    "Seven green bottles",
    "Eight green bottles",
    "Nine green bottles",
    "Ten green bottles",
]
    all_verses = []
    
    while take > 0:
        verse = []
        
        if start != 1:
            #Some pre-calculations
            current_bottle = bottles[start - 1]
            next_bottle = bottles[start - 2]
            lower_next_bottle = next_bottle.lower()
            
            line_1 = f"{current_bottle} hanging on the wall,"
            line_2 = line_1
            line_3 = "And if one green bottle should accidentally fall,"
            line_4 = f"There'll be {lower_next_bottle} hanging on the wall."
            if take > 1:
                line_5 = ""
                verse += (line_1, line_2, line_3, line_4, line_5)
            else:
                verse += (line_1, line_2, line_3, line_4)
                
            start -= 1
            take -= 1
            
            all_verses.extend(verse)
            
        else:
            line_1 = "One green bottle hanging on the wall,"
            line_2 = line_1
            line_3 = "And if one green bottle should accidentally fall,"
            line_4 = "There'll be no green bottles hanging on the wall." # or no_bottle = bottle[1] \n line_4 = f"There'll be {no_bottle.replace("One", "no")} hanging on the wall."
            
            verse += (line_1, line_2, line_3, line_4)
            all_verses.extend(verse)
            
            start -= 1
            take -= 1
            
    return all_verses