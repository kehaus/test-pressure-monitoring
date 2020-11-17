#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:37:39 2020

@author: root
"""

import os




import os 
import sys
import time

import numpy as np
from PyQt5.QtWidgets import QApplication

pp = os.path.dirname(os.getcwd())
path_tpg = os.path.join(pp, 'time-plot-gui', 'src')

test_mode = True
if not test_mode:
    from TimePlotGui import TimePlotGui, TimePlotMainWindow, DeviceWrapper, DummyDevice, start_application
else:
    module_path = path_tpg
    if module_path not in sys.path:
        sys.path.append(module_path)
    from src import TimePlotGui, TimePlotMainWindow, DeviceWrapper, DummyDevice, start_application
    
    
from pfeiffer import TPG261
    

t = TPG261()
dw = DeviceWrapper(t)

# initialized UI
start_application([dw], sampling_latency=0.05)



    