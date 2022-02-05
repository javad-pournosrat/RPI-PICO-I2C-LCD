import machine
import utime
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

sesore_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

while True:
    reading = sesore_temp.read_u16() * conversion_factor
    tempurature = 27 - (reading - 0.706)/0.001721
    #print(tempurature)
    lcd.putstr('Tempurature:\n' + str(tempurature)[0:5])
    lcd.custom_char(0, bytearray([
      0x07,
      0x05,
      0x07,
      0x00,
      0x00,
      0x00,
      0x00,
      0x00
      ]))
    
    lcd.move_to(5, 1)
    lcd.putchar(chr(0))
    lcd.move_to(6, 1)
    lcd.putstr('C')
    utime.sleep(2)
    lcd.clear()
