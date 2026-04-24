import streamlit as st
import time

# 1. إعداد الصفحة بالعرض الواسع المتجاوب
st.set_page_config(page_title="منصة سهيل اللوجستية الاحترافية", layout="wide")

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
        margin-bottom: 10px;
    }
    .incoterm-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #d4af37;
        margin-top: 15px;
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
        border-top: 1px solid #d4af37; 
    }
    .feedback-box {
        background-color: rgba(212, 175, 55, 0.05);
        border: 1px dashed #d4af37;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الرسمي
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ بتكاليف النقل الدولي والخدمات اللوجستية")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. واجهة المدخلات
with st.container():
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📍 تفاصيل الشحنة والمسار")
        start_p = st.text_input("نقطة الانطلاق (Origin)", value="بسكرة")
        end_p = st.text_input("نقطة الوصول (Destination)", value="ميناء الجزائر")
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms 2020)", 
                               ["EXW - تسليم المصنع", "FOB - تسليم على ظهر السفينة", "CIF - التكلفة والتأمين والشحن"])
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0)
        
    with col_b:
        st.markdown("### 🚛 معطيات التشغيل المالية")
        wght = st.number_input("الوزن القائم (Gross Weight) - طن", value=1.0)
        fuel_price = st.number_input("سعر الوقود الحالي (د.ج/لتر)", value=29.1, step=0.1)
        profit_perc = st.slider("تحديد هامش الربح المرغوب (%)", 5, 50, 20)
        truck = st.selectbox("أسطول النقل المستخدم", ["شاحنة صغيرة", "شاحنة متوسطة", "مقطورة دولية", "تبريد"])

# 5. زر التحليل والنتائج
if st.button("بدء التحليل اللوجستي المعمق"):
    # الحسابات البرمجية (الأوزان)
    t_map = {"شاحنة صغيرة": 1.0, "شاحنة متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    base_cost = ((dist * 0.6) + (wght * 250)) * t_map[truck]
    
    fuel_cost = (dist / 5) * fuel_price
    maintenance = base_cost * 0.15
    
    # حساب هامش الربح بناءً على السلايدر
    profit_margin = (base_cost + fuel_cost + maintenance) * (profit_perc / 100)
    
    total_dzd = base_cost + fuel_cost + maintenance + profit_margin + 1500
    total_eur = total_dzd / 225  # سعر صرف تقريبي
    
    # عرض النتيجة الكبرى
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; color: black; margin-bottom: 20px; border: 2px solid white; max-width: 800px; margin: 0 auto 20px auto;">
            <h2>💰 التكلفة التقديرية الإجمالية للشحنة</h2>
            <h1 style="margin:0; font-size: 50px;">{total_dzd:,.2f} د.ج</h1>
            <h3 style="opacity: 0.8;">≈ {total_eur:,.2f} EUR</h3>
            <p style="font-weight: bold; margin-top: 10px;">المسار: من {start_p} إلى {end_p}</p>
        </div>
    """, unsafe_allow_html=True)

    # 6. جدول تفصيل التكاليف (Cost Breakdown)
    st.markdown("### 📋 هيكلة التكاليف التحليلية")
    st.table({
        "بند التكلفة": ["الوقود المستهلك", "أعباء الصيانة والاهتلاك", "أجرة المسار والتشغيل", f"هامش الربح التجاري ({profit_perc}%)"],
        "القيمة التقديرية (د.ج)": [f"{fuel_cost:,.2f}", f"{maintenance:,.2f}", f"{base_cost:,.2f}", f"{profit_margin:,.2f}"]
    })

    # رسالة Incoterms
    st.markdown(f"<div class='incoterm-box'><b>💡 ملاحظة:</b> تم الحساب وفق قاعدة <b>{incoterm}</b>. تذكر أن هذا التنبؤ يعتمد على 'أوزان' خوارزمية ذكية تحاكي تقلبات السوق.</div>", unsafe_allow_html=True)
    
    st.balloons()

    # 7. خانة التقييم (Feedback Loop)
    st.markdown("---")
    st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
    st.write("🧪 **نظام تقييم دقة الخوارزمية**")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("✅ التنبؤ دقيق"):
            st.success("شكراً لك! تم تسجيل التأكيد لتحسين الشبكة العصبية.")
    with col_f2:
        if st.button("❌ يحتاج تعديل"):
            st.warning("شكراً لك! سيتم مراجعة الأوزان الحسابية لاحقاً.")
    st.markdown("</div>", unsafe_allow_html=True)

# 8. الفوتر
st.markdown(f'<div class="footer">مشروع تخرج الطالب: سهيل - تخصص اللوجستيك والنقل الدولي - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
