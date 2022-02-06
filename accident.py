import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.clear()


for i in range(0, 16):
        lcd.custom_char(0, bytearray([
              
              0x15,
              0x1F,
              0x1F,
              0x15,
              0x1F,
              0x11,
              0x1F,
              0x1F
                
                ]))
        lcd.custom_char(2, bytearray([
              
              0x15,
              0x1F,
              0x1F,
              0x15,
              0x1F,
              0x11,
              0x1F,
              0x1F
                
                ]))


        if int(i)%2 == 0:

            
            lcd.custom_char(1, bytearray([
              
              0x04,
              0x04,
              0x0E,
              0x15,
              0x04,
              0x04,
              0x0A,
              0x11
                
                ]))
            

            
            lcd.custom_char(3, bytearray([
              
              0x04,
              0x04,
              0x0E,
              0x15,
              0x04,
              0x04,
              0x0A,
              0x11
                
                ]))
        else:

                lcd.custom_char(1, bytearray([
                  
                  0x04,
                  0x04,
                  0x1F,
                  0x04,
                  0x04,
                  0x04,
                  0x0A,
                  0x11
                    
                    ]))
                

                lcd.custom_char(3, bytearray([
                  
                  0x04,
                  0x04,
                  0x1F,
                  0x04,
                  0x04,
                  0x04,
                  0x0A,
                  0x11
                    
                    ]))
            
        if (int(i)) == 8:
            lcd.clear()
            lcd.custom_char(4, bytearray([
                  
                  0x00,
                  0x00,
                  0x00,
                  0x1F,
                  0x16,
                  0x1F,
                  0x16,
                  0x1F
                    
                    ]))
            lcd.custom_char(5, bytearray([
                  
                  0x00,
                  0x00,
                  0x00,
                  0x03,
                  0x12,
                  0x0E,
                  0x12,
                  0x03
                    
                    ]))
            lcd.custom_char(6, bytearray([
                  
                  0x00,
                  0x00,
                  0x00,
                  0x11,
                  0x08,
                  0x07,
                  0x08,
                  0x11
                    
                    ]))
            lcd.custom_char(7, bytearray([
                  
                  0x00,
                  0x00,
                  0x00,
                  0x1F,
                  0x0D,
                  0x1F,
                  0x0D,
                  0x1F
                    
                    ]))
            lcd.custom_char(8, bytearray([
                
                  0x00,
                  0x00,
                  0x00,
                  0x18,
                  0x09,
                  0x0E,
                  0x09,
                  0x18
                    ]))
            lcd.custom_char(9, bytearray([
                
                  0x00,
                  0x00,
                  0x00,
                  0x11,
                  0x02,
                  0x1C,
                  0x02,
                  0x11
                    ]))
            
            lcd.move_to(11,1)
            lcd.putchar(chr(4))
            
            lcd.move_to(10,1)
            lcd.putchar(chr(5))
            
            lcd.move_to(9,1)
            lcd.putchar(chr(6))
            
            lcd.move_to(4,1)
            lcd.putchar(chr(7))
            
            lcd.move_to(5,1)
            lcd.putchar(chr(8))
            
            lcd.move_to(6,1)
            lcd.putchar(chr(9))
            
            utime.sleep(1)
            #lcd.clear()
            break
            
        lcd.move_to(int(i),0)
        lcd.putchar(chr(0))
        lcd.move_to(int(i),1)
        lcd.putchar(chr(1))
        #utime.sleep(1)

        lcd.move_to(15-int(i),0)
        lcd.putchar(chr(2))
        lcd.move_to(15-int(i),1)
        lcd.putchar(chr(3))
        
        
        
        utime.sleep(1)
        lcd.clear()
