import os
print("I'm replacing marker headers")
finders = ['r should','l should','r asis','r bar 1','r knee 1','r bar 2',
'r mall','r heel','r met','l asis','l bar 1','l knee 1','l bar 2','l mall',
'l heel','l met']
replacers = ['r_should','l_should','r_asis','r_bar_1','r_knee_1','r_bar_2',
'r_mall','r_heel','r_met','l_asis','l_bar_1','l_knee_1','l_bar_2','l_mall',
'l_heel','l_met']
combined = zip(finders,replacers)

gen_path = "G:"+"\\"+"GRF"+"\\"+"jawan data"+"\\"+"CompiledGRF"
os.chdir(gen_path)
siz = list(range(0,len(finders)))
print(os.getcwd())
for fold in os.listdir(gen_path):
        if mark_files.find('.trc')>0:
            with open(gen_path + '\\' + fold + '\\' + mark_files) as m_file:
                new_f=m_file.read()
                for num in siz:
                    new_f = new_f.replace(finders[num],replacers[num])

            with open(gen_path + '\\' + fold + '\\' + mark_files,"w") as m_file:
                m_file.write(new_f)
            continue
        else:
            continue
print("Done with all files")
