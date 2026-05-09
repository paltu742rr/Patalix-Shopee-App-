import os

project_files = {
    # 1. मुख्य चेहरा (Login & PIN)
    "index.html": """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Patalix Shopee - Lock</title>
    <style>
        body { background: #ffffff; text-align: center; font-family: sans-serif; padding-top: 100px; }
        .app-card { border: 2px solid #003399; display: inline-block; padding: 30px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        input { padding: 10px; font-size: 18px; width: 100px; text-align: center; border-radius: 5px; border: 1px solid #ccc; }
        .btn { background: #003399; color: white; border: none; padding: 12px 25px; border-radius: 8px; margin-top: 20px; cursor: pointer; font-size: 16px; }
    </style>
</head>
<body>
    <div class="app-card">
        <h1 style="color: #003399;">Patalix Shopee</h1>
        <p><b>ज़ारा:</b> नमस्ते गौरव! अपना PIN डालें:</p>
        <input type="password" id="userPin" placeholder="****" maxlength="4">
        <br>
        <button class="btn" onclick="verify()">Unlock App</button>
    </div>

    <script>
        function verify() {
            const pin = document.getElementById('userPin').value;
            if(pin === "2027") { 
                alert("पिन सही है! स्वागत है गौरव।");
                window.location.href = "product.html"; 
            } else { 
                alert("गलत पिन! फिर से कोशिश करें।"); 
            }
        }
    </script>
</body>
</html>
""",

    # 2. प्रोडक्ट पेज (EMI & Flipkart Data)
    "product.html": """
<!DOCTYPE html>
<html>
<head>
    <title>Motorola Edge 50 - Patalix</title>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .container { max-width: 500px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 15px; }
        .price { color: #2874f0; font-size: 28px; font-weight: bold; }
        .emi { background: #f1f8ff; padding: 10px; border-radius: 5px; border-left: 5px solid #003399; margin: 15px 0; }
        .buy-now { background: #fb641b; color: #fff; border: none; padding: 15px; width: 100%; font-size: 18px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Motorola Edge 50 Pro (64MP)</h2>
        <p class="price">₹29,999</p>
        <div class="emi">
            <b>EMI Offer:</b> ₹2,500/month for 12 months (No-cost EMI available)
        </div>
        <p style="color: #0084ff;"><i>ज़ारा: "गौरव, यह फोन मुजफ्फरपुर हब पर उपलब्ध है!"</i></p>
        <button class="buy-now" onclick="window.location.href='tracking.html'">अभी खरीदें (Track Order)</button>
    </div>
</body>
</html>
""",

    # 3. ट्रैकिंग पेज (Live Location)
    "tracking.html": """
<!DOCTYPE html>
<html>
<body style="font-family: sans-serif; padding: 30px; text-align: center;">
    <h2 style="color: #003399;">Order Status</h2>
    <div style="font-size: 50px;">🚚</div>
    <p style="font-size: 20px;">स्थिति: <b>मुजफ्फरपुर हब</b></p>
    <hr>
    <p><b>ज़ारा का अपडेट:</b> गौरव, सामान आपके शहर पहुँच चुका है।</p>
    <button onclick="window.location.href='index.html'" style="padding: 10px;">Logout</button>
</body>
</html>
""",

    # 4. बैकएंड दिमाग (Python Logic)
    "main.py": """
import json

def load_user_data():
    with open('data.json', 'r') as f:
        return json.load(f)

def run_app():
    data = load_user_data()
    print(f"Patalix Shopee System Active for {data['user']} in {data['city']}")
    print("Zara AI is ready to fetch Flipkart API data...")

if __name__ == "__main__":
    run_app()
""",

    # 5. यूज़र डेटा
    "data.json": """
{
    "user": "Gaurav Kumar",
    "city": "Muzaffarpur",
    "app_version": "1.0.0",
    "target_exam": "Bihar Board 2027"
}
"""
}

def build_app():
    print("🔥 Patalix Shopee: Full System Build Shuru...")
    for filename, content in project_files.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ {filename} [OK]")
    print("\n🎉 मुबारक हो गौरव! पूरा ऐप और उसका दिमाग तैयार है।")
    print("👉 अब 'index.html' को ब्राउज़र में खोलें।")

if __name__ == "__main__":
    build_app()
  
