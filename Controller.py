import _thread
import time


class Controller:
    def __init__(self, myGUI):
        self._myGUI = myGUI

    def startCrawler(self):
        try:
            _thread.start_new_thread(self.crawler, ())
        except:
            print("Error: unable to start thread")

    def crawler(self):
        i = 0
        j = 0
        while True:
            time.sleep(0.5)  # unit = second, delay time
            self.notifyGuiChange(i, j)
            i += 1
            j -= 1


    def notifyGuiChange(self, Max, min):
        self._myGUI.updateGUI(Max, min)
