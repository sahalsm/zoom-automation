import pyautogui
import subprocess
import tkinter
import time
import pandas as pd
from datetime import datetime


def sign_in(id,pwd):
    subprocess.Popen("C:\\Users\\muham\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(5)

    try:
        join_btn = pyautogui.locateCenterOnScreen('join.png',confidence = .5)
        pyautogui.move(join_btn)
        pyautogui.click(join_btn)

        time.sleep(2)

        join_id = pyautogui.locateCenterOnScreen('join_id.png',confidence = .5)
        pyautogui.move(join_id)
        pyautogui.click(join_id)
        pyautogui.write(id)
        time.sleep(1)
        pyautogui.press('enter')

        time.sleep(5)

        join_pwd = pyautogui.locateCenterOnScreen('join_pwd.png',confidence = .5)
        pyautogui.move(join_pwd)
        pyautogui.click(join_pwd)
        pyautogui.write(pwd)
        time.sleep(1)
        pyautogui.press('enter')
    except:
        pass

df = pd.read_csv('schedule.csv')
while 1:
    now = datetime.now().strftime("%H:%M %A")
    if now in str(df['time']):
        row = df.loc[df['time'] == now]
        m_id = str(row.iloc[0,1])
        m_pwd = str(row.iloc[0,2])
        sign_in(m_id,m_pwd)
        print("signin successfully")
        time.sleep(40)




