# Patalix Shopee App - Security Module
# GPay style PIN protection system

class PatalixLock:
    def __init__(self, user_pin="1234"):
        self.correct_pin = user_pin
        self.locked = True

    def unlock_app(self, entered_pin):
        if entered_pin == self.correct_pin:
            self.locked = False
            print("Patalix Shopee Unlocked! Welcome Gaurav.")
            return True
        else:
            print("Wrong PIN! Bintu-Free Smart Guard is watching.")
            return False

# Testing the lock
app_lock = PatalixLock("2027") # Tum apna saal ya koi bhi 4-digit rakh sakte ho
print("--- Patalix Shopee App Security ---")
entered = input("Enter your 4-digit PIN: ")
app_lock.unlock_app(entered)
