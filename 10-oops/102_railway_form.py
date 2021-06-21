class RailwayForm:
    formType = "Railway Form"
    def printData(self):
        print("Name is: ", self.name)
        print("Train is: ", self.train)

myApplication = RailwayForm()
myApplication.name = "Suraj"
myApplication.train = "Rajdhani Express"
myApplication.printData()