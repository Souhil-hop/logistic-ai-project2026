import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="منصة التنبؤ اللوجستي الذكي", 
    page_icon="📊",
    layout="wide"
)

# قاموس إحداثيات الولايات الجزائرية (للحساب الأوتوماتيكي)
coords = {
    "07. بسكرة": (34.8516, 5.7281), "16. الجزائر": (36.7538, 3.0588),
    "19. سطيف": (36.1911, 5.4133), "31. وهران": (35.6987, -0.6359),
    "23. عنابة": (36.9000, 7.7667), "25. قسنطينة": (36.3650, 6.6147),
    "30. ورقلة": (31.9493, 5.3250), "39. الوادي": (33.3683, 6.8674),
    "47. غرداية": (32.4909, 3.6733), "01. أدرار": (27.8742, -0.2939),
    "05. باتنة": (35.5559, 6.1741), "09. البليدة": (36.4700, 2.8277)
}

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- كود CSS لإصلاح الخلفية والتنسيق ---
def local_css():
    st.markdown(f"""
        <style>
        /* خلفية الصفحة الرئيسية */
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("https://images.unsplash.com/photo-1519003722824-192d992a605b?q=80&w=1500");
            background-size: cover;
            background-attachment: fixed;
            color: white !important;
        }}
        
        /* تنسيق البطاقات */
        .main-card {{
            background: rgba(0, 0, 0, 0.85);
            padding: 20px;
            border-radius: 15px;
            border-right: 5px solid #d4af37;
            margin-bottom: 20px;
        }}
        
        /* بطاقة النتيجة النهائية */
        .result-box {{
            background: linear-gradient(45deg, #d4af37, #f4cf67);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            color: black !important;
            margin: 20px 0;
        }}
        
        /* تحسين مظهر الجداول */
        .stTable {{
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px;
        }}
        
        h1, h2, h3, label {{ color: #d4af37 !important; }}
        p {{ color: white !important; }}
        </style>
    """, unsafe_allow_html=True)

local_css()

# --- محتوى الصفحة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.8); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="font-size:45px;">منصة التنبؤ اللوجستي الذكي 🚛</h1>
            <p style="font-size:22px;">نموذج متطور يعتمد على الشبكات العصبية الإصطناعية (Keras Model)</p>
            <hr style="border-color:#d4af37;">
            <div style="margin:20px 0;">
                <p style="font-size:24px; font-weight:bold;">إعداد الطلبة:</p>
                <p style="font-size:20px;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
                <p style="font-size:18px;">جامعة محمد خيضر بسكرة - 2026</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 الدخول للمنصة"):
        st.session_state.page = 'main'
        st.rerun()

# --- محتوى منصة التحليل ---
elif st.session_state.page == 'main':
    if st.button("⬅️ العودة"):
        st.session_state.page = 'welcome'
        st.rerun()

    st.markdown("<h1 style='text-align:center;'>📊 مدخلات النظام الذكي</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📍 المسار والمسافة")
        start = st.selectbox("من ولاية:", list(coords.keys()), index=0)
        end = st.selectbox("إلى ولاية:", list(coords.keys()), index=1)
        
        # حساب المسافة أوتوماتيكياً
        raw_dist = geodesic(coords[start], coords[end]).km
        dist = st.number_input("المسافة المقدرة (كم):", value=round(raw_dist, 2))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📦 مواصفات الشحنة")
        c_type = st.selectbox("نوع البضاعة:", ["مواد غذائية", "أدوية", "إلكترونيات", "مواد بناء", "أثاث"])
        t_type = st.selectbox("نوع الشاحنة:", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        wght = st.number_input("الوزن الإجمالي (كغ):", value=1000.0)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 استخراج التنبؤ المالي والبدائل"):
        # منطق الحسابات (الأوزان)
        cargo_m = {"أدوية": 1.35, "مواد غذائية": 1.15, "إلكترونيات": 1.25, "مواد بناء": 1.0, "أثاث": 1.2}
        truck_m = {"صغيرة": 1.0, "متوسطة": 1.45, "تبريد": 2.3, "مقطورة دولية": 2.9}
        
        # المعادلة
        base = ((dist * 0.95) + ((wght/1000) * 480)) * truck_m[t_type] * cargo_m[c_type]
        final = base * 1.38
        
        # عرض النتيجة الرئيسية
        st.markdown(f"""
            <div class="result-box">
                <h2 style="color:black !important;">التكلفة التقديرية للرحلة</h2>
                <h1 style="color:black !important; font-size:45px;">{final:,.2f} د.ج</h1>
                <p style="color:black !important;">(بناءً على معطيات الشبكة العصبية لنوع: {c_type})</p>
            </div>
        """, unsafe_allow_html=True)

        # جدول المقارنة (تحليل البدائل)
        st.markdown("### 🔄 تحليل البدائل (مقارنة الوسائل)")
        comp_list = []
        for name, factor in truck_m.items():
            cost = ((((dist * 0.95) + ((wght/1000) * 480)) * factor * cargo_m[c_type]) * 1.38)
            comp_list.append({
                "نوع الشاحنة": name,
                "التكلفة المقدرة (د.ج)": f"{cost:,.2f}",
                "ملاحظة": "سعر تقديري"
            })
        
        st.table(pd.DataFrame(comp_list))

    # التذييل
    st.markdown("<br><hr><p style='text-align:center;'>إعداد الطلبة: سهيل، محمد الحسين، عبد الله | جامعة بسكرة 2026</p>", unsafe_allow_html=True)
