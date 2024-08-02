---CRQ Automation Tool---
---Authors: Angus Webb, Redwan Chowdhury---

**DISCLAIMER** This script has been altered to anonymise people and processes within MTO. It does not currently work and is purely for demonstration purposes.

Version History:
1.0, March 04 2024:
-created crq.py script.

2.0, April 15 2024:
-added image recognition for more accurate locating of text fields/buttons. Images folder created
-divided screen into quadrants for faster image searches compared to searching the whole screen
-CI numbers no longer have to be added manually
-added multiple helper functions for cleaner and more concise code

2.0.1, April 29 2024:
-fixed a bug where risk assessment would not work for PROD CRQ's
-added UAT CRQ# entry method for PROD CRQ's

For the program to run properly, do the following:
-Manage Display Settings
    -Navigate to Settings > System > Display
    -Under "Scale and layout", set the first drop-down ("Change the size of text, apps and other items") to 150%
    -Set second drop-down ("Display resolution") to 1920 x 1080
    -Set third drop-down ("Display orientation") to Landscape
-Ensure that you are only using one monitor, as multiple monitors may mess with the layout of the pixels.
-Use Google Chrome for best results

Execution of the program:
-CRQ notes must be copied prior to running the script
-Ensure to have the application acronym, environment (UAT/PROD) and date ready
-If anything unexpected occurs, move the mouse to any corner of the screen to stop the program
-The program can stay running in the background while you perform other tasks. When going back to the program, check
 the terminal to see what it is currently looking for.
-The program will not save or hit "next stage" on the CRQ, so ensure to do so manually

Dependencies:
-pyautogui (https://pyautogui.readthedocs.io/en/latest/) for automation
-opencv (https://pypi.org/project/opencv-python/) helps the tool run on different computers
-pyperclip (https://pypi.org/project/pyperclip/) to access your computer's clipboard
-pillow (https://pypi.org/project/pillow/) for image recognition functionality
*note about installing dependencies: attempting to use "pip install x" on the office network will not work,
 but will work on different networks such as your home network. Therefore it is best to try installing these
 during a remote shift.