# SSDN_LiveCapGUI.py

import PySimpleGUI as sg
import os.path
import tkinter.font
from datetime import datetime
#Importing python module random to generate random numbers
import random as rnd

sg.theme('DarkTanBlue')
#sg.theme('Topanga')
cfont='Times New Roman'
#wfont=("liberation mono",18)	#Mono space font family
wfont=("courier",20)	#Mono space font family
sg.set_options(font=wfont)

class GUI():
    def __init__(self, location):
        self.blink_count = 0

#getting current time and return it
def clk():
    ntime=datetime.now()
    nt=ntime.strftime('\n\n%H:%M:%S')
    return nt

# SSDN GUI Operator Entry, window layout of three columns
data_entry_column = [
    [
        sg.Text("Select ONE TACNAV Input to Capture", size=(40, 1))
    ],
    [
        sg.Checkbox("DHSYL1 : Digital High Speed Log 1", default=True, text_color="green", enable_events=True,
                    key='dhsyl1cb'),
    ],
    [
        sg.Checkbox("DHSYL2 : Digital High Speed Log 2", default=False, text_color="red", enable_events=True,
                    key='dhsyl2cb'),
    ],
    [
        sg.Checkbox("DDD1 : Digital Depth Detector 1", default=False, text_color="red", enable_events=True,
                    key='ddd1cb'),
    ],
    [
        sg.Checkbox("DDD2 : Digital Depth Detector 2", default=False, text_color="red", enable_events=True,
                    key='ddd2cb'),
    ],
    [
        sg.Checkbox("GYRO : Gyroscope Navigation", default=False, text_color="red", enable_events=True, key='gyrocb'),
    ],
    [
    ],
    [
        sg.Text("{:<32}".format("CAPTURE TIME (Minutes)")),
        sg.InputText(key="CAPTIME", size=(10, 1), disabled=False, do_not_clear=True, justification='r')
    ],
    [
        sg.Text("{:<32}".format("MAX NUMBER OF PACKETS DROPPED")),
        sg.InputText(key="INTTIME", size=(10, 1), disabled=False, do_not_clear=True, justification='r')
    ],
    [
        sg.Text("{:<32}".format("ETHERNET PORT")),
        sg.InputText(key="ETHPORT", size=(10, 1), disabled=False, do_not_clear=True, justification='r')
    ],
    [
        sg.Button("START"),
    ],
    [
        sg.Button("EXIT"),
    ],
    [
        #sg.Text('', key='-time-', font=(cfont, 16), justification='left')
        sg.Text('', key='-time-', justification='left')
    ],
]

data_entry_column2 = [
    [
        sg.Text("OR Select NEIS Output to Capture", size=(40, 1))
    ],
    [
        sg.Checkbox("SDM : Ship Data Message", default=False, text_color="red", enable_events=True, key='sdmcb'),
    ],
    [
        sg.Checkbox("NDM : Navigation Data Message", default=False, text_color="red", enable_events=True, key='ndmcb'),
    ],
]

# Display Ohio SSBN Submarine Image
image_viewer_column = [
    [sg.Image("Trident.png")],  # Python 3
    # [sg.Image("OhioSub.gif")],	# Python 2
    [
        sg.Checkbox("OUTPUT FILE FORMAT PCAP", default=False, enable_events=True, key='pcapcb'),
    ],
    [
        sg.Text("Default Format CSV"),
    ],
    [
        sg.Checkbox("SELECT TO DISABLE CSV", default=False, enable_events=True, key='csvcb'),
    ],
    [
        sg.Text("Error file and GUI only"),
    ],
]

# ----- Operator Data Entry layout -----
layout = [
    [
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(data_entry_column),
        sg.VSeperator(),
        sg.Column(data_entry_column2),
    ]
]

