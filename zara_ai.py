# Patalix Shopee App - Smart Zara AI (API Ready)

class ZaraAssistant:
    def __init__(self, user_name="Gaurav"):
        self.user_name = user_name

    def process_request(self, api_data=None):
        # अगर API से डेटा नहीं आया (अभी के लिए)
        if api_data is None:
            print("[Zara]: मैं अभी फ्लिपकार्ट से जुड़ने की कोशिश कर रही हूँ...")
        else:
            # जब API से असली डेटा आएगा, तब ज़ारा इसे इस्तेमाल करेगी
            print(f"[Zara]: गौरव, मुझे फ्लिपकार्ट पर '{api_data['name']}' मिला है।")
            print(f"[Zara]: इसका दाम ₹{api_data['price']} है। क्या मैं इसे आर्डर कर दूँ?")

# भविष्य में जब हम API लाएंगे, तो ज़ारा ऐसे काम करेगी:
# test_data = {"name": "Motorola G54", "price": "14,999"}
# zara.process_request(test_data)
