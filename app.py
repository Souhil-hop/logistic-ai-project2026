import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="مشروع سهيل اللوجستي", layout="centered")

# 2. التنسيق الجمالي
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; font-weight: bold; border-radius: 10px; height: 50px; }
    h1, h3 { text-align: center; color: #d4af37; }
    .result-card { background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. العناوين واسمك
st.title("🚚 نظام التنبؤ اللوجستي الذكي")
st.markdown("### تطوير المبرمج: سهيل")
st.write("---")

# 4. المدخلات
col1, col2 = st.columns(2)
with col1:
    start_p = st.text_input("من (المنطلق)", value="بسكرة")
    dist = st.number_input("المسافة (كم)", min_value=1.0, value=400.0)
with col2:
    end_p = st.text_input("إلى (الوصول)", value="العاصمة")
    wght = st.number_input("الوزن (طن)", min_value=0.1, value=1.0)

truck = st.selectbox("نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة", "تبريد"])
fuel = st.slider("سعر الوقود (د.ج)", 20.0, 50.0, 29.1)

# 5. زر التشغيل والنتيجة
if st.button("تشغيل خوارزمية سهيل 🚀"):
    # حسابات بسيطة محاكية لـ Keras
    t_weight = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة": 2.2, "تبريد": 2.8}
    prediction = ((dist * 0.6) + (wght * 250)) * t_weight[truck] + (dist/5 * fuel) + 1500
    
    # عرض النتيجة في أيقونة ذهبية
    st.markdown(f"""
        <div class="result-card">
            <h2>💰 التكلفة التقديرية</h2>
            <h1 style="color: black; font-size: 40px;">{prediction:,.2f} د.ج</h1>
            <p>المسار: من {start_p} إلى {end_p}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()

# 6. الحقوق
st.markdown("<br><hr><center>حقوق الملكية محفوظة للمطور سهيل - 2026</center>", unsafe_allow_html=True)
