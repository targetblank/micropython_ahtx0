# micropython_ahtx0

MicroPython driver for the AHT10 and AHT20 temperature and humidity sensors.

## Example usage

```python
import utime
from machine import Pin, I2C

import ahtx0

# I2C for the Wemos D1 Mini with ESP8266
i2c = I2C(scl=Pin(5), sda=Pin(4))

# Create the sensor object using I2C
sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.2f C" % sensor.temperature)
    print("Humidity: %0.2f %%" % sensor.relative_humidity)
    utime.sleep(5)
```

## Changelog

### 0.1.2

- fixed packaging

### 0.1.1

- fixed code style and typos

### 0.1.0

- initial release