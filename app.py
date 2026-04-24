import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="منصة سهيل اللوجستية - نظام دعم القرار", layout="wide")

# 2. التنسيق الفخم
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 8px; width: 100%; height: 50px; }
    .recommendation-box {
        background-color: rgba(0, 255, 0, 0.1);
        border: 2px solid #00ff00;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: #00ff00;
        margin-top: 20px;
    }
    .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 10px; border-top: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | مختبر اللوجستيك الذكي</div>", unsafe_allow_html=True)
st.title("📊 نظام دعم القرار والتحليل المقارن")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>تطوير الطالب: سهيل</h3>", unsafe_allow_html=True)

# 4. مدخلات البيانات
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        dist = st.number_input("المسافة (كم)", value=400.0)
        fuel_p = st.number_input("سعر الوقود", value=29.1)
    with col2:
        wght = st.number_input("الوزن الإجمالي (طن)", value=5.0)
        profit = st.slider("هامش الربح (%)", 5, 50, 15)
    with col3:
        incoterm = st.selectbox("Incoterm", ["EXW", "FOB", "CIF"])

# 5. زر التحليل
if st.button("إجراء تحليل المقارنة اللوجستية"):
    # خوارزمية حساب خيارين
    # الخيار أ: شاحنة متوسطة (Moyen tonnage)
    # الخيار ب: شاحنة مقطورة (Semi-remorque)
    
    def calculate(truck_weight):
        base = ((dist * 0.6) + (wght * 250)) * truck_weight
        fuel = (dist / 5) * fuel_p
        maint = base * 0.15
        total = (base + fuel + maint) * (1 + profit/100) + 1500
        return total

    cost_moyen = calculate(1.4)
    cost_semi = calculate(2.2)

    # عرض المقارنة
    st.markdown("### 🔍 نتائج المقارنة بين وسائل النقل")
    c_m1, c_m2 = st.columns(2)
    
    with c_m1:
        st.metric(label="شاحنة متوسطة (Moyen Tonnage)", value=f"{cost_moyen:,.2f} د.ج", delta="- الأرخص" if cost_moyen < cost_semi else "")
    with c_m2:
        st.metric(label="شاحنة مقطورة (Semi-remorque)", value=f"{cost_semi:,.2f} د.ج", delta="- سعة أكبر" if cost_semi > cost_moyen else "")

    # القيمة المضافة: التوصية الآلية
    st.markdown("---")
    if wght <= 3:
        rec_text = "💡 التوصية: الشاحنة المتوسطة هي الأنسب اقتصادياً لحمولتك."
    else:
        rec_text = "💡 التوصية: يفضل استخدام المقطورة لضمان سلامة الحمولة وتجنب غرامات الوزن الزائد."
    
    st.markdown(f"<div class='recommendation-box'>{rec_text}</div>", unsafe_allow_html=True)
    
    # تفصيل التكاليف في جدول
    st.markdown("### 📝 تفصيل التكاليف للخيار الأنسب")
    chosen_cost = min(cost_moyen, cost_semi)
    st.table({
        "البند": ["تكلفة الوقود", "الصيانة", "هامش الربح", "المجموع النهائي"],
        "القيمة (د.ج)": [f"{(dist/5*fuel_p):,.2f}", f"{(chosen_cost*0.1):,.2f}", f"{(chosen_cost*(profit/100)):,.2f}", f"{chosen_cost:,.2f}"]
    })

st.markdown(f'<div class="footer">مشروع الطالب سهيل - تخصص اللوجستيك - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
