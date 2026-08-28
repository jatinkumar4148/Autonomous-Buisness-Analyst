import streamlit as st
import time
import math
import random
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Analyst Desk",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "running" not in st.session_state:
    st.session_state.running = False

if "completed" not in st.session_state:
    st.session_state.completed = False

if "active_agent" not in st.session_state:
    st.session_state.active_agent = 0

if "progress" not in st.session_state:
    st.session_state.progress = 0

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "analysis_idea" not in st.session_state:
    st.session_state.analysis_idea = ""

# =========================================================
# THEME
# =========================================================

dark = st.session_state.dark_mode

if dark:
    BG = "#071412"
    CARD = "#0d211d"
    CARD2 = "#102923"
    TEXT = "#f4faf7"
    MUTED = "#9eb4aa"
    BORDER = "rgba(255,255,255,.12)"
    SIDEBAR = "#031512"
    INPUT = "#0b1c18"
else:
    BG = "#f8faf9"
    CARD = "#ffffff"
    CARD2 = "#f5fbf8"
    TEXT = "#0b2020"
    MUTED = "#65727b"
    BORDER = "#e2e8e6"
    SIDEBAR = "#03211c"
    INPUT = "#ffffff"

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {{
    font-family: 'Inter', sans-serif;
}}

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(circle at 80% 5%, rgba(71,214,135,.06), transparent 22%),
        {BG};
    color: {TEXT};
}}

.main .block-container {{
    max-width: 1400px;
    padding-top: 8px;
    padding-bottom: 60px;
}}

/* =====================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
===================================================== */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {{
    background:
        radial-gradient(circle at 20% 20%, rgba(43,255,171,.12), transparent 20%),
        linear-gradient(180deg, {SIDEBAR}, #021613);
    border-right: 1px solid rgba(94,255,190,.15);
}}

section[data-testid="stSidebar"] > div {{
    padding-top: 25px;
}}

.brand {{
    padding: 10px 10px 22px 10px;
}}

.brand-title {{
    font-size: 23px;
    font-weight: 800;
    color: white;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.brand-star {{
    color: #b8ff3d;
    font-size: 26px;
    animation: starFloat 2.5s ease-in-out infinite;
}}

.brand-sub {{
    color: #72f0b0;
    font-size: 13px;
    margin-top: 5px;
}}

@keyframes starFloat {{
    0%,100% {{ transform: translateY(0) rotate(0deg); }}
    50% {{ transform: translateY(-5px) rotate(8deg); }}
}}

.live-card {{
    position: relative;
    margin: 8px 0 28px 0;
    padding: 13px 15px;
    border: 1px solid rgba(105,255,190,.22);
    border-radius: 13px;
    background: rgba(255,255,255,.035);
    overflow: hidden;
}}

.live-card:before {{
    content: "";
    position: absolute;
    width: 120px;
    height: 120px;
    right: -40px;
    top: -50px;
    background: radial-gradient(circle, rgba(59,255,151,.22), transparent 70%);
    animation: liveGlow 2s infinite alternate;
}}

@keyframes liveGlow {{
    from {{ opacity: .3; transform: scale(.8); }}
    to {{ opacity: 1; transform: scale(1.3); }}
}}

.live-row {{
    display: flex;
    align-items: center;
    gap: 11px;
    color: white;
    font-size: 14px;
    font-weight: 600;
}}

.live-dot {{
    width: 18px;
    height: 18px;
    background: #ff5353;
    border-radius: 50%;
    position: relative;
    box-shadow: 0 0 15px rgba(255,83,83,.8);
}}

.live-dot:after {{
    content: "";
    position: absolute;
    inset: -5px;
    border: 1px solid #ff5353;
    border-radius: 50%;
    animation: livePulse 1.5s infinite;
}}

@keyframes livePulse {{
    0% {{ transform: scale(.7); opacity: .9; }}
    100% {{ transform: scale(1.7); opacity: 0; }}
}}

.wave {{
    margin-left: auto;
    width: 50px;
    height: 25px;
    position: relative;
}}

.wave span {{
    display: inline-block;
    width: 3px;
    margin-right: 3px;
    border-radius: 10px;
    background: #49ff9d;
    animation: wave 1s ease-in-out infinite;
}}

.wave span:nth-child(1) {{ height: 8px; animation-delay: .1s; }}
.wave span:nth-child(2) {{ height: 17px; animation-delay: .2s; }}
.wave span:nth-child(3) {{ height: 25px; animation-delay: .3s; }}
.wave span:nth-child(4) {{ height: 13px; animation-delay: .4s; }}
.wave span:nth-child(5) {{ height: 20px; animation-delay: .5s; }}

@keyframes wave {{
    0%,100% {{ transform: scaleY(.5); opacity: .5; }}
    50% {{ transform: scaleY(1); opacity: 1; }}
}}

.sidebar-heading {{
    color: #9cff75;
    font-size: 13px;
    font-weight: 600;
    margin: 25px 0 12px;
}}

.nav-item {{
    position: relative;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 13px 14px;
    margin: 6px 0;
    color: #e5efeb;
    border-radius: 11px;
    transition: all .3s ease;
    overflow: hidden;
}}

.nav-item:hover {{
    background: rgba(66,255,164,.09);
    transform: translateX(5px);
}}

.nav-item.active {{
    background: linear-gradient(
        90deg,
        rgba(49,255,155,.15),
        rgba(49,255,155,.025)
    );
    box-shadow: inset 3px 0 0 #57ffab;
}}

.nav-icon {{
    font-size: 22px;
    width: 28px;
}}

.nav-item.active .nav-icon {{
    color: #8aff58;
    animation: iconPulse 1.5s infinite;
}}

@keyframes iconPulse {{
    0%,100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.12); }}
}}

