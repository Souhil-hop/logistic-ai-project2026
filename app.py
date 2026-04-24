import streamlit as st

# 1. التعديل الجوهري: جعل العرض واسعاً (wide) ليتأقلم مع الكمبيوتر
st.set_page_config(page_title="المتنبيء اللوجستي - سهيل", layout="wide")

# 2. التنسيق الفخم (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { 
        background-color: #d4af37; 
        color: black; 
        width: 100%; 
        font-weight: bold; 
        border-radius: 8px; 
        border: none; 
        height: 50px; 
    }
    label { color: #d4af37 !important; font-size: 16px; }
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; margin-top: 0px; }
    .university-header {
        text-align: center;
        color: #d4af37;
        font-weight: bold;
        font-size: 18px;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }
    /* تحسين العرض في الشاشات الكبيرة */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 90% !important;
    }
    .footer { 
        position: fixed; 
        left: 0; 
        bottom: 0; 
        width: 100%; 
        background-color: #0d1117; 
        color: #d4af37; 
        text-align: center; 
        padding: 10px; 
        font-style: italic; 
        border-top: 1px solid #d4af37; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (برعاية الجامعة)
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة</div>", unsafe_allow_html=True)

# 4. العنوان الرئيسي واسم المطور (سهيل)
st.title("🚚 نظام التنبؤ اللوجستي الذكي")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# باستخدام الحاويات لضمان مظهر جيد في العرض الواسع
with st.container():
    # 5. قسم مسار الرحلة
    st.markdown("### 📍 مسار الرحلة")
    col_loc1, col_loc2 = st.columns(2)
    with col_loc1:
        start_point = st.text_input("نقطة الانطلاق", value="بسكرة")
    with col_loc2:
        end_point = st.text_input("نقطة الوصول", value="الجزائر العاصمة")

    # 6. المدخلات الأساسية للبيانات
    st.markdown("### 📊 بيانات التشغيل")
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

    # 7. زر التنبؤ
    if st.button("بدء تحليل البيانات اللوجستية"):
        truck_weight = 1.0
        if "متوسطة" in truck_type: truck_weight = 1.4
        elif "مقطورة" in truck_type: truck_weight = 2.2
        elif "تبريد" in truck_type: truck_weight = 2.8
        
        fuel_impact = (dist / 5) * fuel_price
        prediction = ((dist * 0.6) + (wght * 250)) * truck_weight + fuel_impact + 1500
        
        st.markdown(f"""
            <div style="background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; border: 2px solid white; max-width: 600px; margin: 0 auto;">
                <h2 style="color: black; margin: 0;">💰 التكلفة التقديرية</h2>
                <p style="color: black; font-size: 38px; font-weight: bold; margin: 10px 0;">
                    {prediction:,.2f} <span style="font-size: 20px;">د.ج</span>
                </p>
                <p style="color: #333; font-size: 16px; margin: 0; font-weight: bold;">المسار: من {start_point} إلى {end_point}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

# 8. التوقيع الثابت (الفوتر)
st.markdown(f'<div class="footer">المشروع التطبيقي للطالب: سهيل - جميع الحقوق محفوظة لولاية بسكرة 2026</div>', unsafe_allow_html=True)
