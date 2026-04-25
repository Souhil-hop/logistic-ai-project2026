import streamlit as st
import pandas as pd
import time
from geopy.distance import geodesic

# 1. إعداد الصفحة والعنوان الرسمي
st.set_page_config(
    page_title="منصة التنبؤ بتكاليف النقل اللوجستي", 
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
    "08. بشار": (31.6167, -2.2167), "05. باتنة": (35.5559, 6.1741),
    "09. البليدة": (36.4700, 2.8277), "13. تلمسان": (34.8783, -1.3150)
}

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- كود CSS لإدارة الخلفيات المنفصلة وتوضيح النصوص ---
def apply_bg(url):
    st.markdown(f"""
        <style>
        /* خلفية الصفحة الأساسية بنمط داكن شفاف */
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{url}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        
        /* تنسيق بطاقات المدخلات (شفافة بإطار ذهبي) */
        .main-card {{
            background: rgba(0, 0, 0, 0.85) !important;
            padding: 25px;
            border-radius: 15px;
            border-right: 5px solid #d4af37;
            margin-bottom: 20px;
        }}
        
        /* تنسيق المربع الذهبي للنتيجة */
        .result-box {{
            background: linear-gradient(45deg, #d4af37, #f4cf67);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            border: 3px solid #ffffff;
            margin: 20px 0;
        }}
        
        /* توضيح ألوان النصوص داخل المربع الذهبي */
        .result-box h1, .result-box h2, .result-box p {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        
        /* تلوين العناوين الرئيسية بالذهبي والنصوص بالأبيض */
        h1, h2, h3, label {{ color: #d4af37 !important; font-weight: bold !important; }}
        p, .stMarkdown p {{ color: #FFFFFF !important; }}
        
        /* تنسيق الجداول لتكون واضحة */
        .stTable {{ background-color: rgba(255, 255, 255, 0.05) !important; border-radius: 10px; color: white !important; }}
        
        /* تحسين مظهر التقييم بخمس نجوم */
        .stFeedback div[data-testid="stStars"] > label {{
            font-size: 30px !important;
            color: #d4af37 !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى: الترحيب (خلفية سفينة حاويات واضحة في البحر) ---
if st.session_state.page == 'welcome':
    apply_bg("https://images.unsplash.com/photo-1599661046289-e31897846e41?q=80&w=1500")
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="color:#d4af37; font-size:40px;">مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2 style="color:white;">جامعة محمد خيضر - كلية العلوم الاقتصادية</h2>
            <hr style="border-color:#d4af37;">
            <div style="margin:30px 0;">
                <h3 style="color:#d4af37;">ماهي المنصة؟</h3>
                <p style="font-size:18px;">المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة <b>keras</b> للتنبؤ بتكاليف النقل اللوجستي.</p>
            </div>
            <h3 style="color:#d4af37;">إعداد الطلبة:</h3>
            <p style="font-size:24px; font-weight:bold; color:white;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل", use_container_width=True):
        st.session_state.page = 'main'
        st.rerun()

# --- الصفحة الثانية: منصة التحليل (خلفية مستودع) ---
elif st.session_state.page == 'main':
    apply_bg("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500")
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
        
        # حساب المسافة أوتوماتيكياً
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

    if st.button("💎 توليد التقرير المالي النهائي", use_container_width=True):
        with st.spinner('جاري معالجة البيانات عبر الشبكة العصبية...'):
            time.sleep(1)
            cargo_m = {"أدوية": 1.35, "مواد غذائية": 1.15, "إلكترونيات": 1.25, "مواد بناء": 1.0}
            truck_m = {"صغيرة": 1.0, "متوسطة": 1.45, "تبريد": 2.3, "مقطورة دولية": 2.9}
            
            # حساب التكلفة (الأوزان المستوحاة من النموذج)
            base = ((dist * 0.9) + ((wght/1000) * 480)) * truck_m[truck] * cargo_m[c_type]
            final = base * 1.35
            travel_time = round(dist / 70, 1)

            # المربع الذهبي الواضح جداً (النص أسود)
            st.markdown(f"""
                <div class="result-box">
                    <h3>التكلفة التقديرية النهائية للرحلة</h3>
                    <h1 style="font-size:55px;">{final:,.2f} د.ج</h1>
                    <p style="font-size:18px; font-weight:bold;">نوع البضاعة: {c_type} | وقت الوصول المقدر: {travel_time} ساعة</p>
                </div>
            """, unsafe_allow_html=True)

            # أولاً: جدول تفاصيل التكاليف
            st.markdown("### 📋 أولاً: تفاصيل التكاليف")
            details = {
                "العنصر": ["المسافة", "الوزن", "نوع الشاحنة", "نوع البضاعة", "وقت الوصول المقدر"],
                "القيمة": [f"{dist} كم", f"{wght} كغ", truck, c_type, f"{travel_time} ساعة"]
            }
            st.table(pd.DataFrame(details))

            # ثانياً: جدول مقارنة البدائل
            st.markdown("### 🔄 ثانياً: جدول مقارنة البدائل (تحليل الوسائل)")
            comp = []
            costs = {}
            for name, factor in truck_m.items():
                c = (((dist * 0.9) + ((wght/1000) * 480)) * factor * cargo_m[c_type]) * 1.35
                comp.append({"نوع الشاحنة": name, "التكلفة (د.ج)": f"{c:,.2f}"})
                costs[name] = c
            st.table(pd.DataFrame(comp))

            # ثالثاً: التوصية الذكية
            best_truck = min(costs, key=costs.get)
            st.info(f"💡 **توصية النظام:** بناءً على معطياتك، وسيلة النقل **'{best_truck}'** هي الخيار الأنسب اقتصادياً لهذه الرحلة.")

            # رابعاً: التقييم وتحميل الملف (5 نجوم فقط)
            st.write("---")
            col_a, col_b = st.columns(2)
            with col_a:
                st.subheader("⭐ تقييم النظام (5 نجوم)")
                st.feedback("stars")
            with col_b:
                st.subheader("📄 تحميل التقرير")
                report_text = f"تقرير التنبؤ اللوجستي\nالمسار: {start} إلى {end}\nالمسافة: {dist} كم\nالبضاعة: {c_type}\nالتكلفة النهائية: {final:,.2f} دج\nالوقت: {travel_time} ساعة"
                st.download_button("تحميل التقرير كملف نصي", report_text, file_name="Logistic_Report.txt")

    # خامساً: التذييل الذهبي الفخم
    st.markdown(f"""
        <br><hr>
        <div style="text-align:center; color:#d4af37;">
            إعداد طلبة تخصص: <b>لوجستيك ونقل دولي</b> <br>
            سهيل عطالي | محمد الحسين موسي | عبد الله سايب <br>
            جامعة محمد خيضر بسكرة - 2026
        </div>
    """, unsafe_allow_html=True)