.enterprise {{
    margin-top: 100px;
    padding: 18px;
    border: 1px solid rgba(88,255,178,.25);
    border-radius: 15px;
    background:
        radial-gradient(circle at 80% 10%, rgba(72,255,170,.15), transparent 30%),
        rgba(255,255,255,.025);
}}

.enterprise-icon {{
    font-size: 28px;
    color: #00ff9c;
}}

.enterprise-title {{
    color: white;
    font-weight: 700;
    margin-top: 10px;
}}

.enterprise-text {{
    color: #b4c7bf;
    font-size: 12px;
    line-height: 1.9;
    margin-top: 8px;
}}

/* =====================================================
   TOP AREA
===================================================== */

.topbar {{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    height: 36px;
}}

.theme-label {{
    color: {MUTED};
    font-size: 12px;
    margin-right: 10px;
}}

/* =====================================================
   STREAMLIT HEADER + SIDEBAR OPEN/CLOSE
===================================================== */

/*
   Keep Streamlit's header/toolbar DOM alive so the native sidebar
   open/close control continues to work.
*/
header[data-testid="stHeader"] {{
    visibility: visible !important;
    display: block !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}}

/*
   Hide only the top-right actions.
   Do NOT hide the complete stToolbar.
*/
header button[aria-label*="Share"],
header button[aria-label*="Star"],
header button[aria-label*="Edit"],
header button[aria-label*="GitHub"],
header button[aria-label*="Deploy"] {{
    display: none !important;
    visibility: hidden !important;
}}

/* Hide Streamlit decoration without removing header controls. */
div[data-testid="stDecoration"] {{
    display: none !important;
    visibility: hidden !important;
}}

/* Keep native sidebar collapse control visible. */
button[data-testid="stSidebarCollapseButton"] {{
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 999999 !important;
}}

/* Keep native sidebar open control visible after collapse. */
[data-testid="stSidebarCollapsedControl"] {{
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 999999 !important;
}}

[data-testid="stSidebarCollapsedControl"] button {{
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 1000000 !important;
}}

/* Remove extra content spacing without collapsing the header itself. */
[data-testid="stAppViewContainer"] {{
    margin-top: 0 !important;
    padding-top: 0 !important;
}}

[data-testid="stAppViewBlockContainer"] {{
    padding-top: 0 !important;
}}

/* Streamlit button */
div[data-testid="stButton"] > button {{
    border-radius: 12px !important;
    transition: all .3s ease !important;
}}

.theme-button button {{
    width: 54px !important;
    height: 40px !important;
    min-height: 40px !important;
    border-radius: 15px !important;
    background: {CARD} !important;
    border: 1px solid rgba(255,190,70,.35) !important;
    box-shadow: 0 8px 25px rgba(0,0,0,.08) !important;
    font-size: 23px !important;
}}

.theme-button button {{
    background: {CARD} !important;
    color: {TEXT} !important;
}}

.theme-button button:hover {{
    transform: rotate(18deg) scale(1.08) !important;
    box-shadow:
        0 0 0 6px rgba(255,190,70,.08),
        0 10px 30px rgba(255,190,70,.15) !important;
}}

/* =====================================================
   HERO
===================================================== */

.hero {{
    position: relative;
    padding: 2px 5px 0;
    min-height: 125px;
    overflow: hidden;
}}

.hero-title {{
    font-size: clamp(40px, 4vw, 62px);
    line-height: 1.02;
    letter-spacing: -2.8px;
    font-weight: 800;
    color: {TEXT};
    max-width: 720px;
    position: relative;
    z-index: 2;
    animation: heroIn .8s ease both;
}}

