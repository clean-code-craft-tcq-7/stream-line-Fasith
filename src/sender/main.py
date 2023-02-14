from src.sender.sensor.charge_rate_sensor import ChargeRateSensor
from src.sender.sensor.temperature_sensor import TemperatureSensor
from src.sender.logger import ConsoleLogger

def main(logger, number_of_streams = 1):
    
    charge_rate_sensor = ChargeRateSensor()
    temperature_sensor = TemperatureSensor()

    for i in range(0, number_of_streams):
        charge_rate_readings = charge_rate_sensor.simulate_reading(50)
        temperature_readings = temperature_sensor.simulate_reading(50)

        formatted_data = {
            "charge_rate" : charge_rate_readings,
            "temperature" : temperature_readings
        }

        logger.log(formatted_data)


if __name__ == "__main__":
    logger = ConsoleLogger()
    main(logger,2)

