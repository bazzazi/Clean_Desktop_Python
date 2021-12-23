from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time, os, pyttsx3

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.speech("file detected")
        for filename in os.listdir(first_path):
            first_file_path = first_path + "/" + filename
            second_file_path = second_path + "/" + filename
            os.rename(first_file_path, second_file_path)
            self.speech("file moved successfully")

    def speech(self, value):
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.say(value)
        engine.runAndWait()


first_path = "C:/Users/Mohammad Ali Bazzazi/Desktop/first"
second_path = "C:/Users/Mohammad Ali Bazzazi/Desktop/second"

fileHandler = FileHandler()
observer = Observer()

observer.schedule(fileHandler, first_path, recursive=True)
observer.start()

try:
    while 1:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

