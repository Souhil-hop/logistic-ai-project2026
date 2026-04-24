import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main():
    st.session_state.page = 'main'

# --- الصفحة الأولى: الواجهة الترحيبية المحدثة بالصور ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        /* تثبيت الخلفية لتملأ كامل الشاشة */
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url("https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&q=80&w=1500");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .welcome-box {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            border: 2px solid #d4af37;
            margin: auto;
            max-width: 800px;
            margin-top: 50px;
        }
        .welcome-title { color: #d4af37; font-size: 40px; font-weight: bold; }
        .welcome-desc { color: #ffffff; font-size: 22px; line-height: 1.6; margin-top: 20px; }
        .stButton>button { 
            background-color: #d4af37 !important; 
            color: black !important; 
            font-weight: bold !important;
            font-size: 20px !important;
            border-radius: 12px !important;
            height: 60px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="welcome-box">
            <h1 class="welcome-title">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <p class="welcome-desc">
                هذا النظام عبارة عن <b>مشروع محاكاة لشبكة عصبية</b> باستخدام لغة البايثون (Python).
                تم تصميمه للتنبؤ بتكاليف النقل اللوجستي، مما يوفر أداة دقيقة لدعم القرار وتحليل سيناريوهات النقل المختلفة.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # مساحة
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: النظام الرئيسي ---
elif st.session_state.page == 'main':
    st.markdown("""
        <style>
        .stApp { background: #0d1117; }
        .main-header { text-align: center; color: #d4af37; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
        label { color: #d4af37 !important; font-weight: bold; }
        .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 5px; border-top: 1px solid #d4af37; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 class='main-header'>📦 المنصة المتكاملة للتنبؤ ودعم القرار</h2>", unsafe_allow_html=True)
    
    if st.sidebar.button("🏠 العودة للرئيسية"):
        st.session_state.page = 'welcome'
        st.rerun()

    # المدخلات
    col1, col2 = st.columns(2)
    with col1:
        start_p = st.selectbox("نقطة الانطلاق", ["بسكرة", "الجزائر", "سطيف", "وهران"])
        end_p = st.selectbox("نقطة الوصول", ["ميناء الجزائر", "ميناء جنجن", "ميناء وهران"])
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0)
    with col2:
        wght_kg = st.number_input("الوزن القائم (كغ)", value=1000.0)
        fuel_p = st.number_input("سعر الوقود (د.ج)", value=29.1)
        chosen_truck = st.selectbox("نوع الشاحنة المعنية بالتحليل", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])

    if st.button("التكلفة النهائية"):
        st.balloons()
        
        # خوارزمية الحساب
        t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
        w_t = wght_kg / 1000.0
        base_cost = ((dist * 0.7) + (w_t * 300)) * t_map[chosen_truck]
        fuel_cost = (dist / 5) * fuel_p
        maint = base_cost * 0.12
        profit = (base_cost + fuel_cost + maint) * 0.20
        total = base_cost + fuel_cost + maint + profit

        # 1. التكلفة الكبيرة
        st.markdown(f"""
            <div style="background-color: #d4af37; padding: 30px; border-radius: 15px; text-align: center; color: black; margin: 20px 0;">
                <h1 style="margin:0;">{total:,.2f} د.ج</h1>
                <p><b>التكلفة المقدرة للخيار المختار</b></p>
            </div>
        """, unsafe_allow_html=True)

        # 2. هيكلة التكاليف (الجدول الذي كان ناقصاً)
        st.markdown("### 📋 هيكلة التكاليف التفصيلية")
        st.table({
            "بند التكلفة": ["تكلفة الوقود الأساسية", "الصيانة والاهتلاك", "أجرة المسار والتشغيل", "هامش الربح (20%)"],
            "القيمة المقدرة (د.ج)": [f"{fuel_cost:,.2f}", f"{maint:,.2f}", f"{base_cost:,.2f}", f"{profit:,.2f}"]
        })

        # 3. جدول المقارنة
        st.write("---")
        st.markdown("### 📊 جدول المقارنة الشامل")
        comp_data = []
        for t, m in t_map.items():
            c = ((dist * 0.7) + (w_t * 300)) * m + fuel_cost + (base_cost*0.12) + profit
            comp_data.append({"نوع الشاحنة": t, "التكلفة الكلية (د.ج)": round(c, 2)})
        
        df = pd.DataFrame(comp_data)
        st.dataframe(df.style.highlight_min(axis=0, color='#28a745'), use_container_width=True)

        # 4. التوصية ورأي المستخدم
        st.info(f"💡 التوصية: بناءً على معطياتك، نظام الشبكة العصبية يقترح خيار '{chosen_truck}' كأكثر استقراراً لهذه المسافة.")
        
        st.write("---")
        st.markdown("### 🧪 خانة رأي المستخدم")
        opinion = st.radio("ما رأيك في دقة النتائج؟", ["دقيقة جداً", "تحتاج تعديل بسيط", "غير منطقية"])
        if st.button("إرسال التقييم"):
            st.success("شكراً لك! سيتم استخدام تقييمك لتدريب النموذج بشكل أفضل.")

    st.markdown("<div class='footer'>مشروع التخرج: سهيل - تخصص اللوجستيك - جامعة بسكرة 2026</div>", unsafe_allow_html=True)
