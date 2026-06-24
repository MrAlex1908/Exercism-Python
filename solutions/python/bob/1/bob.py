def response(hey_bob):
    clean_message = hey_bob.strip()
    if clean_message.isupper() and clean_message.endswith("?"):  
        return "Calm down, I know what I'm doing!"
    elif clean_message.endswith("?"):
        return "Sure."
    elif clean_message.isupper():
        return "Whoa, chill out!"
    elif not clean_message: 
        return "Fine. Be that way!"
    else: 
        return "Whatever."
