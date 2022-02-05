import machine
import utime

sesore_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

while True:
    reading = sesore_temp.read_u16() * conversion_factor
    tempurature = 27 - (reading - 0.706)/0.001721
    print(tempurature)
    utime.sleep(2)
