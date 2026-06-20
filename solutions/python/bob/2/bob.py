"""This file will help you you to predict a teenager Bob."""

def response(hey_bob):
    """This function calculates Bob's answer."""
    clean_message = hey_bob.strip()
    if clean_message.isupper() and clean_message.endswith("?"):  
        return "Calm down, I know what I'm doing!"
    if clean_message.endswith("?"):
        return "Sure."
    if clean_message.isupper():
        return "Whoa, chill out!"
    if not clean_message: 
        return "Fine. Be that way!"
    else: 
        return "Whatever."
