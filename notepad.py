from asammdf import MDF
import sys
import matplotlib.pyplot as plt
mdf = MDF('Dauerzeitschrieb_20171218_053831.mf4',memory = 'full')
sig_list = []
# file = open('data.txt', 'r')
name = input("Give the file name\n")
name = name + '.txt'
try:
    file = open(name, 'r')
except:
    print("No such file found.")
while 1:
    try:
        sig_list = file.read().split('\n')
        print(sig_list)
        if len(sig_list) >= 0:
            filter = mdf.filter(sig_list)
            file_name = input("Enter the file name to be saved\n")
            filter.convert('4.10').save(file_name+'.mf4')
            mdf_new = MDF((file_name+'.mf4'), memory = 'full')
            data_frame = mdf_new.export('pandas' , filename = file_name )
            data_frame.to_csv(file_name+'.csv')
            print("CSV and mf4 file created.\n")
            choice_2 = input("Do you want to plot the signal(s)?(y/n)\n")
            if choice_2 == "y":
                for i in range(len(sig_list)):
                    plt.figure(i)
                    plt.xlabel('Time [s]')
                    plt.ylabel('[{}]'.format(mdf.get(sig_list[i]).unit))
                    plt.plot(mdf.get(sig_list[i]).timestamps, mdf.get(sig_list[i]).samples, 'b')
                    plt.plot(mdf.get(sig_list[i]).timestamps, mdf.get(sig_list[i]).samples, 'b.')
                    plt.grid(True)
    except:
        break

plt.show()
print ("Complete")
# print(sig_list)