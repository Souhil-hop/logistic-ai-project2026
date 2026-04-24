import streamlit as st
import plotly.graph_objects as go
import time

# 1. إعدادات متقدمة
st.set_page_config(page_title="SOUHAIL LOGISTICS AI", layout="wide")

# 2. تصميم نيون مستقبلي (Modern Dark Tech)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background-color: #050505;
    }
    
    /* تصميم البطاقات */
    .tech-card {
        background: #0a0a0a;
        border-left: 5px solid #00f2ff;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.1);
    }
    
    /* تغيير الخط للعنوان */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        text-shadow: 0 0 10px #00f2ff;
    }
    
    /* الأزرار */
    .stButton>button {
        background: transparent;
        color: #00f2ff !important;
        border: 2px solid #00f2ff !important;
        border-radius: 0px;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background: #00f2ff !important;
        color: black !important;
        box-shadow: 0 0 20px #00f2ff;
    }
    
    label { color: #888 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر
st.markdown("<h1 class='main-title'>SOUHAIL AI ENGINE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444;'>LOGISTICS PREDICTION SYSTEM v2.0</p>", unsafe_allow_html=True)

# 4. التقسيم
col_left, col_right = st.columns([1, 1.5])

with col_left:
    st.markdown('<div class="tech-card">', unsafe_allow_html=True)
    st.write("### ⚙️ SYSTEM INPUTS")
    start = st.text_input("ORIGIN", "BISKRA")
    end = st.text_input("DESTINATION", "ALGIERS")
    dist = st.slider("DISTANCE (KM)", 10, 1000, 400)
    weight = st.number_input("LOAD (TONS)", 0.1, 50.0, 1.0)
    truck = st.selectbox("VEHICLE TYPE", ["Standard", "Refrigerated", "Heavy Duty"])
    st.markdown('</div>', unsafe_allow_html=True)

# 5. الحسابات
t_cost = {"Standard": 1.0, "Refrigerated": 1.7, "Heavy Duty": 2.5}
prediction = ((dist * 0.8) + (weight * 350)) * t_cost[truck] + 3000

with col_right:
    # رسم بياني أسود ونيون
    st.write("### 📊 ANALYTICS")
    w_vals = [i for i in range(1, 21)]
    p_vals = [(((dist * 0.8) + (i * 350)) * t_cost[truck] + 3000) for i in w_vals]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=w_vals, y=p_vals, mode='lines', line=dict(color='#00f2ff', width=4)))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00f2ff'), margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig, use_container_width=True)

# 6. النتيجة بطريقة الـ Terminal
if st.button("EXECUTE PREDICTION"):
    placeholder = st.empty()
    with placeholder.container():
        st.write("📡 Scanning routes...")
        time.sleep(0.5)
        st.write("🧠 Computing Neural Weights...")
        time.sleep(0.5)
    
    placeholder.markdown(f"""
        <div style="border: 2px solid #00f2ff; padding: 20px; text-align: center; background: rgba(0, 242, 255, 0.05);">
            <h4 style="color: #00f2ff; margin: 0;">PREDICTED LOGISTICS COST</h4>
            <h1 style="color: #fff; font-size: 50px; margin: 10px 0; text-shadow: 0 0 15px #00f2ff;">
                {prediction:,.2f} <span style="font-size: 20px;">DZD</span>
            </h1>
            <p style="color: #888;">ROUTE: {start} >> {end}</p>
        </div>
    """, unsafe_allow_html=True)

# 7. الفوتر
st.markdown("<br><br><p style='text-align: center; color: #222;'>DEVELOPED BY SOUHAIL | CORE_AI_v2.0</p>", unsafe_allow_html=True)
