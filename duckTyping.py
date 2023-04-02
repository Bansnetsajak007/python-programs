class vscode:
     def execute(self):
        print("compiling the code...")


class pycharm:
    def execute(self):
        print("Running..")
        print("Checking errors..")
        print("compiling the code...")

class machine:
    def run(self,ide):
        ide.execute()


vs=vscode()
py=pycharm()
obj=machine()  #instance of class machine
obj2 = machine();

obj.run(py)
obj2.run(vs)