@keyframes heroIn {{
    from {{
        opacity: 0;
        transform: translateY(25px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.hero-title:after {{
    content: "";
    display: block;
    width: 55px;
    height: 4px;
    margin-top: 17px;
    border-radius: 10px;
    background: linear-gradient(90deg,#ff4c42,#ff6a5b);
    animation: lineGrow .8s .4s ease both;
}}

@keyframes lineGrow {{
    from {{ width: 0; }}
    to {{ width: 55px; }}
}}

.hero-desc {{
    margin-top: 16px;
    color: {MUTED};
    font-size: 16px;
    line-height: 1.7;
    max-width: 700px;
    animation: heroIn .8s .15s ease both;
}}

.green-text {{
    color: #149447;
    font-weight: 700;
}}

/* =====================================================
   GRAPH
===================================================== */

.graph-box {{
    position: absolute;
    right: 0;
    top: 0;
    width: 420px;
    height: 220px;
    opacity: .95;
}}

.chart-svg {{
    width: 100%;
    height: 100%;
    overflow: visible;
}}

.chart-line {{
    stroke-dasharray: 900;
    stroke-dashoffset: 900;
    animation: drawChart 2.5s .5s ease forwards;
}}

@keyframes drawChart {{
    to {{ stroke-dashoffset: 0; }}
}}

.chart-point {{
    animation: pointPulse 2s infinite;
}}

@keyframes pointPulse {{
    0%,100% {{ r: 4; opacity: .7; }}
    50% {{ r: 7; opacity: 1; }}
}}

.insight-card {{
    position: absolute;
    left: 120px;
    top: 55px;
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 9px 13px;
    box-shadow: 0 10px 30px rgba(0,0,0,.1);
    animation: floatCard 3s ease-in-out infinite;
}}

@keyframes floatCard {{
    0%,100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-8px); }}
}}

.insight-small {{
    font-size: 9px;
    color: {MUTED};
}}

.insight-value {{
    color: #12a74d;
    font-size: 16px;
    font-weight: 700;
}}

/* =====================================================
   WORKSPACE CARD
===================================================== */

.workspace {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    padding: 20px;
    box-shadow:
        0 15px 40px rgba(10,30,25,.06),
        0 2px 6px rgba(0,0,0,.025);
    animation: cardIn .7s ease both;
}}

@keyframes cardIn {{

    from {{
        opacity: 0;
        transform: translateY(20px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}

.workspace-title {{

    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 16px;
    font-weight: 700;
    color: {TEXT};
    margin-bottom: 12px;

}}

.bulb {{

    width: 30px;
    height: 30px;
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #fff8e8;
    color: #f4a900;

    box-shadow: 0 0 20px rgba(255,180,30,.15);

}}

textarea {{

    border-radius: 10px !important;
    border: 1px solid #b9a8ff !important;

    background: {INPUT} !important;
    color: {TEXT} !important;

    min-height: 90px !important;

    transition: all .3s ease !important;

}}

textarea:focus {{

    border-color: #ff766a !important;

    box-shadow:
        0 0 0 3px rgba(255,91,78,.08),
        0 0 25px rgba(255,91,78,.08) !important;

}}

/* =====================================================
   CHARACTER COUNTER
===================================================== */

.char-counter {{

    width: 100%;

    text-align: right;

    color: {MUTED};

    font-size: 11px;

    line-height: 16px;

    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 8px;

    padding: 0 4px;

    box-sizing: border-box;

    position: static !important;

    z-index: auto !important;

    background: transparent !important;

}}

/* =====================================================
   GENERATE BUTTON
===================================================== */

.generate-wrap {{
    margin-top: 14px;
    position: relative;
}}

.generate-wrap button {{
    position: relative;
    overflow: hidden !important;
    width: 100% !important;
    height: 54px !important;
    border: none !important;
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    background: #000000 !important;
    box-shadow:
        0 8px 22px rgba(0,0,0,.20) !important;
}}

.generate-wrap button:before {{
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,.35),
        transparent
    );
    transform: skewX(-20deg);
    animation: buttonShine 2.5s infinite;
}}

@keyframes buttonShine {{
    0% {{ left: -100%; }}
    45%,100% {{ left: 140%; }}
}}

.generate-wrap button:hover {{
    transform: translateY(-2px) !important;
    box-shadow:
         0 12px 30px rgba(0,0,0,.30) !important;
}}

.generate-wrap button:active {{
    transform: scale(.985) !important;
}}

/* =====================================================
   STATUS CARD
===================================================== */

.status-card {{
    position: relative;
    margin-top: 15px;
    background:
        radial-gradient(circle at 80% 50%, rgba(52,220,120,.07), transparent 25%),
        {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    padding: 22px;
    overflow: hidden;
    box-shadow: 0 12px 35px rgba(10,40,30,.06);
}}

.status-card:before {{
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle, rgba(41,190,104,.3) 1px, transparent 1px);
    background-size: 35px 35px;
    opacity: .12;
    animation: particleMove 15s linear infinite;
}}

@keyframes particleMove {{
    from {{ transform: translate(0,0); }}
    to {{ transform: translate(35px,35px); }}
}}

.status-content {{
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    gap: 20px;
}}

.ai-orb {{
    width: 78px;
    height: 78px;
    min-width: 78px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle, #31db77, #0d9b50);
    box-shadow:
        0 0 0 9px rgba(45,210,112,.07),
        0 0 0 18px rgba(45,210,112,.04),
        0 0 35px rgba(45,210,112,.3);
    position: relative;
    animation: orbFloat 2.5s ease-in-out infinite;
}}

.ai-orb:before,
.ai-orb:after {{
    content: "";
    position: absolute;
    inset: -12px;
    border: 1px solid rgba(48,216,119,.4);
    border-radius: 50%;
    animation: orbRing 2.5s linear infinite;
}}

.ai-orb:after {{
    inset: -22px;
    animation-duration: 4s;
    opacity: .5;
}}

@keyframes orbFloat {{
    0%,100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-5px); }}
}}

@keyframes orbRing {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}

.robot {{
    font-size: 30px;
}}

.status-info {{
    flex: 1;
}}

.status-title {{
    font-size: 19px;
    font-weight: 700;
    color: {TEXT};
}}

.status-title .dot {{
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #32be60;
    border-radius: 50%;
    margin-left: 7px;
    box-shadow: 0 0 12px #32be60;
    animation: greenPulse 1.4s infinite;
}}

@keyframes greenPulse {{
    0%,100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: .45; transform: scale(.75); }}
}}

.status-sub {{
    color: {MUTED};
    font-size: 13px;
    margin-top: 8px;
}}

.badges {{
    display: flex;
    gap: 8px;
    margin-top: 12px;
}}

.badge-small {{
    border: 1px solid {BORDER};
    background: rgba(60,180,100,.05);
    border-radius: 20px;
    padding: 6px 10px;
    color: {MUTED};
    font-size: 11px;
}}

.progress-row {{
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 13px;
}}

.progress-track {{
    height: 7px;
    flex: 1;
    border-radius: 10px;
    background: #e8eceb;
    overflow: hidden;
}}

.progress-fill {{
    height: 100%;
    border-radius: 10px;
    background:
        linear-gradient(
            90deg,
            #43a847,
            #71dd47,
            #1fbb72
        );
    position: relative;
}}

.progress-fill:after {{
    content: "";
    position: absolute;
    top: 0;
    width: 100px;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,.7),
        transparent
    );
    animation: progressGlow 1.5s infinite;
}}

@keyframes progressGlow {{
    from {{ left: -120px; }}
    to {{ left: 100%; }}
}}

.progress-number {{
    color: #0c9d45;
    font-weight: 700;
    font-size: 20px;
}}

/* =====================================================
   RADAR
===================================================== */

.radar {{
    width: 180px;
    height: 130px;
    position: relative;
}}

.radar-circle {{
    position: absolute;
    border: 1px solid rgba(40,190,100,.22);
    border-radius: 50%;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}}

