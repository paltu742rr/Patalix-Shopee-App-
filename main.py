# Patalix Shopee App - Main Entry Point
from security import PatalixLock
from zara_ai import ZaraAssistant

def start_app():
    # 1. सुरक्षा (PIN Lock)
    lock = PatalixLock("2027") # तुम्हारा 12th Board का साल पासवर्ड है
    print("--- Welcome to Patalix Shopee ---")
    
    pin = input("अपना 4-अंकों का PIN डालें: ")
    
    if lock.unlock_app(pin):
        # 2. अगर अनलॉक हो गया, तो ज़ारा आएगी
        zara = ZaraAssistant("Gaurav")
        zara.welcome_user()
        
        # 3. नकली डेटा (बाद में यहाँ असली API आएगी)
        fake_api_data = {"name": "Motorola Edge 50", "price": "27,999"}
        zara.process_request(fake_api_data)
    else:
        print("एक्सेस मना है! सही पिन डालें।")

if __name__ == "__main__":
    start_app()

