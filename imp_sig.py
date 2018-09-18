from asammdf import MDF
import sys
import matplotlib.pyplot as plt
mdf = MDF('Dauerzeitschrieb_20171218_053831.mf4',memory = 'full')

sig_list = []
while 1:
    choice_1 = input("Do you want to add a signal?(y/n)\n")
    if choice_1 == "n":
        if len(sig_list) > 0:
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
        break
    elif choice_1 == "y":
        sig_name = input("Enter exact Signal name\n")
        sig_list.append(sig_name)

plt.show()
print ("Complete")
print(sig_list)