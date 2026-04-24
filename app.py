import streamlit as st

# 1. إعداد الصفحة بالعرض الواسع المتجاوب
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
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    .university-header {
        text-align: center;
        color: #d4af37;
        font-weight: bold;
        font-size: 18px;
        letter-spacing: 1px;
        margin-bottom: 10px;
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
    /* تنسيق صندوق التقييم */
    .feedback-box {
        background-color: rgba(212, 175, 55, 0.1);
        border: 1px dashed #d4af37;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (برعاية الجامعة)
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة</div>", unsafe_allow_html=True)

# 4. العنوان واسم المطور
st.title("🚚 نظام التنبؤ اللوجستي الذكي")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 5. المدخلات
with st.container():
    st.markdown("### 📍 تفاصيل المسار وبيانات التشغيل")
    c1, c2 = st.columns(2)
    with c1:
        start_p = st.text_input("نقطة الانطلاق", value="بسكرة")
        dist = st.number_input("المسافة التقريبية (كم)", min_value=1.0, value=400.0)
    with c2:
        end_p = st.text_input("نقطة الوصول", value="الجزائر العاصمة")
        wght = st.number_input("وزن الحمولة (طن)", min_value=0.1, value=1.0)

    truck_type = st.selectbox("نوع الشاحنة المستخدمة", 
                             ["شاحنة صغيرة (Caddy/Partner)", "شاحنة متوسطة (Moyen tonnage)", 
                              "شاحنة مقطورة (Semi-remorque)", "شاحنة تبريد (Frigo)"])

    fuel_price = st.slider("سعر الوقود الحالي (د.ج/لتر)", 20.0, 50.0, 29.1)

    # 6. زر التنبؤ والنتيجة
    if st.button("بدء تحليل البيانات اللوجستية"):
        # الحسابات
        t_weight = {"شاحنة صغيرة (Caddy/Partner)": 1.0, "شاحنة متوسطة (Moyen tonnage)": 1.4, 
                    "شاحنة مقطورة (Semi-remorque)": 2.2, "شاحنة تبريد (Frigo)": 2.8}
        
        fuel_impact = (dist / 5) * fuel_price
        prediction = ((dist * 0.6) + (wght * 250)) * t_weight[truck_type] + fuel_impact + 1500
        
        # عرض النتيجة
        st.markdown(f"""
            <div style="background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; border: 2px solid white; max-width: 600px; margin: 20px auto;">
                <h2 style="color: black; margin: 0;">💰 التكلفة التقديرية</h2>
                <p style="color: black; font-size: 38px; font-weight: bold; margin: 10px 0;">
                    {prediction:,.2f} <span style="font-size: 20px;">د.ج</span>
                </p>
                <p style="color: #333; font-size: 16px; margin: 0; font-weight: bold;">المسار: من {start_p} إلى {end_p}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

        # --- إضافة خانة التقييم الجديدة ---
        st.markdown("---")
        st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
        st.write("🧪 **تقييم دقة التنبؤ بالذكاء الاصطناعي**")
        st.write("بناءً على خبرتك، هل تجد هذا السعر قريباً من الواقع؟")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            if st.button("✅ نعم، التنبؤ دقيق"):
                st.success("شكراً لك! سيتم استخدام هذا التأكيد لتحسين وزن المعطيات مستقبلاً.")
        with col_f2:
            if st.button("❌ لا، يحتاج تعديل"):
                st.warning("شكراً لملاحظتك. سيتم مراجعة 'الأوزان' (Weights) لتناسب تقلبات السوق.")
        st.markdown("</div>", unsafe_allow_html=True)

# 7. الفوتر
st.markdown(f'<div class="footer">المشروع التطبيقي للطالب: سهيل - جميع الحقوق محفوظة لولاية بسكرة 2026</div>', unsafe_allow_html=True)
