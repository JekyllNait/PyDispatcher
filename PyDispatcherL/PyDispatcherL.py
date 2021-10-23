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
    for i in range(10):
        print("!")
        add_note(fileL, "CPU")
        add_note(fileL, "RRS")
        add_note(fileL, "TRS")
        add_note(fileL, "NUM_HANDLE")
        #       add_note(fileL, str(targetProcess.cpu_percent()))
        #       add_note(fileL, str(targetProcess.memory_info()[0]))
        #       add_note(fileL, str(targetProcess.memory_info()[1]))
        #       add_note(fileL, str(targetProcess.num_handles()))
        time.sleep(1)
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
    process_path = "D:\Game\Warcraft 3 Frozen Throne\Frozen Throne.exe" #"D:\Game\Warcraft 3 Frozen Throne\Frozen Throne.exe"
    procces = subprocess.Popen(process_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging()


if __name__ == '__main__':
    start_procces()