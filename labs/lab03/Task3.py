import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from subprocess import Popen, PIPE
import time

def get_IP():
    p = Popen(["hostname", "-I"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output.decode()

def get_CPU_temperature():
    p = Popen(["vcgencmd", "measure_temp"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return (output.decode().replace("temp=", "").replace("'C\n", ""))

lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [255, 255, 255]


current_menu = "INITIAL"


while True:
   
    if current_menu == "INITIAL":
        if lcd.up_button:
            current_menu = "IP"
            lcd.clear()
            lcd.message = get_IP()
            time.sleep(0.5)
        elif lcd.down_button:
            current_menu = "TEMP"
            lcd.clear()
            lcd.message = get_CPU_temperature()
            time.sleep(0.5)
    elif lcd.select_button:
        lcd.clear()
        break

    elif current_menu == "IP":
        if lcd.up_button:
            current_menu = "TEMP"
            lcd.clear()
            lcd.message = get_CPU_temperature()
            time.sleep(0.5)
        elif lcd.down_button:
            current_menu = "TEMP"
            lcd.clear()
            lcd.message = get_CPU_temperature()
            time.sleep(0.5)
    elif current_menu == "TEMP":
        if lcd.up_button:
            current_menu = "IP"
            lcd.clear()
            lcd.message = get_IP()
            time.sleep(0.5)
        elif lcd.down_button:
            current_menu = "IP"
            lcd.clear()
            lcd.message = get_IP()
            time.sleep(0.5)


    else:
        print("Encountered an unexpected state: ", current_menu)
