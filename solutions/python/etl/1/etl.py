"""ETL exercise for transforming legacy letter-score data."""


def transform(legacy_data):
    """Transform score-to-letters data into lowercase letter-to-score data."""
    
    new_data = {}
    
    for score, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = score
    return new_data

