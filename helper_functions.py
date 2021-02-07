import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zone(x, y):
    if abs(x) <= 1 and y >= 1.75 and y <= 3.5:
        return 1
    else:
        return 0

def swing(call):
    if call == "InPlay" or call == "FoulBall" or call == "StrikeSwinging":
        swing = 1
    else:
        swing = 0
    return swing

def get_title(col):
    if col == 'swing%':
        return 'Swing Rate by Inning'
    elif col == 'z_swing%':
        return 'Zone Swing Rate by Inning'
    elif col == 'o_swing%':
        return 'Reach Rate by Inning'

def get_label(col):
    if col == 'swing%':
        return 'Swing Rate'
    elif col == 'z_swing%':
        return 'Zone Swing Rate'
    elif col == 'o_swing%':
        return 'Reach Rate'

def get_file(col):
    if col == 'swing%':
        return 'graphs/swing_rate.jpg'
    elif col == 'z_swing%':
        return 'graphs/zone_swing_rate.jpg'
    elif col == 'o_swing%':
        return 'graphs/reach_rate.jpg'
