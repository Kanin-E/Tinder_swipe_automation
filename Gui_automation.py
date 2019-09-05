
import os
import sys

import pyautogui


# sys.path
sys.path.append('/home/calanin/.local/lib/python3.6/site-packages')
### Need to append path because default part not include the library path 

os.chdir('/media/calanin/Second HDD/Data_science/Personal_projects/Tinder/captured_pics')

max_photo_no = 9
no_girl_prfl_to_capture = 100

coors = {}
# required
coors['left'] = 996 
coors['right'] = 1367
coors['top'] = 250
coors['bottom'] = 704
coors['blank_space'] = [1560, 510] # for clicking the tinder window screen 

# optional
coors['more_info'] = [1333, 741]
coors['less_info'] = [1333, 700]
coors['next_pic'] = [1353, 483]
coors['pass'] = [1109, 853] 
coors['like'] = [1253, 854]


# Auto save photo to create dataset (next step: create it for the prediction)
## you need to open Tinder screen window in one tab of your browser
#### And don't move your mouse !!!!!

pyautogui.click(
    x=coors['blank_space'][0], 
    y=coors['blank_space'][1], 
    interval=0.25,
)
# To make sure the tinder screen is up
for idx_prfl in range(no_girl_prfl_to_capture):
    pyautogui.press('up', interval=1) # go to more info page

    for idx_pic in range(max_photo_no): # save pictures
        image_file_name = f"girl{idx_prfl+1}_pic{idx_prfl+1}.png"
        im(
            imageFilename=image_file_name, 
            region=(
                coors['left'], coors['top'], 
                coors['right'] - coors['left'],
                coors['bottom'] - coors['top'],
                )
        )
        pyautogui.press('space',interval=0.1) # next photo

    pyautogui.press('left' ,interval=0.25) # cancel     


