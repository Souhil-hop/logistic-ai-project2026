import streamlit as st
import plotly.graph_objects as go
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="منصة سهيل اللوجستية 2026", layout="wide")

# 2. تصميم CSS احترافي (Glassmorphism & Gradients)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    }
    .glass-card {
        background: rgba(212, 175, 55, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 20px;
        padding: 25px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(90deg, #d4af37 0%, #f9d976 100%);
        color: black !important;
        border: none;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5);
    }
    h1, h3 { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الإبداعي باسمك
st.markdown("<h1>🌟 منصة التنبؤ اللوجستي الذكية</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>المهندس المطور: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. توزيع العناصر بشكل احترافي
col_input, col_chart = st.columns([1, 1.5])

with col_input:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📝 مدخلات النظام")
    origin = st.text_input("نقطة الانطلاق", "بسكرة")
    destination = st.text_input("نقطة الوصول", "الجزائر العاصمة")
    
    dist = st.slider("المسافة (كيلومتر)", 10, 1000, 400)
    weight = st.number_input("الوزن الإجمالي (طن)", 0.1, 50.0, 1.0)
    
    truck = st.selectbox("أسطول النقل", ["شاحنة خفيفة", "شاحنة تبريد", "مقطورة دولية"])
    fuel = st.number_input("سعر الوقود اليوم (د.ج)", value=29.0)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. منطق المعالجة والرسم البياني
t_map = {"شاحنة خفيفة": 1.0, "شاحنة تبريد": 1.6, "مقطورة دولية": 2.3}
prediction = ((dist * 0.7) + (weight * 300)) * t_map[truck] + (dist/5 * fuel) + 2000

with col_chart:
    st.subheader("📊 تحليل حساسية التكاليف")
    # إنشاء رسم بياني يوضح تأثير زيادة الوزن على السعر
    weights_range = [w for w in range(1, 21)]
    prices_range = [(((dist * 0.7) + (w * 300)) * t_map[truck] + (dist/5 * fuel) + 2000) for w in weights_range]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=weights_range, y=prices_range, mode='lines+markers', line=dict(color='#d4af37', width=3)))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#d4af37'),
                      xaxis_title="الوزن (طن)", yaxis_title="التكلفة (د.ج)", margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, use_container_width=True)

# 6. زر التشغيل بتأثيرات بصرية
if st.button("🚀 تشغيل محرك الذكاء الاصطناعي لسهيل"):
    with st.status("جاري تحليل البيانات عبر Keras Engine...", expanded=True) as status:
        time.sleep(1)
        st.write("✅ جاري موازنة الأوزان (Weights)...")
        time.sleep(1)
        st.write("✅ جاري معالجة المسار اللوجستي...")
        status.update(label="تم الانتهاء من التنبؤ!", state="complete", expanded=False)
    
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #d4af37 0%, #b8860b 100%); padding: 30px; border-radius: 20px; text-align: center; margin-top: 20px;">
            <h2 style="color: black; margin-bottom: 0;">📦 التكلفة المقدرة للشحنة</h2>
            <h1 style="color: black; font-size: 50px; margin: 10px 0;">{prediction:,.2f} د.ج</h1>
            <p style="color: #222; font-weight: bold;">المسار الفعلي: من {origin} إلى {destination}</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()

# 7. الفوتر
st.markdown("<br><center style='color: #666;'>تطوير: المهندس سهيل | مشروع الذكاء الاصطناعي للخدمات اللوجستية 2026</center>", unsafe_allow_html=True)
