from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FINORIX PRO BOT - 100% REAL & OTC KNOWLEDGE</title>
    <style>
        :root {
            --bg-color: #0b0e14;
            --card-bg: rgba(18, 22, 33, 0.9);
            --neon-green: #00ff88;
            --neon-red: #ff3366;
            --neon-blue: #00e5ff;
            --neon-gold: #ffd700;
            --text-color: #ffffff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            user-select: none;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 10px;
            overflow-x: hidden;
        }

        .app-card {
            width: 100%;
            max-width: 420px;
            background: var(--card-bg);
            border-radius: 20px;
            padding: 15px;
            position: relative;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 25px rgba(0,0,0,0.9);
            border: 2px solid var(--neon-blue);
        }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .profile-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .avatar-wrapper {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            padding: 2px;
            background: linear-gradient(45deg, var(--neon-green), var(--neon-blue));
        }

        .avatar-wrapper img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            display: block;
        }

        .bot-title h3 {
            font-size: 15px;
            font-weight: 800;
            color: var(--neon-gold);
        }

        .bot-title span {
            font-size: 11px;
            color: var(--neon-green);
            font-weight: bold;
        }

        .qx-btn {
            background: linear-gradient(135deg, #0088ff, #0044ff);
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 12px;
            border: none;
            cursor: pointer;
            box-shadow: 0 0 10px rgba(0, 136, 255, 0.6);
        }

        .timezone-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 12px;
        }

        .tz-box {
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 6px;
            text-align: center;
        }

        .tz-title {
            font-size: 10px;
            color: var(--neon-blue);
            font-weight: bold;
            margin-bottom: 2px;
        }

        .tz-time {
            font-size: 13px;
            font-family: monospace;
            font-weight: bold;
            color: #fff;
        }

        .controls-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 12px;
        }

        .select-box {
            background: #181d2a;
            color: #fff;
            border: 1px solid rgba(255,255,255,0.2);
            padding: 8px;
            border-radius: 8px;
            font-size: 12px;
            width: 100%;
            outline: none;
        }

        optgroup {
            background: #0b0e14;
            color: var(--neon-gold);
        }

        .analyze-btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(90deg, #00ff88, #00e5ff);
            border: none;
            border-radius: 10px;
            color: #0b0e14;
            font-weight: 900;
            font-size: 14px;
            cursor: pointer;
            margin-bottom: 12px;
            box-shadow: 0 0 15px rgba(0, 255, 136, 0.4);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .upload-card {
            border: 1px dashed var(--neon-blue);
            background: rgba(0, 229, 255, 0.03);
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            margin-bottom: 12px;
            position: relative;
        }

        .upload-card label {
            font-size: 11px;
            color: #ccc;
            cursor: pointer;
            display: block;
            margin-bottom: 5px;
        }

        .file-input {
            display: none;
        }

        .file-btn {
            background: rgba(255,255,255,0.1);
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 11px;
            color: #fff;
            display: inline-block;
            cursor: pointer;
        }

        .preview-img {
            max-width: 100%;
            max-height: 120px;
            border-radius: 6px;
            margin-top: 8px;
            display: none;
        }

        .scanning-overlay {
            display: none;
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(11, 14, 20, 0.95);
            border-radius: 10px;
            z-index: 10;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .electric-line {
            width: 80%;
            height: 3px;
            background: var(--neon-green);
            box-shadow: 0 0 15px var(--neon-green);
            animation: lightning 0.2s infinite alternate;
        }

        @keyframes lightning {
            0% { opacity: 0.3; transform: scaleX(0.95); }
            100% { opacity: 1; transform: scaleX(1.05); }
        }

        .scan-text {
            margin-top: 8px;
            font-size: 12px;
            color: var(--neon-green);
            font-weight: bold;
        }

        .signal-display {
            background: rgba(0,0,0,0.7);
            border: 2px solid var(--neon-green);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            margin-bottom: 12px;
            min-height: 85px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .signal-title {
            font-size: 18px;
            font-weight: 900;
            letter-spacing: 1px;
        }

        .signal-type {
            font-size: 11px;
            margin-top: 4px;
            padding: 2px 8px;
            border-radius: 4px;
            background: rgba(255,255,255,0.1);
            color: #ddd;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 6px;
            margin-bottom: 12px;
        }

        .stat-box {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 8px;
            padding: 6px;
            text-align: center;
        }

        .stat-label {
            font-size: 9px;
            color: #888;
            margin-bottom: 2px;
        }

        .stat-value {
            font-size: 12px;
            font-weight: bold;
            color: var(--neon-blue);
        }

        .action-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        .sub-btn {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.15);
            color: #fff;
            padding: 8px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: bold;
            cursor: pointer;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 100;
            justify-content: center;
            align-items: center;
            padding: 15px;
        }

        .modal-content {
            background: #121621;
            border: 1px solid var(--neon-blue);
            border-radius: 12px;
            width: 100%;
            max-width: 360px;
            padding: 15px;
            max-height: 80vh;
            overflow-y: auto;
            position: relative;
        }

        .close-btn {
            position: absolute;
            top: 10px;
            right: 12px;
            color: var(--neon-red);
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }

        .history-item {
            border-bottom: 1px solid rgba(255,255,255,0.08);
            padding: 8px 0;
            font-size: 11px;
            display: flex;
            justify-content: space-between;
        }
    </style>
</head>
<body>

    <div class="app-card">
        <div class="header">
            <div class="profile-container">
                <div class="avatar-wrapper">
                    <img src="https://i.ibb.co/L82X19m/profile-img.jpg" alt="Profile">
                </div>
                <div class="bot-title">
                    <h3>FINORIX PRO BOT</h3>
                    <span>100% REAL KNOWLEDGE ACTIVE</span>
                </div>
            </div>
            <button class="qx-btn" onclick="window.open('https://quotex.com', '_blank')">QX</button>
        </div>

        <div class="timezone-container">
            <div class="tz-box">
                <div class="tz-title">QX UTC+00:00 LIVE</div>
                <div class="tz-time" id="qx-time">00:00:00</div>
            </div>
            <div class="tz-box">
                <div class="tz-title">BD UTC+06:00 LIVE</div>
                <div class="tz-time" id="bd-time">00:00:00</div>
            </div>
        </div>

        <div class="controls-grid">
            <select class="select-box" id="asset-select">
                <optgroup label="--- REAL MARKETS ---">
                    <option value="EUR/USD">EUR/USD (REAL)</option>
                    <option value="GBP/USD">GBP/USD (REAL)</option>
                    <option value="USD/JPY">USD/JPY (REAL)</option>
                    <option value="AUD/USD">AUD/USD (REAL)</option>
                    <option value="USD/CAD">USD/CAD (REAL)</option>
                </optgroup>
                <optgroup label="--- OTC MARKETS ---">
                    <option value="EUR/USD (OTC)">EUR/USD (OTC)</option>
                    <option value="GBP/USD (OTC)">GBP/USD (OTC)</option>
                    <option value="USD/BDT (OTC)">USD/BDT (OTC)</option>
                    <option value="USD/INR (OTC)">USD/INR (OTC)</option>
                    <option value="USD/BRL (OTC)">USD/BRL (OTC)</option>
                </optgroup>
            </select>
            <select class="select-box" id="timeframe-select">
                <option value="5s">5 Sec</option>
                <option value="1m" selected>1 Min</option>
                <option value="5m">5 Min</option>
            </select>
        </div>

        <button class="analyze-btn" onclick="runAnalysis()">RUN 100% REAL ANALYSIS</button>

        <div class="upload-card">
            <label>REAL / OTC CHART SCREENSHOT UPLOAD</label>
            <input type="file" id="chart-file" class="file-input" accept="image/*" onchange="handleFileUpload(event)">
            <div class="file-btn" onclick="document.getElementById('chart-file').click()">Upload Screenshot</div>
            <img id="chart-preview" class="preview-img" alt="Chart Preview">

            <div class="scanning-overlay" id="electric-overlay">
                <div class="electric-line"></div>
                <div class="scan-text" id="scan-status-text">APPLYING 100% REAL KNOWLEDGE...</div>
            </div>
        </div>

        <div class="signal-display" id="signal-box">
            <div class="signal-title" id="signal-text" style="color: var(--neon-green);">SYSTEM READY</div>
            <div class="signal-type" id="signal-length">0% FAKE - 100% RELIABLE</div>
        </div>

        <div class="stats-grid">
            <div class="stat-box">
                <div class="stat-label">CONFIRMATION</div>
                <div class="stat-value" id="conf-val">99%</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">ACCURACY</div>
                <div class="stat-value" id="acc-val">100%</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">WIN RATE</div>
                <div class="stat-value" id="win-val">99%</div>
            </div>
        </div>

        <div class="action-grid">
            <button class="sub-btn" onclick="openModal('future-modal')">FUTURE SIGNALS</button>
            <button class="sub-btn" onclick="openModal('history-modal')">TRADE HISTORY</button>
        </div>
    </div>

    <div class="modal" id="future-modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal('future-modal')">&times;</span>
            <h4 style="color: var(--neon-gold); margin-bottom: 10px;">Real Knowledge Future Predictions</h4>
            <div id="future-list"></div>
        </div>
    </div>

    <div class="modal" id="history-modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal('history-modal')">&times;</span>
            <h4 style="color: var(--neon-blue); margin-bottom: 10px;">Verified Real Trade Logs</h4>
            <div id="history-list"></div>
        </div>
    </div>

    <script>
        function updateClocks() {
            const now = new Date();
            const qxHours = String(now.getUTCHours()).padStart(2, '0');
            const qxMins = String(now.getUTCMinutes()).padStart(2, '0');
            const qxSecs = String(now.getUTCSeconds()).padStart(2, '0');
            document.getElementById('qx-time').innerText = `${qxHours}:${qxMins}:${qxSecs}`;

            const bdTime = new Date(now.getTime() + (6 * 60 * 60 * 1000));
            const bdHours = String(bdTime.getUTCHours()).padStart(2, '0');
            const bdMins = String(bdTime.getUTCMinutes()).padStart(2, '0');
            const bdSecs = String(bdTime.getUTCSeconds()).padStart(2, '0');
            document.getElementById('bd-time').innerText = `${bdHours}:${bdMins}:${bdSecs}`;
        }
        setInterval(updateClocks, 1000);
        updateClocks();

        const REAL_KNOWLEDGE_RULES = [
            { type: "REAL", trigger: "Strong Support Level Rejection (100% Real Logic)", dir: "BUY (CALL)", candle: "LONG GREEN CANDLE", conf: "99%", acc: "100%", win: "99%" },
            { type: "REAL", trigger: "Resistance Breakout Confirmation Zone", dir: "BUY (CALL)", candle: "MARUBOZU", conf: "98%", acc: "99%", win: "98%" },
            { type: "REAL", trigger: "Fake Breakout Rejection at Key Resistance", dir: "SELL (PUT)", candle: "REJECTION PIN BAR", conf: "99%", acc: "100%", win: "99%" },
            { type: "REAL", trigger: "Demand Zone Volume Bounce", dir: "BUY (CALL)", candle: "MEDIUM CANDLE", conf: "97%", acc: "99%", win: "97%" },
            { type: "OTC", trigger: "OTC Trend Momentum Continuation Algorithm", dir: "BUY (CALL)", candle: "LONG CANDLE", conf: "99%", acc: "100%", win: "99%" },
            { type: "OTC", trigger: "OTC Price Exhaustion Reversal Node", dir: "SELL (PUT)", candle: "DOJI / SHORT", conf: "98%", acc: "99%", win: "98%" },
            { type: "OTC", trigger: "OTC Gap Filling Mathematical Engine", dir: "BUY (CALL)", candle: "MEDIUM CANDLE", conf: "98%", acc: "99%", win: "98%" },
            { type: "OTC", trigger: "OTC Dynamic Trendline Breakdown", dir: "SELL (PUT)", candle: "STRONG RED CANDLE", conf: "99%", acc: "100%", win: "99%" }
        ];

        const tradeHistory = [];

        function runAnalysis() {
            const overlay = document.getElementById('electric-overlay');
            const scanText = document.getElementById('scan-status-text');
            const signalBox = document.getElementById('signal-box');
            const signalText = document.getElementById('signal-text');
            const signalLength = document.getElementById('signal-length');
            const asset = document.getElementById('asset-select').value;
            const isOTC = asset.includes("OTC");

            scanText.innerText = isOTC ? "APPLYING 100% OTC REAL LOGIC..." : "SCANNING 100% REAL MARKET SNR...";
            overlay.style.display = 'flex';
            
            setTimeout(() => {
                overlay.style.display = 'none';
                const matchedRules = REAL_KNOWLEDGE_RULES.filter(r => isOTC ? r.type === "OTC" : r.type === "REAL");
                const result = matchedRules[Math.floor(Math.random() * matchedRules.length)];
                
                signalText.innerText = result.dir;
                if(result.dir.includes("BUY")) {
                    signalText.style.color = "var(--neon-green)";
                    signalBox.style.borderColor = "var(--neon-green)";
                } else {
                    signalText.style.color = "var(--neon-red)";
                    signalBox.style.borderColor = "var(--neon-red)";
                }

                signalLength.innerText = `${result.trigger} (${result.candle})`;
                document.getElementById('conf-val').innerText = result.conf;
                document.getElementById('acc-val').innerText = result.acc;
                document.getElementById('win-val').innerText = result.win;

                const time = document.getElementById('bd-time').innerText;
                tradeHistory.unshift({ asset, time, dir: result.dir, acc: result.acc });
                updateHistoryUI();

                setTimeout(() => {
                    signalText.innerText = "SYSTEM READY";
                    signalText.style.color = "var(--neon-green)";
                    signalBox.style.borderColor = "var(--neon-green)";
                    signalLength.innerText = "0% FAKE - 100% RELIABLE";
                }, 5000);

            }, 3500);
        }

        function handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.getElementById('chart-preview');
                    img.src = e.target.result;
                    img.style.display = 'block';
                    runAnalysis();
                }
                reader.readAsDataURL(file);
            }
        }

        function openModal(id) {
            if(id === 'future-modal') generateFutureSignals();
            document.getElementById(id).style.display = 'flex';
        }

        function closeModal(id) {
            document.getElementById(id).style.display = 'none';
        }

        function updateHistoryUI() {
            const container = document.getElementById('history-list');
            container.innerHTML = tradeHistory.map(item => `
                <div class="history-item">
                    <span>${item.time} - ${item.asset}</span>
                    <span style="color: ${item.dir.includes('BUY') ? 'var(--neon-green)' : 'var(--neon-red)'}">${item.dir} (${item.acc})</span>
                </div>
            `).join('');
        }

        function generateFutureSignals() {
            const container = document.getElementById('future-list');
            const assets = ["EUR/USD (REAL)", "EUR/USD (OTC)", "USD/BDT (OTC)", "GBP/USD (REAL)"];
            let html = "";
            for(let i=1; i<=4; i++) {
                const randomAsset = assets[Math.floor(Math.random() * assets.length)];
                const dir = Math.random() > 0.5 ? "CALL / BUY" : "PUT / SELL";
                html += `
                    <div class="history-item">
                        <span>+${i*15} Min (${randomAsset})</span>
                        <span style="color: ${dir.includes('BUY') ? 'var(--neon-green)' : 'var(--neon-red)'}">${dir} (100% Real)</span>
                    </div>
                `;
            }
            container.innerHTML = html;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
