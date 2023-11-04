from abc import abstractmethod,ABC
class UserInterface(ABC):
    @abstractmethod
    def display(self,input):
        pass
class ConsoleUserInterface(UserInterface):
    def display(self,input):
        print(input)
class GUIUserInterface(UserInterface):
    def display(self,input):
        #реалізація графічного виводу інформації
        pass
