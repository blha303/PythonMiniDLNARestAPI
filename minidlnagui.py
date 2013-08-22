# Run this on a client machine (not the media server)
# This is my first GUI!
 
# Copyright 2013 Steven Smith (blha303). All Rights Reserved.
# New BSD license
# http://www.opensource.org/licenses/BSD-3-Clause
 
from Tkinter import *
import tkMessageBox
import requests
import json
 
hostname = "home.blha303.com.au"
port = "5000"
url = "http://%s:%s/api/DETAILS" % (hostname, port if port else "5000")
fields = ['ARTIST', 'ID', 'PATH', 'SIZE', 'TIMESTAMP', 'TITLE', 'DURATION', 'BITRATE',
          'SAMPLERATE', 'CREATOR', 'ALBUM', 'GENRE', 'COMMENT', 'CHANNELS', 'DISC',
          'TRACK', 'DATE', 'RESOLUTION', 'THUMBNAIL', 'ALBUM_ART', 'ROTATION',
          'DLNA_PN', 'MIME']
 
def search(term, name='artist'):
    url = "http://home.blha303.com.au:5000/api/DETAILS"
    headers = {'Content-Type': 'application/json'}
    filters = [dict(name=name.upper(), op='like', val=term)]
    params = dict(q=json.dumps(dict(filters=filters)))
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    return response.json()
 
master = Tk()
windows = PanedWindow()
windows.pack(fill=BOTH, expand=1)
textbox = Text(windows)
windows.add(textbox)
rightside = PanedWindow(windows, orient=VERTICAL)
windows.add(rightside)
top = Entry(rightside)
rightside.add(top)
middle = Listbox(rightside)
x = 1
for i in fields:
    middle.insert(x, i)
    x += 1
 
rightside.add(middle)
 
def buttonCallback():
    term = top.get()
    name = middle.get(middle.curselection() if middle.curselection() else 0)
    data = search(term, name=name)
    textbox.delete(1.0, END)
    if data['num_results'] == 0:
        textbox.insert(INSERT, str(data))
        return
    else:
        output = []
        for i in data['objects']:
            if str(i['PATH']) != "None":
                output.append("PATH: " + str(i['PATH']))
                for a in fields:
                    if a != "PATH":
                        output.append("  " + a + ": " + str(i[a]))
                output.append("")
        textbox.insert(INSERT, "\n".join(output))
 
bottom = Button(rightside, text="Submit", command=buttonCallback)
rightside.add(bottom)
mainloop()
