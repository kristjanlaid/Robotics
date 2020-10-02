import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = (1, 10, 50)
while True:
    if lcd.select_button == 1:
        lcd.message = ('True ')
    elif lcd.select_button == 0:
        lcd.message = ('False')
        

