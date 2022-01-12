class Button:

    def __init__(self, num):

        self.num = num
    
    def seeSum(self):

        return self.num

myButton = Button(5)

print(myButton.seeSum())