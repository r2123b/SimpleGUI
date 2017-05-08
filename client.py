from Viewer import MyGUI
from Controller import Controller

# here is main function
if __name__ == '__main__':
    myGUI = MyGUI()  # init GUI
    myController = Controller(myGUI) #init Controller

    myController.startCrawler()
    myGUI.startGui()