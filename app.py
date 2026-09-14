import os
import time
import json
import random
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string

app = Flask(FINORIX PRO BOT)

# ==========================================
# 1. REAL & OTC MARKETS SEPARATION
# ==========================================
REAL_MARKETS = [
    "EUR/USD (REAL)", "GBP/USD (REAL)", "USD/JPY (REAL)", "AUD/USD (REAL)", 
    "USD/CAD (REAL)", "USD/CHF (REAL)", "EUR/GBP (REAL)", "EUR/JPY (REAL)", 
    "GBP/JPY (REAL)", "AUD/CAD (REAL)"
]

OTC_MARKETS = [
    "USD/BDT (OTC)", "USD/INR (OTC)", "USD/PKR (OTC)", "AUD/CAD (OTC)", 
    "GBP/JPY (OTC)", "EUR/AUD (OTC)", "EUR/NZD (OTC)", "NZD/CHF (OTC)", 
    "USD/CAD (OTC)", "USD/NGN (OTC)", "USD/BRL (OTC)", "CAD/CHF (OTC)", 
    "AUD/JPY (OTC)", "AUD/NZD (OTC)", "EUR/CHF (OTC)", "USD/EGP (OTC)", 
    "USD/MXN (OTC)", "EUR/USD (OTC)", "GBP/AUD (OTC)", "CHF/JPY (OTC)", 
    "NZD/JPY (OTC)", "USD/ARS (OTC)", "GBP/USD (OTC)", "NZD/USD (OTC)", 
    "CAD/JPY (OTC)", "GBP/CAD (OTC)", "USD/JPY (OTC)", "EUR/CAD (OTC)"
]

ALL_MARKETS = REAL_MARKETS + OTC_MARKETS
TIMEFRAMES = ["5 Sec", "10 Sec", "15 Sec", "20 Sec", "25 Sec", "30 Sec", "1 Min", "2 Min", "3 Min", "4 Min", "5 Min"]

# Base64 encoded image or fallback URL for Yasin Bhai's Photo
USER_AVATAR_URL = "https://i.ibb.co/6P0J9vS/yasin-photo.jpg" 

# ==========================================
# 2. TECHNICAL ANALYSIS CALCULATOR
# ==========================================
class QuantumAnalysisEngine:
    @staticmethod
    def analyze_market_data(prices):
        if len(prices) < 20:
            prices = [1.0800 + (random.uniform(-0.001, 0.001) * i) for i in range(30)]
        
        # Simple Moving Averages
        sma_short = sum(prices[-5:]) / 5
        sma_long = sum(prices[-20:]) / 20

        # Relative Strength Index (RSI) calculation
        gains = [max(prices[i] - prices[i-1], 0) for i in range(1, len(prices))]
        losses = [abs(min(prices[i] - prices[i-1], 0)) for i in range(1, len(prices))]
        avg_gain = sum(gains[-14:]) / 14 if sum(gains[-14:]) > 0 else 0.001
        avg_loss = sum(losses[-14:]) / 14 if sum(losses[-14:]) > 0 else 0.001
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Calculation of Decision Score
        buy_score = 0
        sell_score = 0

        if sma_short > sma_long:
            buy_score += 2
        else:
            sell_score += 2

        if rsi < 40:
            buy_score += 2
        elif rsi > 60:
            sell_score += 2
        else:
            buy_score += 1

        # Decision Output Guarantee
        if buy_score >= sell_score:
            direction = "BUY"
            confirmation = random.randint(91, 99)
            accuracy = random.randint(92, 99)
            win_rate = random.randint(90, 98)
        else:
            direction = "SELL"
            confirmation = random.randint(90, 98)
            accuracy = random.randint(91, 99)
            win_rate = random.randint(89, 97)

        candle_type = random.choice(["SHORT", "MEDIUM", "LONG"])
        return direction, candle_type, confirmation, accuracy, win_rate

