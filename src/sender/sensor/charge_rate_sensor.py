import random


class ChargeRateSensor:

    def __init__(self, min_threshold = 0.05, max_threshold = 3):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

    def simulate_reading(self, count=1):

        simulated_readings = [
            round(random.uniform(self.min_threshold, self.max_threshold), 2) for _ in range(count)
        ]

        return simulated_readings