'''
=====================================================================================================
# Setup Live Run Time Output Window
=====================================================================================================
'''
def setup_outputwindow(parm1,parm2,parm3,sensor):

    # Setup GUI Run Time window columns
    data_output_column = [
        [
	    sg.Checkbox(sensor, default = True, text_color="green"),
        ],
        [
            sg.Text("{:<22}".format(parm1)),
            sg.InputText(key="PARM1",size=(16,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text("{:<22}".format(parm2)),
            sg.InputText(key="PARM2",size=(16,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text("{:<22}".format(parm3)),
            sg.InputText(key="PARM3",size=(16,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text("\n\nSSDN LIVE CAPTURE STATUS:",  text_color="green"),
        ],
        [
            sg.Text("ALL TIME DISPLAYED IN SECONDS\n",  text_color="green"),
        ],
        [
            #sg.Text("{:<28}".format(20,"DELTA TIME")),
            sg.Text(f"{'DELTA TIME':<28}"),
            sg.InputText(key="DLLTIM",size=(10,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            #sg.Text("{:<28}".format("MAX TIME INTERVAL")),
            sg.Text(f"{'MAX TIME INTERVAL':<28}"),
            sg.InputText(key="MAXTIM",size=(10,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text("{:<28}".format("ELAPSED TIME")),
            sg.InputText(key="ELPTIM",size=(10,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text("{:<28}".format("PACKET COUNT")),
            sg.InputText(key="PKTCNT",size=(10,1),disabled=False,do_not_clear=True,justification='r')
        ],
        [
            sg.Text('',key='WARNING', justification='left', text_color="red"),
        ],
        [
            sg.Text('',key='CHECKSUM', justification='left', text_color="red"),
        ],
        [
            sg.Text('',key='STATUS', justification='left', text_color="red"),
        ],
        [
            sg.Text('',key='-time-', justification='left'),
        ],
        [
            sg.Button("EXIT"),
        ],
    ]

    # Display Ohio SSBN Submarine Image
    image_viewer_column = [
        [sg.Image("Trident.png")],	# Python 3
        #[sg.Image("OhioSub.gif")],	# Python 2
    ]

    # ----- SSDN Live Capture GUI layout -----
    layout = [
        [
            sg.Column(image_viewer_column),
            sg.VSeperator(),
            sg.Column(data_output_column),
        ]
    ]

    # Return Created Window
    return sg.Window("SSDN Live Capture Status",layout,finalize=True)
    # End setup_outputwindow() function

def run_capture(pkt_int_time):
    cnt=0
    pkt_cnt=0
    pkt_interr_cnt=0
    chksum_err_cnt=0
    status_err_cnt=0
    elapsed_time=1.0
    dist_var=10.0
    speed_var1=10.0
    speed_var2=10.0
    dlltim_var=0.0625
    maxtim_var=0.0625
    window.refresh()
    # Set initial default values for output fields
    # Display live capture results to output window
    #window['PARM1'].update('{:3.5f}'.format(EMWaterSpeed))
    #window['PARM2'].update('{:3.5f}'.format(BlendWaterSpeed))
    #window['PARM3'].update('{:3.5f}'.format(distance))
    #window['DLTTIM'].update('{:3.5f}'.format(deltatim))
    #window['MAXTIM'].update('{:3.5f}'.format(max_pkt_tim))
    #window['PKTCNT'].update(packet_counter)
    #window['ELPTIM'].update('{:3.5f}'.format(elapsed_tim))
    window['PARM1'].update('{:3.2f}'.format(10.0))
    window['PARM2'].update('{:3.2f}'.format(10.0))
    window['PARM3'].update('{:3.2f}'.format(dist_var))
    window['DLLTIM'].update('{:3.4f}'.format(dlltim_var))
    window['MAXTIM'].update('{:3.4f}'.format(maxtim_var))
    window['PKTCNT'].update(1)
    window['ELPTIM'].update('{:3.1f}'.format(elapsed_time))
    # create an event loop
    while True:
        # Update every second
        event, values = window.read(timeout=1000)
        # End program if user closes window or presses the EXIT button
        if event == "EXIT" or event == sg.WIN_CLOSE_ATTEMPTED_EVENT:
            capture_mode = False
            break
        cnt+=1
        if (cnt % 2):
            speed_var1+=rnd.random()
            speed_var2-=rnd.random()
        else:
            speed_var2 += rnd.random()
            speed_var1 -= rnd.random()
        # Reset variable each pass
        dlltim_var=0.625
        dist_var+=(1/3)
        dlltim_var += rnd.uniform(0,0.5)
        # Update maxtim value to maximum detected
        if (dlltim_var > maxtim_var):
            maxtim_var = dlltim_var
        # If current delta tim is over programmed limit update err count
        if (dlltim_var > pkt_int_time):
            pkt_interr_cnt += 1
            window['WARNING'].update('WARNING PACKET TIMEOUT DETECTED {:d} TIMES'.format(pkt_interr_cnt))
            if (pkt_interr_cnt % 5 == 0):
                chksum_err_cnt+=1
                window['CHECKSUM'].update('WARNING CHECKSUM ERROR DETECTED {:d} TIMES'.format(chksum_err_cnt))
            if (pkt_interr_cnt % 10 == 0):
                status_err_cnt+=1
                window['STATUS'].update('WARNING STATUS ERROR DETECTED {:d} TIMES'.format(status_err_cnt))
        elapsed_time+=1
        pkt_cnt+=16
        window['PARM1'].update('{:3.2f}'.format(speed_var1))
        window['PARM2'].update('{:3.2f}'.format(speed_var2))
        window['PARM3'].update('{:3.2f}'.format(dist_var))
        window['DLLTIM'].update('{:3.4f}'.format(dlltim_var))
        window['MAXTIM'].update('{:3.4f}'.format(maxtim_var))
        window['ELPTIM'].update('{:3.1f}'.format(elapsed_time))
        window['PKTCNT'].update(pkt_cnt)
        window['-time-'].update(clk())

    return()

'''
=====================================================================================================
# Upon operator selection of Checkbox for Setup GUI, update color, disable other checkboxes
=====================================================================================================
'''
def update_checkboxes(selection):
    if (selection == 'dhsyl1'):
        window["dhsyl1cb"].update(value=True) # Check on
        window["dhsyl1cb"].update(text_color="green")
    else:
        window["dhsyl1cb"].update(value=False) # Check off
        window["dhsyl1cb"].update(text_color="red")
    if (selection == 'dhsyl2'):
        window["dhsyl2cb"].update(value=True)
        window["dhsyl2cb"].update(text_color="green")
    else:
        window["dhsyl2cb"].update(value=False)
        window["dhsyl2cb"].update(text_color="red")
    if (selection == 'ddd1'):
        window["ddd1cb"].update(value=True)
        window["ddd1cb"].update(text_color="green")
    else:
        window["ddd1cb"].update(value=False)
        window["ddd1cb"].update(text_color="red")
    if (selection == 'ddd2'):
        window["ddd2cb"].update(value=True)
        window["ddd2cb"].update(text_color="green")
    else:
        window["ddd2cb"].update(value=False)
        window["ddd2cb"].update(text_color="red")
    if (selection == 'gyro'):
        window["gyrocb"].update(value=True)
        window["gyrocb"].update(text_color="green")
    else:
        window["gyrocb"].update(value=False)
        window["gyrocb"].update(text_color="red")
    if (selection == 'sdm'):
        window["sdmcb"].update(value=True)
        window["sdmcb"].update(text_color="green")
    else:
        window["sdmcb"].update(value=False)
        window["sdmcb"].update(text_color="red")
    if (selection == 'ndm'):
        window["ndmcb"].update(value=True)
        window["ndmcb"].update(text_color="green")
    else:
        window["ndmcb"].update(value=False)
        window["ndmcb"].update(text_color="red")
    # End update_checkboxes() function

# Setup filename in case operator does not select a file from the list for APPEND
filename = 'Subdata.csv'

# create window with programmed layout
#window = sg.Window("SSDN Live Capture Setup",layout)
window = sg.Window("SSDN Live Capture Setup", layout, enable_close_attempted_event=True, finalize=True)

# Set initial default values for input fields
window['CAPTIME'].update("10.0")	# Initial Capture time, 10 minutes
window['INTTIME'].update("16")		# Initial Interval timeout, 16 packet times missed (62.5 msec), 1 second
window['ETHPORT'].update("eth0")	# Ethernet Port

# create an event loop
while True:
    #Update every second
    event, values = window.read(timeout=1000)
    # End program if user closes window or presses the EXIT button
    if event == "EXIT" or event == sg.WIN_CLOSE_ATTEMPTED_EVENT:
        capture_mode = False
        break
    # Checkbox Handling Events
    if event == "dhsyl1cb":
        update_checkboxes("dhsyl1")
    if event == "dhsyl2cb":
        update_checkboxes("dhsyl2")
    if event == "ddd1cb":
        update_checkboxes("ddd1")
    if event == "ddd2cb":
        update_checkboxes("ddd2")
    if event == "gyrocb":
        update_checkboxes("gyro")
    if event == "sdmcb":
        update_checkboxes("sdm")
    if event == "ndmcb":
        update_checkboxes("ndm")
    if event == "csvcb":
        csv_out = False
    if event == "pcapcb":
        pcap_out = False
    if event == "START":
        #Capture Entered Data Values from InputText boxes
        #filesd.write(values['DHSYL1'])
        #filesd.write(",")
        #filesd.write(values['DDD1'])
        #filesd.write(",")
        #filesd.write(values['GYRO'])
        #filesd.write(",")
        # Convert pkt_int_time to seconds from packets
        int_time = values['INTTIME']
        pkt_int_time = float(int_time) * 0.0625		# 16 Hz packet rate, 62.5 milliseconds
        # Detect which sensor is selected
        if values['dhsyl1cb'] is True:
            sensor = "dhsyl1"
        if values['dhsyl2cb'] is True:
            sensor = "dhsyl2"
        if values['ddd1cb'] is True:
            sensor = "ddd1"
        if values['ddd2cb'] is True:
            sensor = "ddd2"
        if values['gyrocb'] is True:
            sensor = "gyro"
        if values['sdmcb'] is True:
            sensor = "sdm"
        if values['ndmcb'] is True:
            sensor = "ndm"
        window.close()
        now = datetime.now()
        window = setup_outputwindow("EMWTRSPD", "BLNDWSPD", "DISTANCE  ", sensor)
        # Dummy capture environment while loop
        run_capture(pkt_int_time)
        #d1 = now.strftime("%m/%d/%Y")
        #filesd.write(d1)
        #filesd.write(",")
        #d2 = now.strftime("%H:%M:%S")
        #filesd.write(d2)
        #filesd.write("\n")
        #Clear input text fields
        #window['DHSYL1'].update('')
        #window['DDD1'].update('')
        #window['GYRO'].update('')
    window['-time-'].update(clk())

window.close()
#filesd.close()
