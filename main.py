import pyautogui
import time
import sys

# Check if at least two arguments are provided (script name and input value)
if len(sys.argv) < 2:
    print("Usage: python main.py <input_value>")
    print("Example: python main.py 100")
    sys.exit(1)  # Exit with an error code
# Access the command-line argument (assuming the input value is the second argument)
input_value = int(sys.argv[1])

# stop for 5s
print("The Script is Started running...")
time.sleep(5)
count = 0
i = input_value

while count <= i:
    pyautogui.typewrite("Dumpshit" + str(count))
    time.sleep(0.1)
    count = count + 1
    pyautogui.press("enter")
