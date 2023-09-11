"""This is the interface for the wall safe using the pythondialog package. I adapted it from the examples at https://pythondialog.sourceforge.io/doc/intro/intro.html and https://pythondialog.sourceforge.io/ ."""
import sys
import locale
import time

from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

d = Dialog(dialog="dialog", autowidgetsize=True)

d.set_background_title('OOP Manor Custom Wall Safe')

while True:
    guess = d.passwordbox('Input passcode.', insecure=True)
    if guess[1] == 'yes':
        d.infobox("Unlocking...", title="Credentials validated")
        time.sleep(2)
        sys.exit(0)
    elif guess[0] == d.CANCEL:
        d.infobox("Goodbye.")
        time.sleep(1)
        sys.exit(0)
    else:
        d.infobox("Invalid credentials")
        time.sleep(1)
    if d.yesno('Try again?') == d.OK:
        continue
    else:
        d.infobox("Goodbye.")
        time.sleep(1)
        sys.exit(0)