.r1 {{ width: 55px; height: 55px; }}
.r2 {{ width: 95px; height: 95px; }}
.r3 {{ width: 135px; height: 135px; }}

.radar-scan {{
    position: absolute;
    width: 75px;
    height: 75px;
    left: 50%;
    top: 50%;
    transform-origin: 0 0;
    background: linear-gradient(
        45deg,
        rgba(81,215,78,.65),
        transparent 70%
    );
    clip-path: polygon(0 0,100% 0,0 100%);
    animation: radarSpin 2.8s linear infinite;
}}

@keyframes radarSpin {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}

/* =====================================================
   PIPELINE
===================================================== */

.pipeline {{
    margin-top: 16px;
    padding: 25px 22px;
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    box-shadow: 0 12px 35px rgba(10,40,30,.05);
}}

.pipeline-row {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    position: relative;
}}

.pipeline-line {{
    position: absolute;
    left: 7%;
    right: 7%;
    top: 43px;
    height: 3px;
    background: #dce2df;
    z-index: 0;
}}

.energy-line {{
    position: absolute;
    left: 7%;
    top: 43px;
    height: 3px;
    background: linear-gradient(
        90deg,
        #46d94e,
        #b1ff57,
        #46d94e
    );
    z-index: 1;
    box-shadow: 0 0 12px rgba(70,220,80,.8);
    animation: energyMove 1.4s linear infinite;
}}

@keyframes energyMove {{
    0% {{ width: 0%; }}
    100% {{ width: 86%; }}
}}

.agent {{
    width: 18%;
    text-align: center;
    position: relative;
    z-index: 3;
}}

.agent-circle {{
    width: 72px;
    height: 72px;
    margin: auto;
    border-radius: 50%;
    border: 1px solid #dce2df;
    background: {CARD};
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 29px;
    position: relative;
    transition: all .4s ease;
}}

.agent.active .agent-circle {{
    border: 2px solid #ff6b4e;
    box-shadow:
        0 0 0 10px rgba(255,107,78,.07),
        0 0 30px rgba(255,107,78,.25);
    animation: activeAgent 1.5s infinite;
}}

@keyframes activeAgent {{
    0%,100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.07); }}
}}

.agent.completed .agent-circle {{
    border: 2px solid #42be4c;
    box-shadow:
        0 0 0 9px rgba(66,190,76,.07),
        0 0 25px rgba(66,190,76,.2);
}}

.agent.completed .agent-circle:after {{
    content: "✓";
    position: absolute;
    right: -3px;
    bottom: -3px;
    width: 22px;
    height: 22px;
    background: #16a447;
    color: white;
    border-radius: 50%;
    font-size: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: checkPop .4s ease both;
}}

@keyframes checkPop {{
    from {{ transform: scale(0); }}
    to {{ transform: scale(1); }}
}}

.agent-name {{
    margin-top: 12px;
    font-size: 13px;
    font-weight: 600;
    color: {TEXT};
}}

.agent-status {{
    display: inline-block;
    margin-top: 8px;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 10px;
    background: #eef0f1;
    color: #687078;
}}

.agent.active .agent-status {{
    background: #fff0e9;
    color: #f05a30;
}}

.agent.completed .agent-status {{
    background: #e8f8e9;
    color: #15963d;
}}

.agent-time {{
    margin-top: 8px;
    color: {MUTED};
    font-size: 10px;
}}

/* =====================================================
   FINAL CARD
===================================================== */

.final-card {{
    position: relative;
    overflow: hidden;
    margin-top: 16px;
    padding: 22px 28px;
    min-height: 115px;
    background:
        radial-gradient(circle at 80% 20%, rgba(54,213,105,.14), transparent 25%),
        {CARD};
    border: 1px solid {BORDER};
    border-radius: 17px;
    box-shadow: 0 12px 35px rgba(10,40,30,.05);
}}

.final-card:before {{
    content: "";
    position: absolute;
    width: 700px;
    height: 90px;
    bottom: -45px;
    left: 25%;
    background:
        repeating-linear-gradient(
            -12deg,
            transparent 0 12px,
            rgba(58,207,105,.07) 13px 15px
        );
    animation: hillsMove 8s linear infinite;
}}

@keyframes hillsMove {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100px); }}
}}

.final-content {{
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    gap: 18px;
}}

.document {{
    width: 65px;
    height: 75px;
    background: white;
    border-radius: 6px;
    box-shadow: 0 7px 20px rgba(0,0,0,.1);
    position: relative;
    transform: rotate(-4deg);
    animation: docFloat 3s ease-in-out infinite;
}}

@keyframes docFloat {{
    0%,100% {{ transform: translateY(0) rotate(-4deg); }}
    50% {{ transform: translateY(-5px) rotate(1deg); }}
}}

.document:before {{
    content: "";
    position: absolute;
    left: 12px;
    right: 12px;
    top: 18px;
    height: 3px;
    background: #40be55;
    box-shadow:
        0 9px #dce4df,
        0 18px #dce4df,
        0 27px #dce4df;
}}

.download {{
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: #25b749;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
    margin-left: -18px;
    box-shadow: 0 5px 20px rgba(30,180,70,.3);
    animation: downloadPulse 2s infinite;
}}

/* Final button override - BLACK background + WHITE text */
[data-testid="stDownloadButton"] button,
[data-testid="stDownloadButton"] button p,
[data-testid="stDownloadButton"] button span,
.download-wrap button,
.download-wrap button p {{
    color: #ffffff !important;
    background: #000000 !important;
    opacity: 1 !important;
}}

[data-testid="stDownloadButton"] button:hover,
.download-wrap button:hover {{
    color: #ffffff !important;
    background: #111111 !important;
}}

div[data-testid="stButton"] button:not([aria-label="Switch theme"]) {{
    color: #ffffff !important;
    background: #000000 !important;
    border: none !important;
}}

