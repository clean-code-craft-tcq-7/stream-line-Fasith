from src.sender.sensor.temperature_sensor import TemperatureSensor

def test_temperature_sensor_initializor():
    min_threshold, max_threshold = [20, 30]
    temperature_sensor = TemperatureSensor(min_threshold, max_threshold)
    assert(temperature_sensor.min_threshold == min_threshold)
    assert(temperature_sensor.max_threshold == max_threshold)


def test_temperature_sensor_simulate_reading():
    min_threshold, max_threshold = [20, 30]
    temperature_sensor = TemperatureSensor(min_threshold, max_threshold)
    simulated_readings = temperature_sensor.simulate_reading(50)
    assert(len(simulated_readings) == 50)
    assert(min(simulated_readings) >= min_threshold)
    assert(max(simulated_readings) <= max_threshold)
    