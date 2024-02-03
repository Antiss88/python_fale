#Норм код
class Calculator:
    last_res =  None
    def sum(self,a1,a2):
        self.last_res = a1 + a2
        return a1 + a2
    def print_last_res(self):
        print(self.last_res)





