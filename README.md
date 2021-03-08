# USER GUIDE
Modules:
- pynput (pip install)
- flask (pip install)
- os (pre-install)
- json (pre-install)
- threading (pre-install)

Features:
- With CMD execute "flask run" while in the same directory as app.py
- Add a 3 letters "Key" in order to expand it into a full text
- Edit, remove and add as many keys you want

How it Works?
- With Pynput receives keyword inputs
- It creates a list of inputs and checks for the last 3 inputs received
- If the last 3 inputs are keys in the "keys.json" file then it expands into the desired text
- In case of force exiting the program the "qqq" key is hardcoded into exiting (AVOID USING THIS KEY)

Future Improvements:
- Keys do not work if they contain numbers or special characters
- Basic Code optimization
- Basic GUI improvements
- Automatic Server implementation
- Web-Application instead of local app
- There is a slight chance of bugging if turned on/off too quickly because of file interference (os module)
