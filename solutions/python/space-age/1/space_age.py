"""Calculate a person's age in years on different planets."""


class SpaceAge:
    """Calculate age based on the orbital periods of Solar System planets."""

    DURATION_OF_EARTH_YEAR = 31557600

    def __init__(self, seconds):
        """Initialize a SpaceAge instance with an age in seconds."""
        self.seconds = seconds

    def _calculate_age(self, orbital_period):
        """Return age in years for the given orbital period."""
        return round(
            self.seconds / (orbital_period * SpaceAge.DURATION_OF_EARTH_YEAR),
            2
        )

    def on_earth(self):
        """Return age in Earth years."""
        return self._calculate_age(1.0)

    def on_mars(self):
        """Return age in Mars years."""
        return self._calculate_age(1.8808158)

    def on_mercury(self):
        """Return age in Mercury years."""
        return self._calculate_age(0.2408467)

    def on_venus(self):
        """Return age in Venus years."""
        return self._calculate_age(0.61519726)

    def on_jupiter(self):
        """Return age in Jupiter years."""
        return self._calculate_age(11.862615)

    def on_saturn(self):
        """Return age in Saturn years."""
        return self._calculate_age(29.447498)

    def on_uranus(self):
        """Return age in Uranus years."""
        return self._calculate_age(84.016846)

    def on_neptune(self):
        """Return age in Neptune years."""
        return self._calculate_age(164.79132)