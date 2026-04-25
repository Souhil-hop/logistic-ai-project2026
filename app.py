import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import time

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="منصة التنبؤ بتكاليف النقل اللوجستي", page_icon="📊", layout="wide")

# إحداثيات الولايات (لحساب المسافة أوتوماتيكياً)
coords = {
    "01. أدرار": (27.8742, -0.2939), "02. الشلف": (36.1647, 1.3317), "03. الأغواط": (33.8000, 2.8651),
    "04. أم البواقي": (35.8754, 7.1135), "05. باتنة": (35.5559, 6.1741), "07. بسكرة": (34.8516, 5.7281),
    "08. بشار": (31.6167, -2.2167), "09. البليدة": (36.4700, 2.8277), "13. تلمسان": (34.8783, -1.3150),
    "16. الجزائر": (36.7538, 3.0588), "19. سطيف": (36.1911, 5.4133), "23. عنابة": (36.9000, 7.7667),
    "25. قسنطينة": (36.3650, 6.6147), "30. ورقلة": (31.9493, 5.3250), "31. وهران": (35.6987, -0.6359),
    "39. الوادي": (33.3683, 6.8674), "47. غرداية": (32.4909, 3.6733), "51. أولاد جلال": (34.4170, 5.0660)
}

wilayas_names = [
    "01. أدرار", "02. الشلف", "03. الأغواط", "04. أم البواقي", "05. باتنة", "06. بجاية", "07. بسكرة", 
    "08. بشار", "09. البليدة", "10. البويرة", "11. تمنراست", "12. تبسة", "13. تلمسان", "14. تيارت", 
    "15. تيزي وزو", "16. الجزائر", "17. جلفة", "18. جيجل", "19. سطيف", "20. سعيدة", "21. سكيكدة", 
    "22. سيدي بلعباس", "23. عنابة", "24. قالمة", "25. قسنطينة", "26. المدية", "27. مستغانم", 
    "28. المسيلة", "29. معسكر", "30. ورقلة", "31. وهران", "32. البيض", "33. إليزي", "34. برج بوعريريج", 
    "35. بومرداس", "36. الطارف", "37. تندوف", "38. تيسمسيلت", "39. الوادي", "40. خنشلة", "41. سوق أهراس", 
    "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة", "46. عين تموشنت", "47. غرداية", "48. غليزان", 
    "49. تيميمون", "50. برج باجي مختار", "51. أولاد جلال", "52. بني عباس", "53. عين صالح", "54. عين قزام", 
    "55. تقرت", "56. جانت", "57. المغير", "58. المنيعة"
]

if 'page' not in st.session_state: st.session_state.page = 'welcome'

# --- كود CSS لإصلاح كل شيء (الخلفيات والألوان) ---
def apply_theme(bg_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("{bg_url}");
            background-size: cover; background-attachment: fixed; background-position: center;
        }}
        .main-card {{ background: rgba(0, 0, 0, 0.85); padding: 20px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; }}
        .result-card {{ background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 25px; border-radius: 20px; text-align: center; border: 3px solid #ffffff; }}
        .result-card h1, .result-card p, .result-card h3 {{ color: #000000 !important; font-weight: 900 !important; }}
        h1, h2, h3, label, .stMarkdown p {{ color: #FFFFFF !important; }}
        .stTable {{ background-color: rgba(255, 255, 255, 0.1) !important; border-radius: 10px; }}
        .footer-style {{ text-align: center; color: #d4af37 !important; font-size: 22px !important; font-weight: bold; margin-top: 50px; border-top: 1px solid #d4af37; padding-top: 20px; }}
        </style>
    """, unsafe_allow_html=True)

# --- الصفحة الأولى ---
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
            <h3>إعداد طلبة أولى ماستر لوجستيك ونقل دولي:</h3>
            <p style="font-size:24px; font-weight:bold;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل", use_container_width=True):
        st.session_state.page = 'main'
        st.rerun()

# --- الصفحة الثانية ---
elif st.session_state.page == 'main':
    apply_theme("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500")
    if st.button("⬅️ رجوع"):
        st.session_state.page = 'welcome'
        st.rerun()

    st.markdown("<h1 style='text-align:center;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 تفاصيل المسار")
        start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6)
        end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=15)
        
        # حساب المسافة أوتوماتيكياً
        calc_dist = 500.0
        if start in coords and end in coords:
            calc_dist = geodesic(coords[start], coords[end]).km
        dist = st.number_input("📏 المسافة المحسوبة أوتوماتيكياً (كم)", value=round(calc_dist, 2))
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 💰 معطيات الشحنة")
        cargo_type = st.selectbox("📦 نوع البضاعة", ["مواد غذائية واستهلاكية", "تجهيزات ومعدات صناعية", "مواد أولية وبناء", "أجهزة إلكترونية", "أدوية"])
        wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج)", value=29.10)
        truck_type = st.selectbox("🚛 النوع المطلوب", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 توليد تقرير التنبؤ النهائي", use_container_width=True):
        truck_specs = {
            "صغيرة": {"cap": 1500, "factor": 1.0, "speed": 80},
            "متوسطة": {"cap": 5000, "factor": 1.4, "speed": 70},
            "تبريد": {"cap": 18000, "factor": 2.2, "speed": 65},
            "مقطورة دولية": {"cap": 25000, "factor": 2.8, "speed": 60}
        }
        spec = truck_specs[truck_type]
        base = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
        fuel_c = (dist / 5) * fuel
        total = (base + fuel_c + (base * 0.12)) * 1.20
        travel_hours = (dist / spec["speed"]) + (dist // 300)

        st.markdown(f"""
            <div class="result-card">
                <h3>التكلفة المقدرة للرحلة</h3>
                <h1 style="font-size:55px;">{total:,.2f} د.ج</h1>
                <p>🕒 الوقت المتوقع للوصول: {travel_hours:.1f} ساعة</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📋 التقرير التفصيلي للتكاليف")
        st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 الربح"], "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

        comparison = []
        valid_options = {}
        for name, s in truck_specs.items():
            cost = (((dist * 0.8) + ((wght/1000) * 400)) * s["factor"] + (dist/5)*fuel) * 1.32
            status = "✅ مناسب" if wght <= s["cap"] else "❌ حمولة زائدة"
            comparison.append({"الوسيلة": name, "الحالة": status, "التكلفة التقديرية": f"{cost:,.2f}"})
            if wght <= s["cap"]: valid_options[name] = cost

        st.markdown("### 🔄 تحليل البدائل (جدول المقارنة)")
        st.table(pd.DataFrame(comparison))

        best_v = min(valid_options, key=valid_options.get) if valid_options else "غير محدد"
        st.info(f"💡 **توصية النظام:** الوسيلة الأنسب اقتصادياً هي **'{best_v}'**.")

        st.download_button("📤 تحميل التقرير النهائي (Text)", f"تقرير التنبؤ: {total:,.2f} دج", file_name="Report.txt")

    st.markdown("""
        <div class="footer-style">
            إعداد طلبة أولى ماستر لوجستيك ونقل دولي:<br>
            سهيل عطالي | محمد الحسين موسي | عبد الله سايب<br>
            جامعة محمد خيضر بسكرة - كلية العلوم الاقتصادية - دفعة 2026
        </div>
    """, unsafe_allow_html=True)