div[data-testid="stButton"] button:not([aria-label="Switch theme"]):hover {{
    color: #ffffff !important;
    background: #111111 !important;
}}

/* Keep Generate button black even if other button styles load later */
.generate-wrap button,
.generate-wrap button:hover,
.generate-wrap button:focus,
.generate-wrap button:active {{
    background: #000000 !important;
    color: #ffffff !important;
    border: none !important;
}}

.hero {{
    margin-bottom: .25rem !important;
}}

.workspace {{
    padding: 14px !important;
    margin-top: .35rem !important;
}}

.final-card + br,
.final-card ~ br {{
    display: none !important;
}}

@keyframes downloadPulse {{
    0%,100% {{ box-shadow: 0 5px 20px rgba(30,180,70,.3); }}
    50% {{ box-shadow: 0 5px 30px rgba(30,180,70,.65); }}
}}

.final-title {{
    font-size: 19px;
    font-weight: 700;
    color: {TEXT};
}}

.final-sub {{
    color: {MUTED};
    font-size: 13px;
    margin-top: 7px;
}}

.spark {{
    position: absolute;
    width: 4px;
    height: 4px;
    background: #55cf75;
    border-radius: 50%;
    animation: sparkle 2s infinite;
}}

@keyframes sparkle {{
    0% {{ transform: translateY(20px) scale(0); opacity: 0; }}
    50% {{ transform: translateY(0) scale(1); opacity: 1; }}
    100% {{ transform: translateY(-25px) scale(0); opacity: 0; }}
}}


/* =========================================================
   MOBILE RESPONSIVE OVERRIDES
   Desktop UI remains unchanged; these rules apply only
   to tablets and phones.
   ========================================================= */

@media (max-width: 768px) {{

    /* Main page spacing */
    .main .block-container {{
        max-width: 100% !important;
        padding: 8px 14px 40px !important;
    }}

    /* Keep the hero clean on small screens */
    .hero {{
        min-height: auto !important;
        padding: 4px 2px 8px !important;
    }}

    .hero-title {{
        font-size: clamp(34px, 10vw, 48px) !important;
        line-height: 1.04 !important;
        letter-spacing: -1.8px !important;
        max-width: 100% !important;
    }}

    .hero-desc {{
        font-size: 14px !important;
        line-height: 1.6 !important;
        max-width: 100% !important;
        margin-top: 14px !important;
    }}

    /* Decorative desktop chart is hidden instead of
       squeezing/overlapping the hero content */
    .graph-box {{
        display: none !important;
    }}

    /* Business idea card */
    .workspace {{
        padding: 14px !important;
        margin-top: 8px !important;
        border-radius: 14px !important;
    }}

    .workspace-title {{
        font-size: 15px !important;
        gap: 9px !important;
        margin-bottom: 10px !important;
    }}

    textarea {{
        min-height: 105px !important;
        font-size: 15px !important;
    }}

    .generate-wrap {{
        margin-top: 12px !important;
    }}

    .generate-wrap button {{
        height: 50px !important;
        font-size: 14px !important;
    }}


    /* Keep Streamlit warning visually consistent with desktop */
    [data-testid="stAlert"] {{
        width: 100% !important;
        box-sizing: border-box !important;
        margin: 12px 0 16px !important;
        padding: 12px 16px !important;
        min-height: 56px !important;
        border-radius: 9px !important;
        font-size: 14px !important;
        line-height: 1.4 !important;
    }}

    [data-testid="stAlert"],
    [data-testid="stAlert"] *,
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {{
        opacity: 1 !important;
        visibility: visible !important;
        color: #9a6700 !important;
        -webkit-text-fill-color: #9a6700 !important;
    }}

    [data-testid="stAlert"] {{
        background: #fffbd6 !important;
    }}

    /* Analysis status card becomes a vertical layout */
    .status-card {{
        padding: 18px 14px !important;
        border-radius: 15px !important;
    }}

    .status-content {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        gap: 16px !important;
    }}

    .ai-orb {{
        width: 68px !important;
        height: 68px !important;
        min-width: 68px !important;
    }}

    .robot {{
        font-size: 26px !important;
    }}

    .status-info {{
        width: 100% !important;
        min-width: 0 !important;
    }}

    .status-title {{
        font-size: 18px !important;
        line-height: 1.35 !important;
    }}

    .status-sub {{
        font-size: 13px !important;
        line-height: 1.55 !important;
    }}

    .badges {{
        width: 100% !important;
        justify-content: center !important;
        flex-wrap: wrap !important;
    }}

    .badge-small {{
        font-size: 10px !important;
        padding: 6px 9px !important;
    }}

    .progress-row {{
        width: 100% !important;
        gap: 10px !important;
    }}

    .progress-number {{
        font-size: 18px !important;
        min-width: 42px !important;
    }}

    /* Hide the decorative radar on phones */
    .radar {{
        display: none !important;
    }}

    /* IMPORTANT: the five-agent desktop flex row was
       overflowing on mobile. Use a 2-column grid. */
    .pipeline {{
        padding: 18px 10px !important;
        border-radius: 15px !important;
        overflow: hidden !important;
    }}

    .pipeline-row {{
        display: grid !important;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 22px 8px !important;
        align-items: start !important;
    }}

    .pipeline-line,
    .energy-line {{
        display: none !important;
    }}

    .agent {{
        width: 100% !important;
        min-width: 0 !important;
    }}

    .agent-circle {{
        width: 58px !important;
        height: 58px !important;
        font-size: 24px !important;
    }}

    .agent-name {{
        margin-top: 9px !important;
        font-size: 12px !important;
        line-height: 1.35 !important;
        overflow-wrap: anywhere !important;
    }}

    .agent-status {{
        margin-top: 6px !important;
        padding: 4px 8px !important;
        font-size: 9px !important;
    }}

    .agent-time {{
        margin-top: 6px !important;
        font-size: 9px !important;
    }}

    /* Final result card */
    .final-card {{
        padding: 18px 14px !important;
        min-height: auto !important;
        border-radius: 15px !important;
    }}

    .final-content {{
        flex-direction: column !important;
        text-align: center !important;
        gap: 12px !important;
    }}

    .final-title {{
        font-size: 17px !important;
    }}

    .final-sub {{
        font-size: 12px !important;
        line-height: 1.55 !important;
    }}

    /* Download/result columns should not create narrow
       desktop-style spacing on mobile */
    [data-testid="column"] {{
        min-width: 0 !important;
    }}
}}

