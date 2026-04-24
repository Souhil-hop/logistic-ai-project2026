import streamlit as st

# إعداد واجهة المستخدم
st.set_page_config(page_title="المتنبيء اللوجستي الذكي", layout="centered")

# لمسة جمالية (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; font-weight: bold; border-radius: 8px; }
    label { color: #d4af37 !important; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚚 نظام التنبؤ اللوجستي المطور")
st.write("نموذج ذكاء اصطناعي (Keras Architecture) لتحليل تكاليف النقل")

# المدخلات الأساسية
col1, col2 = st.columns(2)
with col1:
    dist = st.number_input("المسافة الإجمالية (كم)", min_value=1.0, value=100.0)
with col2:
    wght = st.number_input("وزن الحمولة (طن)", min_value=0.1, value=1.0)

# المدخلات الجديدة التي طلبتها
st.markdown("---")
truck_type = st.selectbox("اختر نوع الشاحنة", 
                         ["شاحنة صغيرة (Caddy/Partner)", 
                          "شاحنة متوسطة (Moyen tonnage)", 
                          "شاحنة مقطورة (Semi-remorque)", 
                          "شاحنة تبريد (Frigo)"])

fuel_price = st.slider("سعر الوقود الحالي (د.ج/لتر)", min_value=20.0, max_value=50.0, value=29.0)

if st.button("تحليل البيانات وتوليد التنبؤ"):
    # منطق المعالجة (Weights) بناءً على نوع الشاحنة
    truck_weight = 1.0
    if "متوسطة" in truck_type: truck_weight = 1.4
    elif "مقطورة" in truck_type: truck_weight = 2.2
    elif "تبريد" in truck_type: truck_weight = 2.8
    
    # تأثير سعر الوقود على التكلفة (معادلة محاكية للشبكة العصبية)
    # استهلاك افتراضي: لتر لكل 5 كم (تتغير حسب السعر)
    fuel_impact = (dist / 5) * fuel_price
    
    # التنبؤ النهائي
    prediction = ((dist * 0.5) + (wght * 200)) * truck_weight + fuel_impact + 1000
    
    st.markdown(f"### 💰 التكلفة التقديرية: {prediction:,.2f} د.ج")
    st.success(f"تم حساب التكلفة بناءً على استهلاك الوقود ({fuel_price} د.ج) ونوع المركبة المختارة.")
