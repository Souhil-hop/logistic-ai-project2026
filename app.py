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

# --- دالة CSS للتحكم في الخلفيات والألوان ---
def apply_theme(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{url}");
            background-size: cover; background-attachment: fixed; background-position: center;
        }}
        .main-card {{ background: rgba(0, 0, 0, 0.85); padding: 20px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; }}
        
        /* المربع الذهبي - النص بالأسود العريض */
        .result-card {{ background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 25px; border-radius: 20px; text-align: center; border: 3px solid #ffffff; }}
        .result-card h1, .result-card p, .result-card h3 {{ color: #000000 !important; font-weight: 900 !important; }}
        
        /* بقية العناوين والنصوص باللون الأبيض */
        h1, h2, h3, label, .stMarkdown p {{ color: #FFFFFF !important; }}
        
        .stTable {{ background-color: rgba(255, 255, 255, 0.1) !important; border-radius: 10px; }}
        
        /* التذييل باللون الأصفر وخط كبير */
        .footer-style {{
            text-align: center; 
            color: #d4af37 !important; 
            font-size: 22px !important; 
            font-weight: bold;
            margin-top: 50px;
            border-top: 1px solid #d4af37;
            padding-top: 20px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: الترحيب (خلفية سفينة حاويات واضحة) ---
if st.session_state.page == 'welcome':
    apply_theme("https://images.unsplash.com/photo-1494412519320-aa613dfb7738?q=80&w=1500") 
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="font-weight:bold;">مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2>جامعة محمد خيضر - كلية العلوم الاقتصادية</h2>
            <hr style="border-color:#d4af37;">
            <div style="margin:30px 0;">
                <h3>ماهي المنصة؟</h3>
                <p>المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة <b>keras</b> للتنبؤ بتكاليف النقل اللوجستي.</p>
            </div>
            <h3>إعداد الطلبة:</h3>
            <p style="font-size:24px; font-weight:bold;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل"):
        st.session_state.page = 'main'
        st.rerun()

# --- الصفحة الثانية: التحليل (خلفية مستودع) ---
elif st.session_state.page == 'main':
    apply_theme("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500") 
    if st.button("⬅️ رجوع"):
        st.session_state.page = 'welcome'
        st.rerun()
    
    st.markdown("<h1 style='text-align:center;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📍 تفاصيل المسار")
        start = st.selectbox("🚩 نقطة الانطلاق", list(coords.keys()), index=0)
        end = st.selectbox("🏁 نقطة الوصول", list(coords.keys()), index=1)
        raw_dist = geodesic(coords[start], coords[end]).km
        dist = st.number_input("📏 المسافة المحسوبة أوتوماتيكياً (كم)", value=round(raw_dist, 2))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📦 معطيات الشحنة")
        c_type = st.selectbox("🍎 نوع البضاعة", ["مواد غذائية", "أدوية", "إلكترونيات", "مواد بناء"])
        truck = st.selectbox("🚛 نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=1000.0)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 توليد التقرير النهائي"):
        with st.spinner('جاري التحليل...'):
            time.sleep(1)
            cargo_m = {"أدوية": 1.3, "مواد غذائية": 1.1, "إلكترونيات": 1.2, "مواد بناء": 1.0}
            truck_m = {"صغيرة": 1.0, "متوسطة": 1.4, "تبريد": 2.2, "مقطورة دولية": 2.8}
            
            base = ((dist * 0.9) + ((wght/1000) * 450)) * truck_m[truck] * cargo_m[c_type]
            total = base * 1.35
            travel_time = round(dist / 70, 1)

            st.markdown(f"""
                <div class="result-card">
                    <h3>التكلفة التقديرية للرحلة</h3>
                    <h1 style="font-size:55px;">{total:,.2f} د.ج</h1>
                    <p>نوع الشحنة: {c_type} | وقت الوصول المقدر: {travel_time} ساعة</p>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("### 📋 أولاً: تفاصيل الرحلة والتكلفة")
            st.table(pd.DataFrame({
                "العنصر": ["المسافة", "الوزن", "نوع الشاحنة", "نوع البضاعة", "وقت الوصول"],
                "القيمة": [f"{dist} كم", f"{wght} كغ", truck, c_type, f"{travel_time} ساعة"]
            }))

            st.markdown("### 🔄 ثانياً: جدول مقارنة البدائل")
            comp = []
            costs = {}
            for name, factor in truck_m.items():
                c = (((dist * 0.9) + ((wght/1000) * 450)) * factor * cargo_m[c_type]) * 1.35
                comp.append({"نوع الشاحنة": name, "التكلفة (د.ج)": f"{c:,.2f}"})
                costs[name] = c
            st.table(pd.DataFrame(comp))

            best_truck = min(costs, key=costs.get)
            st.info(f"💡 **توصية النظام:** الوسيلة الأنسب اقتصادياً هي **'{best_truck}'**.")

            st.write("---")
            col_a, col_b = st.columns(2)
            with col_a:
                st.subheader("⭐ تقييم النظام")
                st.feedback("stars")
            with col_b:
                st.subheader("📄 تحميل التقرير")
                report_text = f"تقرير التنبؤ\nالمسافة: {dist} كم\nالتكلفة: {total:,.2f} دج"
                st.download_button("تحميل التقرير كملف نصي", report_text, file_name="Report.txt")

    # التذييل الأصفر الكبير
    st.markdown(f"""
        <div class="footer-style">
            إعداد طلبة تخصص: لوجستيك ونقل دولي <br>
            سهيل عطالي | محمد الحسين موسي | عبد الله سايب <br>
            جامعة محمد خيضر بسكرة - 2026
        </div>
    """, unsafe_allow_html=True)
