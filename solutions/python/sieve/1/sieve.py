"""Find prime numbers using the Sieve of Eratosthenes algorithm."""


def primes(limit):
    """Return a sorted list of all prime numbers up to the given limit."""
    numbers = set(range(2, limit + 1))
    prime_numbers = set()

    while numbers:
        prime = min(numbers)
        prime_numbers.add(prime)
        numbers -= set(range(prime, limit + 1, prime))

    return sorted(prime_numbers)