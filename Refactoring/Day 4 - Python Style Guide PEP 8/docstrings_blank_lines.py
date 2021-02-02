# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        pass

    def read_voltage(self):
        """Returns the voltage."""      
        return 2.7

    def get_temperature(self):
        """Returns the temperature by multiplying the voltage and the temperature factor."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  

class CarbonMonoxideSensor:
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Updates and returns the carbon monoxide."""
        sensor_voltage = self.read_sensor_voltage()
        temperature = self.on_board_temp_sensor.get_temperature()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(self, sensor_voltage, temperature)
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Returns the sensor voltage read."""
        # In real life, it should read from hardware.        
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Returns the converted voltage by multiplying the voltage, voltage factor, and the temperature."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    def __init__(self):
        self.string = ''

    def display(self, msg):
        """Show the message."""
        print(msg)


class CarbonMonoxideDevice():
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit 
              
    def Display(self):
        """Creates the UI to display."""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    