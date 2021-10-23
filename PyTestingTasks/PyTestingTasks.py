import datetime
import psutil
import subprocess
#import time


def addlog(file, message):
    file.write("[" + str(datetime.datetime.now()) + "]: ")
    file.write(message)
    file.write("\n")


def logging():
    print("Good11")
    targetProcess = psutil.Process().children()[0]
    file = open(targetProcess.name() + ".txt", 'a')
    print("Good12")
    addlog(file, "==========Start Logging==========")
    print("Good13")
    addlog(file, targetProcess.cpu_percent())
    print("Good14")
    addlog(file, targetProcess.memory_info()[0])
    print("Good15")
    addlog(file, targetProcess.memory_info()[1])
    print("Good16")
    addlog(file, targetProcess.num_handles())
    print("Good17")
    file.close()
    print("Good18")


def printStartResurseInfoMain():
    print (psutil.cpu_percent()) #CUP в процентах
    print (psutil.virtual_memory()) #Виртуальная память
    print (dict(psutil.virtual_memory()._asdict())["total"])
    print (psutil.virtual_memory().percent) #Виртуальная память в процентах
    print (psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) #Процент доступной виртуальной памяти (обратное)


def printResurseInfo(target):
    print(target.cpu_percent())
    print(target.memory_full_info())
    print(target.memory_percent())


def start_procces():
    printStartResurseInfoMain()

    print("Enter path to programe (tromble):\n")
    process_path = input()
    process_path = "D:\Game\Warcraft 3 Frozen Throne\Frozen Throne.exe" #"D:\Game\Warcraft 3 Frozen Throne\Frozen Throne.exe"
    procces = subprocess.Popen(process_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #time.sleep(2)
    print("Good1")

    print("Good2")
    logging()
    print("Good3")
    #printResurseInfo()


if __name__ == '__main__':
    start_procces()