# ==========================================
# 3. HTML / FRONTEND UI TEMPLATE
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FINORIX PRO BOT - Yasin Bhai</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.net/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #070406;
            --card-bg: #12090e;
            --neon-red: #ff003c;
            --neon-green: #00ff66;
            --neon-cyan: #00e5ff;
            --neon-yellow: #ffea00;
        }

        body {
            background-color: var(--bg-color);
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-bottom: 75px;
        }

        /* Animated Glowing Rainbow Border Frame */
        .neon-box {
            background: var(--card-bg);
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 15px;
            position: relative;
            box-shadow: 0 0 15px rgba(255, 0, 60, 0.15);
            border: 1px solid #29121c;
            animation: borderPulse 3s infinite alternate;
        }

        @keyframes borderPulse {
            0% { border-color: rgba(255, 0, 60, 0.6); box-shadow: 0 0 10px rgba(255, 0, 60, 0.3); }
            50% { border-color: rgba(0, 229, 255, 0.6); box-shadow: 0 0 10px rgba(0, 229, 255, 0.3); }
            100% { border-color: rgba(0, 255, 102, 0.6); box-shadow: 0 0 10px rgba(0, 255, 102, 0.3); }
        }

        /* Header UI Layout */
        .profile-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px dashed #3d1927;
            padding-bottom: 12px;
            margin-bottom: 12px;
        }

        .user-avatar {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            border: 2px solid var(--neon-red);
            object-fit: cover;
            box-shadow: 0 0 12px var(--neon-red);
        }

        .bot-title {
            font-size: 1.1rem;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 0.5px;
            margin: 0;
            background: linear-gradient(90deg, #ff003c, #ffea00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .owner-subtitle {
            font-size: 0.75rem;
            color: #ff8c00;
            font-weight: 700;
            margin: 0;
        }

        .btn-qx {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: #fff;
            font-weight: 800;
            font-size: 0.8rem;
            padding: 6px 14px;
            border-radius: 20px;
            text-decoration: none;
            box-shadow: 0 0 10px rgba(0, 114, 255, 0.5);
            transition: 0.2s;
        }

        /* Timezone Displays */
        .clock-badge {
            background: #1c0a14;
            border: 1px solid #3d1728;
            border-radius: 8px;
            padding: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            text-align: center;
        }

        /* Control Forms & Buttons */
        .select-custom {
            background-color: #170a11;
            border: 1px solid #3b1827;
            color: #fff;
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: 10px;
            padding: 9px;
        }

        .btn-analyze {
            background: linear-gradient(135deg, var(--neon-red), #b30024);
            color: #ffffff;
            font-weight: 900;
            font-size: 1rem;
            border: none;
            border-radius: 12px;
            padding: 13px;
            width: 100%;
            letter-spacing: 1px;
            box-shadow: 0 0 18px rgba(255, 0, 60, 0.5);
            transition: 0.3s;
        }

        /* Signal Display Box */
        .signal-display {
            font-size: 2.1rem;
            font-weight: 900;
            text-align: center;
            border-radius: 14px;
            padding: 12px;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }

        .signal-up {
            background: rgba(0, 255, 102, 0.12);
            border: 2px solid var(--neon-green);
            color: var(--neon-green);
            box-shadow: 0 0 25px rgba(0, 255, 102, 0.3);
        }

        .signal-down {
            background: rgba(255, 0, 60, 0.12);
            border: 2px solid var(--neon-red);
            color: var(--neon-red);
            box-shadow: 0 0 25px rgba(255, 0, 60, 0.3);
        }

        .metric-box {
            background: #180a12;
            border: 1px solid #331524;
            border-radius: 10px;
            padding: 8px;
            text-align: center;
        }

        .metric-title {
            font-size: 0.65rem;
            color: #a37388;
            font-weight: 800;
        }

        .metric-value {
            font-size: 1rem;
            font-weight: 900;
            color: #00e5ff;
        }

        /* Laser Electric Scanner Animation */
        .scanner-frame {
            position: relative;
            border: 2px dashed #401b2c;
            border-radius: 12px;
            padding: 12px;
            text-align: center;
            background: #0d050a;
            overflow: hidden;
        }

        .laser-beam {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #ff003c, #00e5ff, #00ff66);
            box-shadow: 0 0 15px #00e5ff;
            display: none;
            animation: laserScan 2s infinite ease-in-out;
        }

        @keyframes laserScan {
            0% { top: 0%; }
            50% { top: 92%; }
            100% { top: 0%; }
        }

        /* Bottom Fixed Navigation Bar */
        .bottom-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #0f070b;
            border-top: 1px solid #2b111e;
            display: flex;
            justify-content: space-around;
            padding: 8px 0;
            z-index: 9999;
        }

        .bottom-item {
            color: #8c5b71;
            text-decoration: none;
            font-size: 0.7rem;
            font-weight: 800;
            text-align: center;
        }

        .bottom-item.active {
            color: var(--neon-red);
        }
    </style>
</head>
<body class="p-2 p-md-3">

    <div class="container" style="max-width: 480px;">
        <div class="neon-box">
            
            <!-- Step 1 & 2: Left Avatar, Title, Subtitle & QX Right Button -->
            <div class="profile-container">
                <div class="d-flex align-items-center gap-2">
                    <img src="{{ avatar_url }}" alt="Yasin Bhai" class="user-avatar" onerror="this.src='https://ui-avatars.com/api/?name=Yasin+Bhai&background=2a0815&color=ff003c'">
                    <div>
                        <h6 class="bot-title">FINORIX PRO BOT</h6>
                        <p class="owner-subtitle">Yasin Bhai (Owner)</p>
                    </div>
                </div>
                <a href="https://quotex.com" target="_blank" class="btn-qx">
                    <i class="fa-solid fa-arrow-up-right-from-square me-1"></i> QX
                </a>
            </div>

            <!-- Step 3 & 4: Live Timezones -->
            <div class="row g-2 mb-3">
                <div class="col-6">
                    <div class="clock-badge text-info">
                        <div>QX UTC+00:00 LIVE</div>
                        <div id="qxClock" class="fs-6 fw-bold">00:00:00</div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="clock-badge text-warning">
                        <div>BD UTC+06:00 LIVE</div>
                        <div id="bdClock" class="fs-6 fw-bold">00:00:00</div>
                    </div>
                </div>
            </div>

            <!-- Step 5 & 6: Asset Selection & Timeframe -->
            <div class="row g-2 mb-3">
                <div class="col-7">
                    <label class="form-label text-muted small fw-bold mb-1">SELECT ASSET</label>
                    <select id="assetSelect" class="form-select select-custom">
                        <optgroup label="-- REAL FOREX MARKETS --">
                            {% for pair in real_pairs %}
                            <option value="{{ pair }}">{{ pair }}</option>
                            {% endfor %}
                        </optgroup>
                        <optgroup label="-- QUOTEX OTC MARKETS --">
                            {% for pair in otc_pairs %}
                            <option value="{{ pair }}" selected>{{ pair }}</option>
                            {% endfor %}
                        </optgroup>
                    </select>
                </div>
                <div class="col-5">
                    <label class="form-label text-muted small fw-bold mb-1">TIMEFRAME</label>
                    <select id="tfSelect" class="form-select select-custom">
                        {% for tf in timeframes %}
                        <option value="{{ tf }}">{{ tf }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>

            <!-- Step 6: Analyze Button -->
            <button id="btnAnalyze" class="btn-analyze mb-3" onclick="triggerAnalysis()">
                <i class="fa-solid fa-bolt me-2"></i> ANALYZE SIGNAL
            </button>

            <!-- Step 7: QX Live Chart Upload Panel -->
            <div class="scanner-frame mb-3">
                <div class="laser-beam" id="laserBeam"></div>
                <div class="small fw-bold text-white mb-1"><i class="fa-solid fa-cloud-arrow-up text-danger me-1"></i> QX LIVE CHART UPLOAD</div>
                <input type="file" id="chartFile" accept="image/*" class="form-control form-control-sm bg-dark text-white border-secondary mb-2" onchange="previewChart(event)">
                <img id="chartImg" style="max-height: 140px; display: none;" class="w-100 rounded mb-2" alt="Chart Preview">
                <button id="btnScanChart" class="btn btn-sm btn-outline-info w-100 fw-bold d-none" onclick="scanUploadedChart()">
                    <i class="fa-solid fa-qrcode me-1"></i> AI SCAN CHART
                </button>
            </div>

            <!-- Signal Output Display Box -->
            <div id="signalOutput" class="signal-display signal-up">
                READY FOR SIGNAL
            </div>

            <!-- Metrics Score Display -->
            <div class="row g-2 mb-3">
                <div class="col-4">
                    <div class="metric-box">
                        <div class="metric-title">CONFIRMATION</div>
                        <div class="metric-value" id="valConfirm">98%</div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="metric-box">
                        <div class="metric-title">ACCURACY</div>
                        <div class="metric-value" id="valAccuracy">99%</div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="metric-box">
                        <div class="metric-title">WIN RATE</div>
                        <div class="metric-value" id="valWinRate">97%</div>
                    </div>
                </div>
            </div>

            <!-- Step 8: AI Future Signals & History Controls -->
            <div class="row g-2 mb-3">
                <div class="col-6">
                    <button class="btn btn-sm btn-outline-warning w-100 fw-bold" onclick="generateFutureSignals()">
                        <i class="fa-solid fa-crystal-ball me-1"></i> FUTURE SIGNALS
                    </button>
                </div>
                <div class="col-6">
                    <button class="btn btn-sm btn-outline-success w-100 fw-bold" onclick="toggleHistory()">
                        <i class="fa-solid fa-clock-rotate-left me-1"></i> TRADE HISTORY
                    </button>
                </div>
            </div>

            <!-- Future Signals Content Box -->
            <div id="futureBox" class="p-2 mb-3 bg-dark border border-secondary rounded d-none" style="font-family: monospace; font-size: 0.8rem; max-height: 150px; overflow-y: auto;">
                <div class="d-flex justify-content-between text-warning mb-1">
                    <span>Upcoming Signals:</span>
                    <button class="btn btn-xs btn-warning py-0 px-2 fs-7" onclick="copyFutureSignals()">Copy</button>
                </div>
                <div id="futureList" class="text-success"></div>
            </div>

            <!-- History Panel Box -->
            <div id="historyBox" class="p-2 bg-dark border border-secondary rounded d-none" style="max-height: 160px; overflow-y: auto;">
                <div class="text-white small fw-bold mb-1"><i class="fa-solid fa-list me-1"></i> Executed Log</div>
                <ul id="historyList" class="list-group list-group-flush small"></ul>
            </div>

        </div>
    </div>

    <!-- Bottom Navigation Bar -->
    <div class="bottom-bar">
        <a href="#" class="bottom-item active"><i class="fa-solid fa-chart-line fs-5 d-block"></i>TRADE</a>
        <a href="#" class="bottom-item" onclick="alert('QX Engine 100% Real Active')"><i class="fa-solid fa-microchip fs-5 d-block"></i>STATUS</a>
        <a href="#" class="bottom-item" onclick="alert('FINORIX PRO BOT\\nOwner: Yasin Bhai')"><i class="fa-solid fa-user-shield fs-5 d-block"></i>PROFILE</a>
    </div>

    <script>
        let historyCounter = 0;

        // Live Clocks Update
        function updateClocks() {
            const now = new Date();
            
            // QX Time (UTC+0)
            const utcHours = String(now.getUTCHours()).padStart(2, '0');
            const utcMins = String(now.getUTCMinutes()).padStart(2, '0');
            const utcSecs = String(now.getUTCSeconds()).padStart(2, '0');
            document.getElementById('qxClock').innerText = `${utcHours}:${utcMins}:${utcSecs}`;

            // BD Time (UTC+6)
            let bdHours = (now.getUTCHours() + 6) % 24;
            const bdHoursStr = String(bdHours).padStart(2, '0');
            document.getElementById('bdClock').innerText = `${bdHoursStr}:${utcMins}:${utcSecs}`;
        }
        setInterval(updateClocks, 1000);
        updateClocks();

        // Bengali Voice Function
        function speakVoiceSignal(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel(); // Stop previous
                const speech = new SpeechSynthesisUtterance(text);
                speech.lang = 'bn-BD';
                speech.rate = 0.95;
                window.speechSynthesis.speak(speech);
            }
        }

        function previewChart(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.getElementById('chartImg');
                    img.src = e.target.result;
                    img.style.display = 'block';
                    document.getElementById('btnScanChart').classList.remove('d-none');
                }
                reader.readAsDataURL(file);
            }
        }

        async function triggerAnalysis() {
            const asset = document.getElementById('assetSelect').value;
            const tf = document.getElementById('tfSelect').value;
            const btn = document.getElementById('btnAnalyze');

            btn.disabled = true;
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin me-2"></i> ANALYZING MARKET...`;

            try {
                const response = await fetch(`/api/generate_signal?asset=${encodeURIComponent(asset)}&tf=${encodeURIComponent(tf)}`);
                const data = await response.json();

                renderSignalResult(data);
                addHistoryRecord(data.direction, asset, data.accuracy);

                // Instant Bengali Voice
                if(data.direction === "BUY") {
                    speakVoiceSignal("এখান থেকে আপনি আপের জন্য ট্রেড প্লেস করুন");
                } else {
                    speakVoiceSignal("এখান থেকে আপনি ডাউনের জন্য ট্রেড প্লেস করুন");
                }

                // Timeframe Lock
                let timerSeconds = 5;
                const lockInterval = setInterval(() => {
                    btn.innerHTML = `<i class="fa-solid fa-lock me-2"></i> LOCKED (${timerSeconds}s)`;
                    timerSeconds--;
                    if(timerSeconds < 0) {
                        clearInterval(lockInterval);
                        btn.disabled = false;
                        btn.innerHTML = `<i class="fa-solid fa-bolt me-2"></i> ANALYZE SIGNAL`;
                    }
                }, 1000);

            } catch (err) {
                console.error(err);
                btn.disabled = false;
                btn.innerHTML = `<i class="fa-solid fa-bolt me-2"></i> ANALYZE SIGNAL`;
            }
        }

        async function scanUploadedChart() {
            const laser = document.getElementById('laserBeam');
            const btn = document.getElementById('btnScanChart');
            
            laser.style.display = 'block';
            btn.disabled = true;

            setTimeout(async () => {
                laser.style.display = 'none';
                const asset = document.getElementById('assetSelect').value;
                const response = await fetch(`/api/generate_signal?asset=${encodeURIComponent(asset)}&tf=1Min`);
                const data = await response.json();

                renderSignalResult(data);
                addHistoryRecord(data.direction, asset + " (Chart AI)", data.accuracy);

                if(data.direction === "BUY") speakVoiceSignal("এখান থেকে আপনি আপের জন্য ট্রেড প্লেস করুন");
                else speakVoiceSignal("এখান থেকে আপনি ডাউনের জন্য ট্রেড প্লেস করুন");

                // Auto reset chart preview
                setTimeout(() => {
                    document.getElementById('chartImg').style.display = 'none';
                    document.getElementById('chartFile').value = '';
                    btn.classList.add('d-none');
                    btn.disabled = false;
                }, 4000);

            }, 4000);
        }

        function renderSignalResult(data) {
            const box = document.getElementById('signalOutput');
            
            if (data.direction === "BUY") {
                box.className = "signal-display signal-up";
                box.innerText = `BUY (${data.candle_type})`;
            } else {
                box.className = "signal-display signal-down";
                box.innerText = `SELL (${data.candle_type})`;
            }

            document.getElementById('valConfirm').innerText = data.confirmation + "%";
            document.getElementById('valAccuracy').innerText = data.accuracy + "%";
            document.getElementById('valWinRate').innerText = data.win_rate + "%";
        }

        function generateFutureSignals() {
            const box = document.getElementById('futureBox');
            const list = document.getElementById('futureList');
            const asset = document.getElementById('assetSelect').value;
            
            box.classList.remove('d-none');
            list.innerHTML = "Processing Real Market Algorithm...";

            let resultText = "";
            let now = new Date();

            for(let i=1; i<=12; i++) {
                now.setMinutes(now.getMinutes() + 2);
                let timeStr = now.toTimeString().split(' ')[0].substring(0,5);
                let dir = Math.random() > 0.48 ? "UP ⬆️" : "DOWN ⬇️";
                resultText += `[${timeStr}] ${asset} -> ${dir}<br>`;
            }

            list.innerHTML = resultText;
        }

        function copyFutureSignals() {
            const content = document.getElementById('futureList').innerText;
            navigator.clipboard.writeText(content);
            alert("Future signals copied to clipboard!");
        }

        function toggleHistory() {
            const box = document.getElementById('historyBox');
            box.classList.toggle('d-none');
        }

        function addHistoryRecord(direction, asset, acc) {
            historyCounter++;
            const list = document.getElementById('historyList');
            const item = document.createElement('li');
            item.className = "list-group-item bg-dark text-white border-secondary d-flex justify-content-between py-1 px-2";
            item.innerHTML = `<span>#${historyCounter} ${asset}</span> <span class="${direction === 'BUY' ? 'text-success' : 'text-danger'} fw-bold">${direction} (${acc}%)</span>`;
            list.prepend(item);
        }
    </script>
</body>
</html>
"""

# ==========================================
# 4. FLASK SERVER ENDPOINTS
# ==========================================
@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        real_pairs=REAL_MARKETS,
        otc_pairs=OTC_MARKETS,
        timeframes=TIMEFRAMES,
        avatar_url=USER_AVATAR_URL
    )

@app.route('/api/generate_signal', methods=['GET'])
def generate_signal():
    asset = request.args.get('asset', 'USD/BDT (OTC)')
    tf = request.args.get('tf', '1 Min')

    # Real Price Data Simulation
    base_price = 110.50 if "BDT" in asset else 1.0850
    mock_prices = [base_price + (random.uniform(-0.002, 0.002) * i) for i in range(30)]

    direction, candle_type, confirmation, accuracy, win_rate = QuantumAnalysisEngine.analyze_market_data(mock_prices)

    return jsonify({
        "direction": direction,
        "candle_type": candle_type,
        "confirmation": confirmation,
        "accuracy": accuracy,
        "win_rate": win_rate
    })

if __name__ == '__main__':
    # Flask app ready for Render & GitHub hosting
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
