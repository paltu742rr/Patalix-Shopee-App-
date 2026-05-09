// Patalix Shopee App - Logic
function unlockApp() {
    const pinInput = document.querySelector('input[type="password"]').value;
    const correctPin = "2027"; // तुम्हारा तय किया हुआ पिन

    if (pinInput === correctPin) {
        alert("Patalix Shopee अनलॉक हो गया!");
        window.location.href = "product.html"; // सही पिन पर प्रोडक्ट पेज पर ले जाएगा
    } else {
        alert("गलत पिन! कृपया फिर से कोशिश करें।");
    }
}

// बटन क्लिक होने पर फंक्शन चलाएं
document.querySelector('.btn-blue').addEventListener('click', unlockApp);

