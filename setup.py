import os

# Patalix Shopee App के लिए फाइलों का डेटा
files_data = {
    "security.py": """
# Security System
def check_pin(pin):
    return pin == "2027"
""",
    "zara_ai.py": """
# Zara AI Brain
def welcome():
    return "नमस्ते गौरव! मैं ज़ारा हूँ।"
""",
    "index.html": """
<!DOCTYPE html>
<html>
<body style="background:#fff; text-align:center;">
    <h1 style="color:#003399;">Patalix Shopee</h1>
    <p>ज़ारा: अपना PIN डालें</p>
    <input type="password" id="pin">
    <button style="background:#003399; color:#fff;">Unlock</button>
</body>
</html>
""",
    "tracking.html": """
<!DOCTYPE html>
<html>
<body>
    <h2>Tracking: मुजफ्फरपुर हब</h2>
    <p>ज़ारा: आपका फोन पहुँच गया है!</p>
</body>
</html>
"""
}

def create_files():
    print("Patalix Shopee की फाइलें बन रही हैं...")
    for name, content in files_data.items():
        with open(name, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ {name} बन गई!")

if __name__ == "__main__":
    create_files()

