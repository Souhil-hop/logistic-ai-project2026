import streamlit as st

# 1. إعداد الصفحة بالعرض الواسع
st.set_page_config(page_title="منصة سهيل اللوجستية المتكاملة", layout="wide")

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
    .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.1);
        border: 2px solid #d4af37;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: #d4af37;
        margin: 20px 0;
    }
    .footer { 
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0d1117; color: #d4af37; 
        text-align: center; padding: 10px; border-top: 1px solid #d4af37; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الرسمي لجامعة محمد خيضر
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 المنصة المتكاملة للتنبؤ ودعم القرار اللوجستي")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. واجهة المدخلات الشاملة
with st.container():
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📍 تفاصيل المسار")
        start_p = st.text_input("نقطة الانطلاق (Origin)", value="بسكرة")
        end_p = st.text_input("نقطة الوصول (Destination)", value="ميناء الجزائر")
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0)
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms)", ["EXW", "FOB", "CIF"])
        
    with col_b:
        st.markdown("### 💵 المعطيات المالية والتقنية")
        wght = st.number_input("الوزن القائم (طن)", value=5.0)
        fuel_price = st.number_input("سعر الوقود (د.ج/لتر)", value=29.1)
        profit_perc = st.slider("هامش الربح المستهدف (%)", 5, 50, 20)
        truck_type = st.selectbox("نوع الشاحنة المختارة", ["شاحنة صغيرة", "شاحنة متوسطة", "مقطورة دولية", "تبريد"])

# 5. خوارزمية الحساب الشاملة
if st.button("تشغيل التحليل اللوجستي الشامل"):
    t_map = {"شاحنة صغيرة": 1.0, "شاحنة متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    
    def get_cost(t_type_key):
        base = ((dist * 0.6) + (wght * 250)) * t_map[t_type_key]
        fuel = (dist / 5) * fuel_price
        maint = base * 0.15
        total = (base + fuel + maint) * (1 + profit_perc/100) + 1500
        return total, fuel, maint, base

    # حساب الخيار المختار
    total_dzd, f_cost, m_cost, b_cost = get_cost(truck_type)
    profit_val = (b_cost + f_cost + m_cost) * (profit_perc / 100)

    # أ) عرض النتيجة الأساسية
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 25px; border-radius: 15px; text-align: center; color: black; margin: 20px auto; max-width: 800px; border: 2px solid white;">
            <h2 style="margin:0;">💰 التكلفة المقدرة للخيار المختار</h2>
            <h1 style="margin:5px 0; font-size: 45px;">{total_dzd:,.2f} د.ج</h1>
            <p>المسار: من {start_p} إلى {end_p} (قاعدة {incoterm})</p>
        </div>
    """, unsafe_allow_html=True)

    # ب) هيكلة التكاليف (Cost Breakdown)
    st.markdown("### 📋 هيكلة التكاليف التفصيلية")
    st.table({
        "بند التكلفة": ["الوقود", "الصيانة", "التشغيل الأساسي", f"هامش الربح ({profit_perc}%)"],
        "القيمة (د.ج)": [f"{f_cost:,.2f}", f"{m_cost:,.2f}", f"{b_cost:,.2f}", f"{profit_val:,.2f}"]
    })

    st.write("---")

    # ج) نظام المقارنة ودعم القرار (الجديد)
    st.markdown("### 📊 نظام دعم القرار (مقارنة السيناريوهات)")
    cost_moyen = get_cost("شاحنة متوسطة")[0]
    cost_semi = get_cost("مقطورة دولية")[0]
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("تكلفة الشاحنة المتوسطة", f"{cost_moyen:,.2f} د.ج")
    with col_res2:
        st.metric("تكلفة المقطورة الدولية", f"{cost_semi:,.2f} د.ج")

    # التوصية الذكية
    if wght <= 3.5:
        rec = "💡 التوصية: حمولتك خفيفة، استخدام شاحنة متوسطة سيوفر لك ميزانية معتبرة."
    else:
        rec = "💡 التوصية: وزن الحمولة كبير، المقطورة الدولية هي الخيار الأكثر أماناً واستقراراً."
    
    st.markdown(f"<div class='recommendation-box'>{rec}</div>", unsafe_allow_html=True)

    st.balloons()

    # د) نظام التقييم (Feedback)
    st.markdown("---")
    st.write("🧪 **هل تجد نتائج هذا التحليل الشامل دقيقة؟**")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("✅ نعم، تحليل دقيق"): st.success("تم تسجيل تقييمك بنجاح.")
    with col_f2:
        if st.button("❌ يحتاج مراجعة"): st.warning("شكراً، سيتم تحديث الخوارزمية.")

# 6. الفوتر الثابت
st.markdown(f'<div class="footer">مشروع التخرج: سهيل - تخصص اللوجستيك والنقل الدولي - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
