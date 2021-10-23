import datetime
import psutil
import subprocess
import time


def add_note(fileL, message):
    fileL.write("[" + str(datetime.datetime.now()) + "]: ")
    fileL.write(str(message))
    fileL.write("\n")


def logging():
    fileL = open("Testlog.txt", 'a')
    targetProcess = psutil.Process().children()[0]
    while (True):
        print("!")
        #add_note(fileL, "CPU")
        #add_note(fileL, "RSS")
        #add_note(fileL, "VMS")
        #add_note(fileL, "NUM_HANDLE")
        message = "|CPU: " + str(targetProcess.cpu_percent()) + "|RSS: " + str(targetProcess.memory_info()[0]) + "|VMS: " + str(targetProcess.memory_info()[1]) + "|N_H: " + str(targetProcess.num_handles())

        add_note(fileL, message)
        time.sleep(0.1)
    fileL.close()


def print_start_resurse_info_main():
    print (psutil.cpu_percent()) #CUP в процентах
    print (psutil.virtual_memory()) #Виртуальная память
    print (dict(psutil.virtual_memory()._asdict())["total"])
    print (psutil.virtual_memory().percent) #Виртуальная память в процентах
    print (psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) #Процент доступной виртуальной памяти (обратное)


def print_resurse_info(target):
    print(target.cpu_percent())
    print(target.memory_full_info())
    print(target.memory_percent())


def start_procces():
    print_start_resurse_info_main()

    print("Enter path to programe (tromble):")
    process_path = "notepad.exe"
    procces = subprocess.Popen(process_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging()


if __name__ == '__main__':
    start_procces()