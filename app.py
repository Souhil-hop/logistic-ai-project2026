import streamlit as st
import plotly.graph_objects as go
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="SOUHAIL AI | LOGISTICS", layout="wide")

# 2. لمسة التصميم المستقبلية
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #00f2ff22; }
    .main-header { font-size: 45px; font-weight: 800; color: #00f2ff; text-align: center; text-shadow: 0 0 20px #00f2ff44; margin-bottom: 30px; }
    .metric-card { background: #111; border: 1px solid #222; padding: 15px; border-radius: 10px; text-align: center; }
    .stButton>button { border-radius: 5px; border: 1px solid #00f2ff; background: transparent; color: #00f2ff; transition: 0.5s; width: 100%; font-size: 20px; }
    .stButton>button:hover { background: #00f2ff; color: #000; box-shadow: 0 0 30px #00f2ff; }
    </style>
""", unsafe_allow_html=True)

# 3. الشريط الجانبي (Inputs)
with st.sidebar:
    st.markdown("<h2 style='color:#00f2ff;'>⚙️ CONTROL PANEL</h2>", unsafe_allow_html=True)
    st.write("---")
    origin = st.text_input("📍 ORIGIN", "BISKRA")
    dest = st.text_input("🏁 DESTINATION", "ALGIERS")
    truck = st.selectbox("🚛 FLEET TYPE", ["Standard", "Refrigerated", "Heavy Duty", "Express Van"])
    fuel = st.number_input("⛽ FUEL PRICE (DZD)", 20.0, 60.0, 29.1)
    st.write("---")
    st.markdown(f"<p style='color:#888;'>Developed by: <b>SOUHAIL</b></p>", unsafe_allow_html=True)

# 4. الجسم الرئيسي
st.markdown("<div class='main-header'>SOUHAIL AI LOGISTICS HUB</div>", unsafe_allow_html=True)

# عرض أرقام سريعة (Top Metrics)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    dist = st.slider("DISTANCE (KM)", 10, 1200, 400)
with col_m2:
    weight = st.number_input("WEIGHT (TONS)", 0.1, 50.0, 1.0)
with col_m3:
    st.markdown(f"<div class='metric-card'><small>SELECTED VEHICLE</small><br><b style='color:#00f2ff;'>{truck}</b></div>", unsafe_allow_html=True)

st.write("---")

# 5. منطقة التحليلات والنتائج
col_left, col_right = st.columns([1.5, 1])

with col_left:
    # رسم بياني تفاعلي (Area Chart)
    t_multi = {"Standard": 1.0, "Refrigerated": 1.7, "Heavy Duty": 2.5, "Express Van": 1.2}
    w_range = list(range(1, 26))
    p_range = [((dist * 0.8) + (w * 350)) * t_multi[truck] + (dist/5 * fuel) + 2000 for w in w_range]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=w_range, y=p_range, fill='tozeroy', line_color='#00f2ff', name='Cost Curve'))
    fig.update_layout(title="Cost Analysis (Price vs Weight)", paper_bgcolor='rgba(0,0,0,0)', 
                      plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#00f2ff'),
                      xaxis=dict(gridcolor='#222'), yaxis=dict(gridcolor='#222'))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("EXECUTE AI ANALYSIS"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        prediction = ((dist * 0.8) + (weight * 350)) * t_multi[truck] + (dist/5 * fuel) + 2000
        
        st.markdown(f"""
            <div style="background: rgba(0, 242, 255, 0.05); border: 1px solid #00f2ff; padding: 25px; border-radius: 15px; text-align: center;">
                <p style="color: #888; text-transform: uppercase; letter-spacing: 2px;">Predicted Transport Cost</p>
                <h1 style="color: #fff; font-size: 55px; margin: 0; text-shadow: 0 0 15px #00f2ff;">{prediction:,.2f}</h1>
                <p style="color: #00f2ff; font-weight: bold;">DZD</p>
                <hr style="border-color: #222;">
                <p style="font-size: 14px;">ROUTE: {origin} ➔ {dest}</p>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

# تذييل الصفحة
st.markdown("<br><p style='text-align: center; color: #333;'>CORE_ENGINE_v3.0 © SOUHAIL DESIGN</p>", unsafe_allow_html=True)
