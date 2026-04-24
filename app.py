import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="منصة سهيل اللوجستية الاحترافية", layout="wide")

# 2. التنسيق (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 8px; width: 100%; height: 50px; }
    .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .incoterm-box { background-color: #161b22; padding: 10px; border-radius: 5px; border-left: 4px solid #d4af37; margin-bottom: 15px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 10px; border-top: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الرسمي
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ بتكاليف النقل الدولي والخدمات اللوجستية")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. واجهة المدخلات الاحترافية
with st.container():
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📍 تفاصيل الشحنة")
        start_p = st.text_input("نقطة الانطلاق (Origin)", value="بسكرة")
        end_p = st.text_input("نقطة الوصول (Destination)", value="ميناء الجزائر")
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms 2020)", 
                               ["EXW - تسليم المصنع", "FOB - تسليم على ظهر السفينة", "CIF - التكلفة والتأمين والشحن"])
        
    with col_b:
        st.markdown("### 🚛 معطيات النقل")
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0)
        wght = st.number_input("الوزن القائم (Gross Weight) - طن", value=1.0)
        truck = st.selectbox("أسطول النقل", ["شاحنة صغيرة", "شاحنة متوسطة", "مقطورة دولية", "تبريد"])

# 5. زر التحليل والنتائج
if st.button("بدء التحليل اللوجستي المعمق"):
    # حسابات تفصيلية
    t_map = {"شاحنة صغيرة": 1.0, "شاحنة متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    base_cost = ((dist * 0.6) + (wght * 250)) * t_map[truck]
    fuel_cost = (dist / 5) * 29.1
    maintenance = base_cost * 0.15
    profit_margin = (base_cost + fuel_cost + maintenance) * 0.20
    
    total_dzd = base_cost + fuel_cost + maintenance + profit_margin + 1500
    total_eur = total_dzd / 225  # سعر صرف تقريبي
    
    # عرض النتائج
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; color: black; margin-bottom: 20px;">
            <h2>💰 التكلفة التقديرية الإجمالية</h2>
            <h1 style="margin:0;">{total_dzd:,.2f} د.ج</h1>
            <h3>≈ {total_eur:,.2f} EUR</h3>
        </div>
    """, unsafe_allow_html=True)

    # جدول تفصيل التكاليف لطلبة اللوجستيك
    st.markdown("### 📋 تفصيل التكاليف (Cost Breakdown)")
    st.table({
        "البند": ["تكلفة الوقود", "الصيانة والاهتلاك", "أجرة المسار الأساسية", "هامش الربح (20%)"],
        "القيمة (د.ج)": [f"{fuel_cost:,.2f}", f"{maintenance:,.2f}", f"{base_cost:,.2f}", f"{profit_margin:,.2f}"]
    })

    # رسالة تعليمية حول الـ Incoterms
    st.markdown(f"<div class='incoterm-box'><b>ملاحظة لوجستية:</b> تم حساب التكلفة بناءً على قاعدة <b>{incoterm}</b>. يرجى التأكد من توزيع مسؤولية التأمين والرسوم الجمركية وفقاً للعقد.</div>", unsafe_allow_html=True)
    
    st.balloons()

# 6. الفوتر
st.markdown(f'<div class="footer">مشروع التخرج: سهيل - تخصص اللوجستيك والنقل الدولي - 2026</div>', unsafe_allow_html=True)
