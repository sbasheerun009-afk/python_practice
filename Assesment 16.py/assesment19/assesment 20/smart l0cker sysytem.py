class SmartLocker:
    def __init__(self,LockerId,ownerName,pin):
        self.LockerId = LockerId
        self.ownername = ownerName
        self.__pin = pin
        self.__Accesscount = 0
    def verifypin(self,pin):
         return self.__pin == pin
    def LockerAccess(self,pin):
        if self.__pin == pin:
            self.__Accesscount += 1
            print("access granted")
        else:
            print("access deniend")
    def ChangePin(self,oldpin,newpin):
        if self.verifypin(oldpin):
            self.__pin = newpin
    def view_details(self):
        print("Locker ID:", self.LockerId)
        print("Owner Name:", self.ownername)

    def get_access_count(self, pin):
        if self.verifypin(pin):
            print("Access Count:", self.get_access_count)
        else:
            print("Incorrect PIN")
locker = SmartLocker("shaik123", "Basheerun", "pass1234")

locker.LockerAccess("pass1234")     # Correct PIN
locker.LockerAccess("pass1111")     # Wrong PIN

locker.view_details()

locker.ChangePin("pass1234", "pass5678")

locker.LockerAccess("pass5678")

locker.get_access_count("pass5678")