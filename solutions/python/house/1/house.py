"""Recite verses from the cumulative nursery rhyme "This is the House that Jack Built"."""


def recite(start_verse, end_verse):
    """Return the requested range of verses as a list of strings."""
    
    objects = [
        "the house that Jack built",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn"
    ]

    actions = [
        None,
        "that lay in",
        "that ate",
        "that killed",
        "that worried",
        "that tossed",
        "that milked",
        "that kissed",
        "that married",
        "that woke",
        "that kept",
        "that belonged to"
    ]
    

    verses = []
    for verse_index in range(start_verse - 1, end_verse):
        verse = f"This is {objects[verse_index]}"
        for char in range(verse_index, 0, -1):
            verse += f" {actions[char]} {objects[char - 1]}" 
        verses.append(verse + ".")
    return verses

