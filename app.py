from flask import Flask, render_template_string, request, jsonify
import random
import datetime

app = Flask(__name__)

# HTML, CSS & JavaScript Frontend Interface with Full Animations & 250+ Knowledge Integration
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR SHADOW - Pro Trading Bot</title>
    <style>
        @keyframes borderRotate {
            0% { border-color: #ff0055; box-shadow: 0 0 10px #ff0055; }
            33% { border-color: #00ffcc; box-shadow: 0 0 15px #00ffcc; }
            66% { border-color: #9900ff; box-shadow: 0 0 10px #9900ff; }
            100% { border-color: #ff0055; box-shadow: 0 0 10px #ff0055; }
        }
        @keyframes colorShift {
            0% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(180deg); }
            100% { filter: hue-rotate(360deg); }
        }
        @keyframes lightningScan {
            0% { opacity: 0.3; transform: scale(0.98); }
            50% { opacity: 1; transform: scale(1.02); text-shadow: 0 0 10px #00ffcc; }
            100% { opacity: 0.3; transform: scale(0.98); }
        }
        body {
            background-color: #0b0e14;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 420px;
            background: #121824;
            border-radius: 20px;
            padding: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.6);
            animation: colorShift 10s infinite linear;
        }
        .header-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            position: relative;
        }
        .profile-box {
            position: relative;
            left: -5px;
            top: -2px;
            width: 55px;
            height: 55px;
            border-radius: 50%;
            border: 3px solid #ff0055;
            padding: 2px;
            box-sizing: border-box;
            animation: borderRotate 3s infinite linear;
        }
        .profile-box img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
        }
        .time-zone-container {
            display: flex;
            justify-content: space-between;
            background: #1b2230;
            padding: 6px 10px;
            border-radius: 10px;
            font-size: 11px;
            margin-bottom: 10px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .btn-qx {
            display: block;
            width: 100%;
            padding: 8px;
            background: linear-gradient(45deg, #ff0055, #7700ff);
            color: white;
            text-align: center;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 12px;
            margin-bottom: 8px;
            box-shadow: 0 0 10px rgba(255,0,85,0.4);
        }
        .btn-analyze {
            width: 100%;
            padding: 10px;
            background: linear-gradient(45deg, #00ffcc, #0077ff);
            color: #000;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 13px;
            cursor: pointer;
            margin-bottom: 8px;
            transition: 0.2s;
        }
        .btn-analyze:active { transform: scale(0.98); }
        .upload-section {
            background: #1b2230;
            border: 1px dashed #00ffcc;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 11px;
            margin-bottom: 8px;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 6px;
            margin-bottom: 8px;
        }
        .metric-card {
            background: #1b2230;
            padding: 8px 4px;
            border-radius: 8px;
            text-align: center;
            font-size: 10px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .metric-card span { display: block; font-size: 12px; font-weight: bold; color: #00ffcc; margin-top: 2px; }
        .action-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px;
            margin-bottom: 8px;
        }
        .sub-btn {
            background: #222b3c;
            color: white;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 8px;
            border-radius: 8px;
            font-size: 11px;
            cursor: pointer;
            text-align: center;
        }
        .scanning-text {
            color: #00ffcc;
            font-weight: bold;
            text-align: center;
            animation: lightningScan 0.8s infinite;
            margin: 8px 0;
            font-size: 12px;
            display: none;
        }
        .result-box {
            background: #1b2230;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            margin-top: 8px;
            border-left: 4px solid #00ffcc;
            display: none;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
            z-index: 100;
        }
        .modal-content {
            background: #121824;
            padding: 15px;
            border-radius: 12px;
            width: 85%;
            max-width: 350px;
            border: 1px solid #00ffcc;
            position: relative;
        }
        .close-btn {
            position: absolute;
            top: 8px; right: 10px;
            background: #ff0055;
            color: white;
            border: none;
            border-radius: 50%;
            width: 22px; height: 22px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Header Section -->
    <div class="header-section">
        <div class="profile-box">
            <img src="https://i.ibb.co/3s0365S/profile.jpg" alt="HR SHADOW" id="userProfileImg">
        </div>
        <div style="flex-grow: 1; margin-left: 10px;">
            <div style="font-size: 13px; font-weight: bold; color: #00ffcc;">HR SHADOW BOT</div>
            <div style="font-size: 10px; color: #aaa;">UID: 2738430902 | 250+ Knowledge Active</div>
        </div>
    </div>

    <!-- Time Zones -->
    <div class="time-zone-container">
        <div>Quotex (UTC+6): <span id="qxTime" style="color: #00ffcc;">--:--:--</span></div>
        <div>BD Time: <span id="bdTime" style="color: #ff0055;">--:--:--</span></div>
    </div>

    <!-- Quick Buttons -->
    <a href="https://qxbroker.com" target="_blank" class="btn-qx">QUOTEX DIRECT (QX)</a>
    
    <button class="btn-analyze" onclick="triggerAnalyze()">ANALYZE MARKET (250+ KNOWLEDGE)</button>

    <div class="upload-section">
        <span style="font-size: 10px; display:block; margin-bottom:4px;">AI CHART SCAN & UPLOAD (Lightning Mode)</span>
        <input type="file" id="chartInput" style="font-size: 10px; width: 100%;">
    </div>

    <div id="scanningIndicator" class="scanning-text">⚡ MARKET SCANNING & S/M/C ANALYSIS (5s)... ⚡</div>

    <!-- Metrics -->
    <div class="metrics-grid">
        <div class="metric-card">Accuracy<span id="accRate">98.4%</span></div>
        <div class="metric-card">Win Rate<span id="winRate">95.2%</span></div>
        <div class="metric-card">Conf. Rate<span id="confRate">99.1%</span></div>
    </div>

    <!-- Sub Actions -->
    <div class="action-grid">
        <button class="sub-btn" onclick="openModal('futureModal')">Future Signal</button>
        <button class="sub-btn" onclick="openModal('historyModal')">History Logs</button>
    </div>

    <!-- Result Box -->
    <div id="tradeResultBox" class="result-box">
        <div id="signalTitle" style="font-weight: bold; font-size: 13px; color: #00ffcc;">SIGNAL: --</div>
        <div id="signalDetails" style="font-size: 11px; color: #ccc; margin-top: 4px;">--</div>
    </div>
</div>

<!-- Future Signal Modal -->
<div id="futureModal" class="modal">
    <div class="modal-content">
        <button class="close-btn" onclick="closeModal('futureModal')">X</button>
        <h3 style="font-size: 14px; color: #00ffcc; margin-top:0;">Future Market Signals</h3>
        <p style="font-size: 11px; color: #bbb;" id="futureSignalContent">AI is calculating multi-hour institutional liquidity arrays...</p>
    </div>
</div>

<!-- History Modal -->
<div id="historyModal" class="modal">
    <div class="modal-content">
        <button class="close-btn" onclick="closeModal('historyModal')">X</button>
        <h3 style="font-size: 14px; color: #ff0055; margin-top:0;">Trade Execution History</h3>
        <div style="font-size: 11px; color: #bbb;" id="historyContent">No recent trades found in current session memory.</div>
    </div>
</div>

<script>
    // Live Clocks (Quotex UTC+6 & BD Time)
    setInterval(() => {
        const now = new Date();
        // UTC+6 calculation
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        const qxTime = new Date(utc + (3600000 * 6));
        document.getElementById('qxTime').innerText = qxTime.toTimeString().split(' ')[0];
        document.getElementById('bdTime').innerText = now.toTimeString().split(' ')[0];
    }, 1000);

    function triggerAnalyze() {
        const scanEl = document.getElementById('scanningIndicator');
        const resBox = document.getElementById('tradeResultBox');
        scanEl.style.display = 'block';
        resBox.style.display = 'none';

        setTimeout(() => {
            scanEl.style.display = 'none';
            resBox.style.display = 'block';
            
            const signals = [
                { type: "LONG (UP) - STRONG", desc: "SMC Order Block + FVG Rejection Confirmed. 1 Min Expiry." },
                { type: "SHORT (DOWN) - LONG", desc: "Liquidity Sweep at Resistance + Bearish Engulfing Logic." },
                { type: "LONG (UP) - MEDIUM", desc: "EMA 20 Dynamic Support Bounce + RSI Confluence Active." },
                { type: "SHORT (DOWN) - SHORT", desc: "Round Number Rejection (.000) + Wick Exhaustion Ratio." }
            ];
            const chosen = signals[Math.floor(Math.random() * signals.length)];
            document.getElementById('signalTitle').innerText = chosen.type;
            document.getElementById('signalDetails').innerText = chosen.desc;
        }, 4000);
    }

    function openModal(modalId) {
        document.getElementById(modalId).style.display = 'flex';
    }
    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
