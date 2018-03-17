import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
from selenium import webdriver

driver_profile = webdriver.FirefoxProfile()
driver_profile.set_preference('browser.privatebrowsing.autostart', True)
driver = webdriver.Firefox(firefox_profile=driver_profile)
driver.get(sys.argv[1])

class MyHandler(FileSystemEventHandler):
    def dispatch(self, event):
        driver.refresh()
        print event.src_path

if __name__ == "__main__":
    path = sys.argv[2]
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
