import os
import tkinter
from tkinter import filedialog


root = tkinter.Tk()
root.withdraw()
cdir = os.getcwd()
gen_path = filedialog.askdirectory(parent = root, initialdir = cdir, title = 'Select directory where .trc files are located')
if len(gen_path)>0:
    print('You selected ',gen_path)


#print("I'm replacing marker headers")
replace_with = ['r should','l should','r asis','r bar 1','r knee 1','r bar 2',
'r mall','r heel','r met','l asis','l bar 1','l knee 1','l bar 2','l mall',
'l heel','l met']
find_this = ['r_should','l_should','r_asis','r_bar_1','r_knee_1','r_bar_2',
'r_mall','r_heel','r_met','l_asis','l_bar_1','l_knee_1','l_bar_2','l_mall',
'l_heel','l_met']
combined = zip(find_this,replace_with)


os.chdir(gen_path)
siz = list(range(0,len(find_this)))
#print(os.getcwd())
status = len(os.listdir(gen_path))
tick=0
#print(status)
for mark_files in os.listdir(gen_path):
    #print(mark_files)
    if '.trc' in  mark_files:
        tick+=1
        print(tick)
        if status==len(os.listdir(gen_path)):
            print('Replacing Headers')
        with open(gen_path + '\\' + mark_files) as m_file:
            new_f=m_file.read()
            for num in siz:
                new_f = new_f.replace(find_this[num],replace_with[num])
        with open(gen_path + '\\' + mark_files,"w") as m_file:
            m_file.write(new_f)
        status=status-1
        #print('i',status)
        continue
    elif status>1:
        status=status-1
        #print('e',status)
        continue
    elif status<=1:
        print('No .trc file found')
        break

if tick>1:
    print('Done')




""""""
