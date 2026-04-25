import streamlit as st
import pandas as pd
import time
from geopy.distance import geodesic

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة التنبؤ بتكاليف النقل اللوجستي", page_icon="📊", layout="wide")

# إحداثيات الولايات
coords = {
    "07. بسكرة": (34.8516, 5.7281), "16. الجزائر": (36.7538, 3.0588),
    "19. سطيف": (36.1911, 5.4133), "31. وهران": (35.6987, -0.6359),
    "23. عنابة": (36.9000, 7.7667), "25. قسنطينة": (36.3650, 6.6147),
    "30. ورقلة": (31.9493, 5.3250), "39. الوادي": (33.3683, 6.8674),
    "47. غرداية": (32.4909, 3.6733), "01. أدرار": (27.8742, -0.2939),
    "05. باتنة": (35.5559, 6.1741), "09. البليدة": (36.4700, 2.8277)
}

if 'page' not in st.session_state: st.session_state.page = 'welcome'

# --- كود CSS الشامل لإصلاح كل العيوب ---
st.markdown("""
    <style>
    /* تثبيت الخلفية في كل الصفحات */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("https://images.unsplash.com/photo-1519003722824-192d992a605b?q=80&w=1500");
        background-size: cover;
        background-attachment: fixed;
    }
    .main-card { background: rgba(0, 0, 0, 0.85); padding: 20px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; }
    
    /* المربع الذهبي - توضيح الكتابة */
    .result-card {
        background: linear-gradient(45deg, #d4af37, #f4cf67);
        padding: 25px; border-radius: 20px; text-align: center; border: 3px solid #ffffff;
    }
    .result-card h1, .result-card h2, .result-card h3, .result-card p {
        color: #000000 !important; /* أسود غامق للوضوح */
        font-weight: 900 !important;
    }
    h1, h2, h3, label { color: #d4af37 !important; }
    p, .stMarkdown { color: white !important; }
    .stTable { background-color: rgba(255, 255, 255, 0.1) !important; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الترحيب (الرجوع للأصل) ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="color:#d4af37;">مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2 style="color:white;">جامعة محمد خيضر - كلية العلوم الاقتصادية</h2>
            <hr style="border-color:#d4af37;">
            <div style="margin:30px 0;">
                <h3 style="color:#d4af37;">ماهي المنصة؟</h3>
                <p>المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة <b>keras</b> للتنبؤ بتكاليف النقل اللوجستي.</p>
            </div>
            <h3 style="color:#d4af37;">إعداد الطلبة:</h3>
            <p style="font-size:24px; font-weight:bold;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل"):
        st.session_state.page = 'main'
        st.rerun()

# --- الصفحة الثانية: التحليل ---
elif st.session_state.page == 'main':
    if st.button("⬅️ رجوع"):
        st.session_state.page = 'welcome'
        st.rerun()
    
    # العنوان الأصلي
    st.markdown("<h1 style='text-align:center; color:#d4af37;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📍 تفاصيل المسار")
        start = st.selectbox("🚩 نقطة الانطلاق", list(coords.keys()), index=0)
        end = st.selectbox("🏁 نقطة الوصول", list(coords.keys()), index=1)
        raw_dist = geodesic(coords[start], coords[end]).km
        dist = st.number_input("📏 المسافة (كم)", value=round(raw_dist, 2))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📦 معطيات الشحنة")
        c_type = st.selectbox("🍎 نوع البضاعة", ["مواد غذائية", "أدوية", "إلكترونيات", "مواد بناء"])
        truck = st.selectbox("🚛 نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        wght = st.number_input("⚖️ الوزن (كغ)", value=1000.0)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 توليد التقرير النهائي"):
        start_time = time.time()
        with st.spinner('جاري معالجة البيانات عبر الشبكة العصبية...'):
            time.sleep(1.2) # محاكاة وقت المعالجة
            
            cargo_m = {"أدوية": 1.3, "مواد غذائية": 1.1, "إلكترونيات": 1.2, "مواد بناء": 1.0}
            truck_m = {"صغيرة": 1.0, "متوسطة": 1.4, "تبريد": 2.2, "مقطورة دولية": 2.8}
            
            base = ((dist * 0.9) + ((wght/1000) * 450)) * truck_m[truck] * cargo_m[c_type]
            total = base * 1.35
            duration = round(time.time() - start_time, 2)

            # المربع الذهبي بوضوح عالي
            st.markdown(f"""
                <div class="result-card">
                    <p style="font-size:20px;">التكلفة التقديرية النهائية</p>
                    <h1 style="font-size:50px;">{total:,.2f} د.ج</h1>
                    <p>نوع الشحنة: {c_type} | الوقت المستغرق: {duration} ثانية</p>
                </div>
            """, unsafe_allow_html=True)

            # الجدول الأول: تفاصيل التكاليف
            st.markdown("### 📋 أولاً: تفاصيل التكاليف")
            details = {
                "العنصر": ["المسافة", "الوزن", "نوع الشاحنة", "نوع البضاعة", "الوقت المستغرق"],
                "القيمة": [f"{dist} كم", f"{wght} كغ", truck, c_type, f"{duration} ثانية"]
            }
            st.table(pd.DataFrame(details))

            # الجدول الثاني: المقارنة
            st.markdown("### 🔄 ثانياً: جدول مقارنة البدائل")
            comp = []
            for name, factor in truck_m.items():
                c = (((dist * 0.9) + ((wght/1000) * 450)) * factor * cargo_m[c_type]) * 1.35
                comp.append({"نوع الشاحنة": name, "التكلفة (د.ج)": f"{c:,.2f}"})
            st.table(pd.DataFrame(comp))

    st.markdown("<br><hr><p style='text-align:center;'>إعداد: سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>", unsafe_allow_html=True)
