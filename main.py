import pyautogui as pygui #pip install pyautogui
import win32clipboard as clip #pip install pywin32
import time

while True:
    time.sleep(5)
    # Copy the email first
    pygui.hotkey('ctrlleft', 'shiftright', 'shiftleft', 'right')
    pygui.hotkey('ctrlleft', 'x')

    clip.OpenClipboard()
    isDone = clip.GetClipboardData()
    clip.CloseClipboard()
    if (isDone == "done"):
        exit()

    pygui.hotkey('del')
    pygui.hotkey('alt', 'tab')

    pygui.moveTo(1660, 100, duration=1)  # Coordinates of login button
    pygui.click()
    pygui.moveTo(996, 469, duration=1)  # Coordinates of Login with Google button
    pygui.click()
    # pygui.moveTo(888,562, duration = 1) #Coordinates of Gunakan Akun lain (Use another account)
    # pygui.click()
    pygui.moveTo(779, 507, duration=1)  # Coordinates of email field
    pygui.click()

    # Paste the email
    pygui.hotkey('ctrlleft', 'v')
    pygui.moveTo(1170, 705, duration=1)  # Coordinates of berikutnya (next button)
    pygui.click()
    time.sleep(3)  # wait for loading

    # Move to notepad again
    pygui.keyDown('alt')
    pygui.press('tab')
    pygui.press('tab')
    pygui.keyUp('alt')

    # Copy the password
    time.sleep(3)  # wait for loading
    pygui.hotkey('ctrlleft', 'shiftright', 'shiftleft', 'right')
    pygui.hotkey('ctrlleft', 'x')
    pygui.hotkey('del')
    pygui.hotkey('alt', 'tab')

    pygui.moveTo(779, 507, duration=1)  # Coordinates of password field
    pygui.click()

    # Paste the password
    pygui.hotkey('ctrlleft', 'v')
    pygui.moveTo(1170, 735, duration=1)  # Coordinates of berikutnya (next button)
    pygui.click()
    time.sleep(10)  # wait for loading
    # Hide the notepad
    pygui.hotkey('alt', 'tab')

    # Move the cursor to select the file
    pygui.moveTo(163, 395, duration=1)  # Coordinates of select the file
    pygui.click()

    # Move the cursor to 'Save to TeraBox'
    pygui.moveTo(1542, 285, duration=1)  # Coordinates of 'Save to TeraBox' button
    pygui.click()

    # Move the cursor to 'Yes'
    pygui.moveTo(1093, 699, duration=1)  # Coordinates of 'Yes' button
    pygui.click()

    # Move the cursor to 'X' (close) button
    pygui.moveTo(1201, 397, duration=1)  # Coordinates of select the file
    pygui.click()

    # Move the cursor to profile button
    pygui.moveTo(1570, 93, duration=1)  # Coordinates of profile

    # Move the cursor to signout button
    pygui.moveTo(1521, 389, duration=1)  # Coordinates of signout button
    pygui.click()

    # Move the cursor to 'yes' signout button
    pygui.moveTo(896, 599, duration=1)  # Coordinates of 'yes' signout button
    pygui.click()

    # New tab to 'https://myaccount.google.com/'
    pygui.hotkey('ctrlleft', 't')

    pygui.write('https://myaccount.google.com/')
    pygui.hotkey('enter')

    time.sleep(5)

    # Move the cursor to 'Google Account Profile' button
    pygui.moveTo(1875, 103, duration=1)  # Coordinates of 'Google Account Profile' button
    pygui.click()

    # Move the cursor to 'Signout of all accounts' button
    pygui.moveTo(1702, 458, duration=1)  # Coordinates of 'Signout of all accounts' button
    pygui.click()

    # Move the cursor to 'Remove account' button
    pygui.moveTo(881, 580, duration=1)  # Coordinates of 'Remove account' button
    pygui.click()

    # Move the cursor to 'Select Account' button
    pygui.moveTo(1133, 514, duration=1)  # Coordinates of 'Select Account' button
    pygui.click()

    # Move the cursor to 'Yes Delete' button
    pygui.moveTo(1068, 632, duration=1)  # Coordinates of 'Yes Delete' button
    pygui.click()

    # Close 'https://myaccount.google.com/' tab
    pygui.hotkey('ctrlleft', 'w')

    # Move to notepad again
    pygui.hotkey('alt', 'tab')