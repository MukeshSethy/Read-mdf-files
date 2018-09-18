from asammdf import MDF
mdf = MDF('Dauerzeitschrieb_20171218_053831.mf4',memory = 'full')
i = 0
j = 0
while 1:
    try:
        mdf.get_channel_name(i,j)
        while 1: 
            try:
                print(mdf.get_channel_name(i,j))
                j = j + 1
            except:
                break
        i = i + 1
        j = 0
    except:
        break
print("Complete")