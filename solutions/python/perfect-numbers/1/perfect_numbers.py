def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors = []
    
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
        
    divisors_sum = sum(divisors)

    if number == divisors_sum:
        return "perfect"
    
    if number > divisors_sum: 
        return "deficient"
    
    if number < divisors_sum: 
        return "abundant"