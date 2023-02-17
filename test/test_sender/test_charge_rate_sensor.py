from src.sender.sensor.charge_rate_sensor import ChargeRateSensor

def test_charge_rate_sensor_initializor():
    min_threshold, max_threshold = [0.05, 3]
    charge_rate_sensor = ChargeRateSensor(min_threshold, max_threshold)
    assert(charge_rate_sensor.min_threshold == min_threshold)
    assert(charge_rate_sensor.max_threshold == max_threshold)


def test_charge_rate_sensor_simulate_reading():
    min_threshold, max_threshold = [0.05, 3]
    charge_rate_sensor = ChargeRateSensor(min_threshold, max_threshold)
    simulated_readings = charge_rate_sensor.simulate_reading(50)
    assert(len(simulated_readings) == 50)
    assert(min(simulated_readings) >= min_threshold)
    assert(max(simulated_readings) <= max_threshold)
    