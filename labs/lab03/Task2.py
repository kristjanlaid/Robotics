import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
# To run Linux commands from Python(to get CPU temperature and IP) import Popen and PIPE.
from subprocess import Popen, PIPE
import time
# The following function can be used to get the Raspberry's IP address.
# It returns device IP as a character string.
# Note that the functions are not run right away at the beginning of the program, 
# but only when they are called.
def get_IP():
    p = Popen(["hostname", "-I"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output.decode()

# You can use the following function to read the CPU temperature.
# The function runs the Linux command 'vcgencmd -measure_temp' and returns the result as a character string.
def get_CPU_temperature():
    p = Popen(["vcgencmd", "measure_temp"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return (output.decode().replace("temp=", "").replace("'C\n", ""))

lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [255, 255, 255]

# Initialize our state variable.
# Note that the variable is named so that it reflects the meaning of it in the program.
# Also, the state values can be strings so, it is possible to use reasonable names for states
current_menu = "INITIAL"

# The main loop, that runs until the program is closed
while True:
    # Within the main loop we first check the state values 
    # as we want to have different behaviour for different states
    if current_menu == "INITIAL":
        if lcd.up_button:
            # Change the state.
            current_menu = "IP"
            # Do the actions that happen on the corresponding transition.
            lcd.clear()
            # Make the screen to show an IP message
            lcd.message = get_IP()
            time.sleep(0.5)
        elif lcd.down_button:
            current_menu = "TEMP"
            lcd.clear()
            lcd.message = get_CPU_temperature()
            time.sleep(0.5)

    elif current_menu == "IP":
        if lcd.up_button:
            # Change the state
            current_menu = "TEMP"
            # Do the actions that happen on the corresponding transition.
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

    # Having an else statement that is run when no state matched the current one
    # is a good habit and helps for example to find out typos within state names
    # In the current tasks we should never reach this print command.
    else:
        print("Encountered an unexpected state: ", current_menu)
