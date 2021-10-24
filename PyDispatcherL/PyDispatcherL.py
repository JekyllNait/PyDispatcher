import datetime
import psutil
import subprocess
import time


class Dispatcher:
    def __init__(self) -> None:
        self.logger = Logger()

    def start_procces(self) -> None:
        print("Enter path to programe (tromble):")
        commands = input().split("-")
        process_path = commands.pop(0).strip()
        for command in commands:
            command_pair = command.strip().split(" ")
            self._process_command(command_pair[0], command_pair[1])
        procces = subprocess.Popen(process_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.logger.run()

    def _process_command(self, command, parametr) -> None:
        if command == "ti":
            self.logger.polling_interval = float(parametr)
        elif command == "lf":
            self.logger.log_file_path = parametr


class Logger:
    def __init__(self, polling_interval = 0.5, log_file_path = "logs.txt") -> None:
        self.polling_interval = polling_interval
        self.log_file_path = log_file_path

    def _add_note(self, message) -> None:
        self.log_file.write("[" + str(datetime.datetime.now()) + "]")
        self.log_file.write(str(message))
        self.log_file.write("\n")

    def run(self) -> None:
        self.log_file = open(self.log_file_path, 'a')
        targetProcess = psutil.Process().children()[0]
        while (targetProcess.is_running()):
            print("!")
            #add_note(fileL, "CPU")
            #add_note(fileL, "RSS")
            #add_note(fileL, "VMS")
            #add_note(fileL, "NUM_HANDLE")
            message = "|CPU: " + str(targetProcess.cpu_percent()) + "|RSS: " + str(targetProcess.memory_info()[0]) + "|VMS: " + str(targetProcess.memory_info()[1]) + "|N_H: " + str(targetProcess.num_handles())

            self._add_note(message)
            time.sleep(self.polling_interval)
        self.log_file.close()


if __name__ == '__main__':
    dispatcher = Dispatcher()
    dispatcher.start_procces()