/* Extra-small phones */
@media (max-width: 480px) {{

    .main .block-container {{
        padding-left: 10px !important;
        padding-right: 10px !important;
    }}

    .hero-title {{
        font-size: 35px !important;
        letter-spacing: -1.5px !important;
    }}

    .hero-desc {{
        font-size: 13px !important;
    }}

    .workspace {{
        padding: 12px !important;
    }}

    .pipeline {{
        padding: 16px 7px !important;
    }}

    .pipeline-row {{
        gap: 20px 5px !important;
    }}

    .agent-circle {{
        width: 54px !important;
        height: 54px !important;
        font-size: 22px !important;
    }}

    .agent-name {{
        font-size: 11px !important;
    }}

    .agent-status,
    .agent-time {{
        font-size: 8.5px !important;
    }}

    .status-card {{
        padding: 16px 11px !important;
    }}

    .badge-small {{
        width: 100% !important;
        text-align: center !important;
    }}
}}

</style>
""",
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.html(
        textwrap.dedent("""
        <div class="brand">
            <div class="brand-title">
                <span class="brand-star">✦</span>
                Analyst Desk
            </div>
            <div class="brand-sub">
                Mistral AI · RAG · LangGraph
            </div>
        </div>
        """),
    )

    st.html(
        textwrap.dedent("""
        <div class="live-card">
            <div class="live-row">
                <div class="live-dot"></div>
                <span>Live analysis</span>

                <div class="wave">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
        """),
    )

    st.markdown(
        '<div class="sidebar-heading">What you receive</div>',
        unsafe_allow_html=True
    )

    nav_items = [
        ("📈", "Market research"),
        ("▱", "Competitor analysis"),
        ("▣", "Financial planning"),
        ("⚠", "Risk assessment"),
        ("📣", "Marketing strategy")
    ]

    for i, (icon, name) in enumerate(nav_items):

        active_class = "active" if i == st.session_state.active_agent else ""

        st.html(
            textwrap.dedent(f"""
            <div class="nav-item {active_class}">
                <span class="nav-icon">{icon}</span>
                <span>{name}</span>
            </div>
            """),
        )

    st.html(
        textwrap.dedent("""
        <div class="enterprise">
            <div class="enterprise-icon">♢</div>

            <div class="enterprise-title">
                Enterprise-grade AI
            </div>

            <div class="enterprise-text">
                Multi-agent system working together
                to deliver a comprehensive plan.
            </div>
        </div>
        """),
    )

# =========================================================
# TOP BAR
# =========================================================

top1, top2 = st.columns([15, 1])

with top2:

    st.markdown('<div class="theme-button">', unsafe_allow_html=True)

    theme_icon = "☀" if not dark else "☾"

    if st.button(
        theme_icon,
        key="theme_toggle",
        help="Switch theme"
    ):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.html(
    textwrap.dedent("""
    <div class="hero">

        <div class="hero-title">
            Build a business plan<br>
            with sharper thinking.
        </div>

        <div class="hero-desc">
            Describe your idea and our AI team will analyze it across
            <span class="green-text">5 key dimensions</span>
            to create a practical business plan you can evaluate,
            refine, and download.
        </div>

        <div class="graph-box">

            <svg class="chart-svg"
                 viewBox="0 0 430 220">

                <defs>
                    <linearGradient
                        id="areaGradient"
                        x1="0"
                        y1="0"
                        x2="0"
                        y2="1">

                        <stop
                            offset="0%"
                            stop-color="#ff5262"
                            stop-opacity=".20"/>

                        <stop
                            offset="100%"
                            stop-color="#ff5262"
                            stop-opacity="0"/>
                    </linearGradient>
                </defs>

                <path
                    d="M20 190
                       C55 185,55 160,85 155
                       S120 175,145 140
                       S175 100,205 120
                       S240 95,260 105
                       S295 65,315 80
                       S345 60,365 73
                       S390 50,410 30"
                    fill="none"
                    stroke="#ff4e55"
                    stroke-width="3"
                    class="chart-line"/>

                <path
                    d="M20 190
                       C55 185,55 160,85 155
                       S120 175,145 140
                       S175 100,205 120
                       S240 95,260 105
                       S295 65,315 80
                       S345 60,365 73
                       S390 50,410 30
                       L410 210
                       L20 210 Z"
                    fill="url(#areaGradient)"/>

                <circle class="chart-point"
                        cx="85"
                        cy="155"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="145"
                        cy="140"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="205"
                        cy="120"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="260"
                        cy="105"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="315"
                        cy="80"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="365"
                        cy="73"
                        r="4"
                        fill="#ff4e55"/>

                <circle class="chart-point"
                        cx="410"
                        cy="30"
                        r="5"
                        fill="#ff4e55"/>

            </svg>

            <div class="insight-card">
                <div class="insight-small">
                    Insight trend
                </div>

                <div class="insight-value">
                    ↑ 28%
                </div>
            </div>

        </div>

    </div>
    """),
)

# =========================================================
# BUSINESS INPUT
# =========================================================

# =========================================================
# BUSINESS INPUT
# =========================================================

st.html(
    textwrap.dedent("""
    <div class="workspace-title">
        <span class="bulb">♧</span>
        <span>What are you building?</span>
    </div>
    """)
)

# Make placeholder clearly visible
st.markdown(
    """
    <style>
    textarea::placeholder {
        color: #6b7280 !important;
        opacity: 1 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

idea = st.text_area(
    "",
    placeholder="I want to open a coffee shop in Delhi",
    height=90,
    max_chars=500,
    key="business_idea",
    label_visibility="collapsed"
)

st.markdown('<div class="generate-wrap">', unsafe_allow_html=True)

generate = st.button(
    "✣   Generate my business plan",
    key="generate",
    use_container_width=True
)

# =========================================================
# GENERATE BUTTON ACTION
# =========================================================

if generate:

    if not idea.strip():

        st.warning("Please describe your business idea first.")

    else:

        st.session_state.running = True
        st.session_state.completed = False
        st.session_state.active_agent = 0
        st.session_state.progress = 0

        st.rerun()

# =========================================================
# ANALYSIS ANIMATION
# =========================================================

agents = [
    ("📈", "Market research"),
    ("♧", "Competitor analysis"),
    ("▣", "Financial planning"),
    ("⚠", "Risk assessment"),
    ("📣", "Marketing strategy")
]

if st.session_state.running:

    progress_placeholder = st.empty()
    pipeline_placeholder = st.empty()
    status_placeholder = st.empty()

    total_agents = len(agents)

    for i, (icon, name) in enumerate(agents):

        st.session_state.active_agent = i

        # -------------------------------------------------
        # STATUS
        # -------------------------------------------------

        progress_value = int((i / total_agents) * 100)

        if i == 0:
            message = "Analyzing market size, demand, and growth potential..."
        elif i == 1:
            message = "Studying competitors and finding market gaps..."
        elif i == 2:
            message = "Building revenue, cost, and financial projections..."
        elif i == 3:
            message = "Evaluating risks, challenges, and mitigation..."
        else:
            message = "Creating the final marketing strategy..."

        # -------------------------------------------------
        # STATUS CARD
        # -------------------------------------------------

        status_placeholder.html(
            textwrap.dedent(f"""
            <div class="status-card">

                <div class="status-content">

                    <div class="ai-orb">
                        <div class="robot">🤖</div>
                    </div>

                    <div class="status-info">

                        <div class="status-title">
                            Your analyst team is working
                            <span class="dot"></span>
                        </div>

                        <div class="status-sub">
                            {message}
                        </div>

                        <div class="badges">

                            <div class="badge-small">
                                ◷ Usually takes 1–2 minutes
                            </div>

                            <div class="badge-small">
                                ✦ Live analysis in progress
                            </div>

                        </div>

                        <div class="progress-row">

                            <div class="progress-track">

                                <div
                                    class="progress-fill"
                                    style="width:{max(progress_value,8)}%;">
                                </div>

                            </div>

                            <div class="progress-number">
                                {max(progress_value,8)}%
                            </div>

                        </div>

                    </div>

                    <div class="radar">

                        <div class="radar-circle r1"></div>
                        <div class="radar-circle r2"></div>
                        <div class="radar-circle r3"></div>

                        <div class="radar-scan"></div>

                    </div>

                </div>

            </div>
            """),
        )

        # -------------------------------------------------
        # PIPELINE
        # -------------------------------------------------

        pipeline_html = """
        <div class="pipeline">

            <div class="pipeline-row">

                <div class="pipeline-line"></div>
        """

        for j, (agent_icon, agent_name) in enumerate(agents):

            if j < i:
                cls = "agent completed"
                status = "Completed"
                time_text = "✓ Done"

            elif j == i:
                cls = "agent active"
                status = "In progress"
                time_text = f"00:{random.randint(20,59):02d}"

            else:
                cls = "agent"
                status = "Pending"
                time_text = "Est. 00:30"

            pipeline_html += f"""
                <div class="{cls}">

                    <div class="agent-circle">
                        {agent_icon}
                    </div>

                    <div class="agent-name">
                        {j + 1}. {agent_name}
                    </div>

                    <div class="agent-status">
                        {status}
                    </div>

                    <div class="agent-time">
                        ◷ {time_text}
                    </div>

                </div>
            """

        pipeline_html += """
            </div>
        </div>
        """

        pipeline_placeholder.html(textwrap.dedent(pipeline_html))

        # -------------------------------------------------
        # ANIMATION DELAY
        # -------------------------------------------------

        time.sleep(1.5)

    # =====================================================
    # COMPLETED
    # =====================================================

    # Run the real RAG + LangGraph pipeline after the visual progress phase.
    try:
        from rag.retriever import get_vector_store
        from graph.workflow import business_analyst_workflow

        get_vector_store()
        initial_state = {
            "business_idea": idea,
            "market_research": None,
            "competitor_analysis": None,
            "financial_plan": None,
            "risk_analysis": None,
            "marketing_strategy": None,
            "final_report": None,
            "current_step": "starting",
            "error": None,
        }
        analysis_result = business_analyst_workflow.invoke(initial_state)
        if analysis_result.get("error"):
            raise RuntimeError(analysis_result["error"])
        st.session_state.analysis_result = analysis_result
        st.session_state.analysis_idea = idea
    except Exception as exc:
        st.session_state.running = False
        st.error(f"Could not generate the business plan: {exc}")
        st.stop()

    st.session_state.running = False
    st.session_state.completed = True
    st.session_state.active_agent = 4
    st.session_state.progress = 100

    st.rerun()

# =========================================================
# COMPLETED STATE
# =========================================================

elif st.session_state.completed:

    st.html(
        textwrap.dedent("""
        <div class="status-card">

            <div class="status-content">

                <div class="ai-orb">
                    <div class="robot">✓</div>
                </div>

                <div class="status-info">

                    <div class="status-title">
                        Analysis complete
                        <span
                            class="dot"
                            style="background:#22b557;">
                        </span>
                    </div>

                    <div class="status-sub">
                        Your business plan has been generated successfully.
                    </div>

                    <div class="badges">

                        <div class="badge-small">
                            ✓ 5 dimensions analyzed
                        </div>

                        <div class="badge-small">
                            ✓ AI analysis complete
                        </div>

                    </div>

                    <div class="progress-row">

                        <div class="progress-track">

                            <div
                                class="progress-fill"
                                style="width:100%;">
                            </div>

                        </div>

                        <div class="progress-number">
                            100%
                        </div>

                    </div>

                </div>

                <div class="radar">

                    <div class="radar-circle r1"></div>
                    <div class="radar-circle r2"></div>
                    <div class="radar-circle r3"></div>

                    <div style="
                        position:absolute;
                        left:50%;
                        top:50%;
                        transform:translate(-50%,-50%);
                        font-size:38px;
                        color:#23a84d;
                    ">
                        ✓
                    </div>

                </div>

            </div>

        </div>
        """),
    )

    # -----------------------------------------------------
    # FINAL PIPELINE
    # -----------------------------------------------------

    pipeline_html = """
    <div class="pipeline">

        <div class="pipeline-row">

            <div
                class="pipeline-line"
                style="background:#48c957;">
            </div>

            <div
                class="energy-line"
                style="width:86%;">
            </div>
    """

    for j, (agent_icon, agent_name) in enumerate(agents):

        pipeline_html += f"""
            <div class="agent completed">

                <div class="agent-circle">
                    {agent_icon}
                </div>

                <div class="agent-name">
                    {j + 1}. {agent_name}
                </div>

                <div class="agent-status">
                    Completed
                </div>

                <div class="agent-time">
                    ✓ Done
                </div>

            </div>
        """

    pipeline_html += """
        </div>
    </div>
    """

    st.html(textwrap.dedent(pipeline_html))

    # =====================================================
    # FINAL RESULT
    # =====================================================

    st.html(
        textwrap.dedent("""
        <div class="final-card">

            <div class="spark" style="left:8%;top:40%;animation-delay:.2s"></div>
            <div class="spark" style="left:22%;top:25%;animation-delay:.7s"></div>
            <div class="spark" style="left:50%;top:40%;animation-delay:1.2s"></div>
            <div class="spark" style="left:75%;top:30%;animation-delay:.5s"></div>
            <div class="spark" style="left:90%;top:55%;animation-delay:1.5s"></div>

            <div class="final-content">

                <div class="document"></div>

                <div class="download">
                    ↓
                </div>

                <div>

                    <div class="final-title">
                        Your business plan is ready!
                    </div>

                    <div class="final-sub">
                        Review, edit and download your comprehensive
                        business plan.
                    </div>

                </div>

            </div>

        </div>
        """),
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "⬇  Download business plan",
            use_container_width=True
        ):

            plan = st.session_state.analysis_result.get(
                "final_report",
                "Final report not generated.",
            )

            st.download_button(
                label="Download TXT",
                data=plan,
                file_name="business_plan.txt",
                mime="text/plain",
                use_container_width=True
            )

    # Show the real synthesized output directly in the UI.
    report = st.session_state.analysis_result.get(
        "final_report",
        "Final report not generated.",
    )
    st.markdown("## Generated business plan")
    st.markdown(report)

# =========================================================
# DEFAULT STATE
# =========================================================

else:

    st.html(
        textwrap.dedent("""
        <div class="status-card">

            <div class="status-content">

                <div class="ai-orb">
                    <div class="robot">🤖</div>
                </div>

                <div class="status-info">

                    <div class="status-title">
                        Your analyst team is ready
                        <span class="dot"></span>
                    </div>

                    <div class="status-sub">
                        Describe your business idea and start the
                        five-agent analysis.
                    </div>

                    <div class="badges">

                        <div class="badge-small">
                            ◷ Usually takes 1–2 minutes
                        </div>

                        <div class="badge-small">
                            ✦ 5 AI specialists
                        </div>

                    </div>

                    <div class="progress-row">

                        <div class="progress-track">
                            <div
                                class="progress-fill"
                                style="width:3%;">
                            </div>
                        </div>

                        <div class="progress-number">
                            0%
                        </div>

                    </div>

                </div>

                <div class="radar">

                    <div class="radar-circle r1"></div>
                    <div class="radar-circle r2"></div>
                    <div class="radar-circle r3"></div>

                    <div class="radar-scan"></div>

                </div>

            </div>

        </div>
        """),
    )

    # =====================================================
    # INITIAL PIPELINE
    # =====================================================

    pipeline_html = """
    <div class="pipeline">

        <div class="pipeline-row">

            <div class="pipeline-line"></div>
    """

    for j, (agent_icon, agent_name) in enumerate(agents):

        pipeline_html += f"""
            <div class="agent">

                <div class="agent-circle">
                    {agent_icon}
                </div>

                <div class="agent-name">
                    {j + 1}. {agent_name}
                </div>

                <div class="agent-status">
                    Pending
                </div>

                <div class="agent-time">
                    ◷ Est. 00:30
                </div>

            </div>
        """

    pipeline_html += """
        </div>
    </div>
    """

    st.html(textwrap.dedent(pipeline_html))

    # =====================================================
    # READY MESSAGE
    # =====================================================

    st.html(
        textwrap.dedent("""
        <div class="final-card">

            <div class="final-content">

                <div class="document"></div>

                <div>

                    <div class="final-title">
                        Your business plan will be ready soon!
                    </div>

                    <div class="final-sub">
                        Once complete, you'll be able to review,
                        edit and download your plan.
                    </div>

                </div>

            </div>

        </div>
        """),
    )
