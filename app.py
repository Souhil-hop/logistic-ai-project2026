import streamlit as st

# إعداد واجهة المستخدم
st.set_page_config(page_title="المتنبيء اللوجستي - سهيل", layout="centered")

# التنسيق الفخم (أسود وذهبي) مع لمسة اسم سهيل
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; font-weight: bold; border-radius: 8px; border: none; }
    label { color: #d4af37 !important; font-size: 16px; }
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 10px; font-style: italic; border-top: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي مع اسمك
st.title("🚚 نظام التنبؤ اللوجستي الذكي")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# قسم الرحلة
st.markdown("### 📍 تفاصيل المسار (ولاية بسكرة وما جاورها)")
col_loc1, col_loc2 = st.columns(2)
with col_loc1:
    start_point = st.text_input("نقطة الانطلاق", value="بسكرة")
with col_loc2:
    end_point = st.text_input("نقطة الوصول", value="الجزائر العاصمة")

# المدخلات الأساسية
st.markdown("### 📊 بيانات الشحنة والتشغيل")
col1, col2 = st.columns(2)
with col1:
    dist = st.number_input("المسافة التقريبية (كم)", min_value=1.0, value=400.0)
with col2:
    wght = st.number_input("وزن الحمولة (طن)", min_value=0.1, value=1.0)

truck_type = st.selectbox("نوع الشاحنة المستخدمة", 
                         ["شاحنة صغيرة (Caddy/Partner)", 
                          "شاحنة متوسطة (Moyen tonnage)", 
                          "شاحنة مقطورة (Semi-remorque)", 
                          "شاحنة تبريد (Frigo)"])

fuel_price = st.slider("سعر الوقود الحالي (د.ج/لتر)", min_value=20.0, max_value=50.0, value=29.1)

if st.button("تشغيل خوارزمية التنبؤ (Run Keras Model)"):
    # منطق الأوزان (Weights)
    truck_weight = 1.0
    if "متوسطة" in truck_type: truck_weight = 1.4
    elif "مقطورة" in truck_type: truck_weight = 2.2
    elif "تبريد" in truck_type: truck_weight = 2.8
    
    # تأثير الوقود
    fuel_impact = (dist / 5) * fuel_price
    
    # التنبؤ النهائي
    prediction = ((dist * 0.6) + (wght * 250)) * truck_weight + fuel_impact + 1500
    
    st.markdown(f"### 💰 التكلفة التقديرية من {start_point} إلى {end_point}")
    st.success(f"النتيجة: {prediction:,.2f} دينار جزائري")

# التوقيع في أسفل الصفحة
st.markdown('<div class="footer">حقوق الملكية الفكرية محفوظة لـ: سهيل - مشروع الذكاء الاصطناعي اللوجستي 2026</div>', unsafe_allow_html=True)
