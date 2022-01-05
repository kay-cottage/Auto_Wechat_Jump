import os
import cv2
import numpy as np
import sys
from PIL import ImageGrab
import pyautogui
import time
 


#得到不含纯色的像素线段
def get_cube_position(pic_path):
        img = cv2.imread(pic_path,0)
        pic_array = np.array(img)
        #print(pic_array)
        ix = 0
        position = []
        for x in pic_array.tolist():
                ix = ix+1
                for y in x:
                        if y!= x[0]:
                                #print('ix:iy',ix,x.index(y))
                                position_tuple = (x.index(y),ix)
                                position.append(position_tuple)
        return position
                        
                                
                        
def get_screen():
    bbox = (5, 210, 440, 600)
    im = ImageGrab.grab(bbox)    
    im.save('1.png')
    print('saved successfully')
    


def get_distance(position):
    chess_location = pyautogui.locateCenterOnScreen(r'2.png',confidence=0.7)
    chess_x = chess_location[0]
    chess_y = chess_location[1]+70
    position_x = position[0]+5
    position_y = position[1]+210+32
    print('cube_x:cube_y:',position_x,position_y)
    print('chess_x:chess_y',chess_x,chess_y)
    distance = pow((position_y-chess_y)**2 + (chess_x-position_x)**2,0.5)
    print('distance',distance)
    return distance
    
def press_time(distance):
    press_time = distance * 0.0023
    print('press_time:',press_time)
    print('#######')
    return press_time

print('start')    
time.sleep(2)
for i in range(150):
    get_screen()
    position = get_cube_position('1.png')[0]
    get_distance(position)
    #print(position)
    distance = get_distance(position)
    pyautogui. mouseDown()
    time.sleep(press_time(distance))
    pyautogui.mouseUp()
    time.sleep(1)

