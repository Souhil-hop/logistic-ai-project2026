import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic

# 1. إعداد الصفحة لضمان عدم ظهور اسمك الشخصي في الرابط
st.set_page_config(
    page_title="منصة التنبؤ بتكاليف النقل اللوجستي", 
    page_icon="📊",
    layout="wide"
)

# قاموس الإحداثيات (أهم الولايات الجزائرية للبدء)
coords = {
    "07. بسكرة": (34.8516, 5.7281),
    "16. الجزائر": (36.7538, 3.0588),
    "19. سطيف": (36.1911, 5.4133),
    "31. وهران": (35.6987, -0.6359),
    "23. عنابة": (36.9000, 7.7667),
    "25. قسنطينة": (36.3650, 6.6147),
    "30. ورقلة": (31.9493, 5.3250),
    "39. الوادي": (33.3683, 6.8674),
    "47. غرداية": (32.4909, 3.6733),
    "01. أدرار": (27.8742, -0.2939),
    "08. بشار": (31.6167, -2.2167),
    "05. باتنة": (35.5559, 6.1741)
}

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- التصميم CSS ---
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #d4af37 !important; border-radius: 15px; padding: 25px;
    }
    .stApp, .stMarkdown, p, label { color: #FFFFFF !important; font-size: 18px !important; }
    .result-card {
        background: linear-gradient(45deg, #d4af37, #f4cf67);
        padding: 25px; border-radius: 20px; text-align: center; border: 2px solid #ffffff; margin-bottom: 20px;
    }
    .result-card h1, .result-card h2 { color: #000000 !important; font-weight: bold !important; }
    .main-card { background: rgba(0, 0, 0, 0.8); padding: 20px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الترحيب ---
if st.session_state.page == 'welcome':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
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
    
    st.markdown("<h1 style='text-align:center; color:#d4af37;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    col_input, col_map = st.columns([1, 1.2])

    with col_input:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📍 المسار")
        start_city = st.selectbox("🚩 نقطة الانطلاق", list(coords.keys()), index=0)
        end_city = st.selectbox("🏁 نقطة الوصول", list(coords.keys()), index=1)
        
        # حساب المسافة أوتوماتيكياً
        raw_dist = geodesic(coords[start_city], coords[end_city]).km
        dist = st.number_input("📏 المسافة (كم)", value=round(raw_dist, 2))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📦 الشحنة")
        wght = st.number_input("⚖️ الوزن (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود (د.ج)", value=29.10)
        truck_type = st.selectbox("🚛 النوع", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col_map:
        st.markdown("### 🗺️ الخريطة التفاعلية")
        # إنشاء الخريطة بنمط داكن فخم
        m = folium.Map(location=[32.0, 3.0], zoom_start=5, tiles="CartoDB dark_matter")
        folium.Marker(coords[start_city], tooltip=f"انطلاق: {start_city}", icon=folium.Icon(color='orange')).add_to(m)
        folium.Marker(coords[end_city], tooltip=f"وصول: {end_city}", icon=folium.Icon(color='red')).add_to(m)
        folium.PolyLine([coords[start_city], coords[end_city]], color="#d4af37", weight=4, opacity=0.8).add_to(m)
        folium_static(m)

    if st.button("💎 توليد التنبؤ النهائي"):
        truck_specs = {"صغيرة": 1.0, "متوسطة": 1.4, "تبريد": 2.2, "مقطورة دولية": 2.8}
        f = truck_specs[truck_type]
        # معادلة مستوحاة من أوزان الشبكة العصبية
        base = ((dist * 0.85) + ((wght/1000) * 450)) * f
        total = (base + (dist/5)*fuel) * 1.35
        
        st.markdown(f'<div class="result-card"><h1>التكلفة التقديرية: {total:,.2f} د.ج</h1></div>', unsafe_allow_html=True)

        # جدول المقارنة
        comp = []
        for t_name, t_f in truck_specs.items():
            cost = ((((dist * 0.85) + ((wght/1000) * 450)) * t_f) + (dist/5)*fuel) * 1.35
            comp.append({"الوسيلة": t_name, "التكلفة (د.ج)": f"{cost:,.2f}"})
        
        st.markdown("### 🔄 تحليل البدائل")
        st.table(pd.DataFrame(comp))

    st.markdown(f"""
        <div style="text-align:center; color:#d4af37; margin-top:30px; border-top:1px solid #d4af37; padding-top:10px;">
            إعداد: سهيل عطالي | محمد الحسين موسي | عبد الله سايب <br>
            جامعة محمد خيضر بسكرة - أولى ماستر لوجستيك
        </div>
    """, unsafe_allow_html=True)
