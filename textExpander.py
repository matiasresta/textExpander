class TextExpander:

    def __init__(self):
        self.active = False

    def textExpand(self, database):
        if self.active:
            from pynput.keyboard import Listener, Key, Controller
            import os
            controller = Controller()

            try:
                os.remove(os.path.join(os.getcwd(), "text.txt"))
            except:
                pass


            def writeToFile(key):

                key = str(key)
                if key == "Key.space":
                        key = " "
                if len(key) == 3:
                    key = key[1]

                with open("text.txt", "a") as textFile:
                    if len(key) == 1:
                        #print(key)
                        textFile.write(',' + key)
                        if key == "Key.space":
                            textFile.close()

                with open("text.txt", "r") as textFile:
                        data = textFile.read()[1:].split(",")
                        textLen = len(data)
                        comm = "".join(data[-3:])

                        if comm in database:
                            controller.release(Key.backspace); controller.press(Key.backspace)
                            controller.release(Key.backspace); controller.press(Key.backspace)
                            controller.release(Key.backspace); controller.press(Key.backspace)
                            controller.type(database[comm])
                            textFile.close()
                            os.remove(os.path.join(os.getcwd(), "text.txt"))

                        if textLen > 3000:
                            textFile.close()
                            os.remove(os.path.join(os.getcwd(), "text.txt"))

                        if comm == "qqq":
                            textFile.close()
                            os.remove(os.path.join(os.getcwd(), "text.txt"))
                            self.active = False
                            exit()

                        if not self.active:
                            exit()

            with Listener(on_press=writeToFile) as l:
                l.join()
        else:
            exit()