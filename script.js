document.getElementById('loginBtn').addEventListener('click', function() {
    const pin = document.getElementById('userPin').value;
    const correctPin = "2027"; 

    // Fake Database (Asli mein hum ise data.json se layenge)
    const db = {
        "2027": "Gaurav Kumar"
    };

    if (pin === correctPin) {
        const userName = db[pin];
        document.getElementById('zara-text').innerText = `नमस्ते ${userName}! सिस्टम अनलॉक हो रहा है...`;
        document.getElementById('zara-text').style.color = "#0047AB";
        
        // 1.5 second baad product page par bhej dega
        setTimeout(() => {
            window.location.href = "product.html";
        }, 1500);
    } else {
        alert("ACCESS DENIED: पिन गलत है।");
        document.getElementById('userPin').value = "";
    }
});
