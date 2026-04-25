import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="منصة التنبؤ بتكاليف النقل اللوجستي", layout="wide")

# قاموس الإحداثيات (خطوط الطول والعرض) لأهم الولايات لحساب المسافة أوتوماتيكياً
# ملاحظة: يمكنك إضافة إحداثيات بقية الولايات الـ 58 هنا
coords = {
    "01. أدرار": (27.8742, -0.2939), "02. الشلف": (36.1647, 1.3317), "03. الأغواط": (33.8000, 2.8651),
    "04. أم البواقي": (35.8754, 7.1135), "05. باتنة": (35.5559, 6.1741), "07. بسكرة": (34.8516, 5.7281),
    "08. بشار": (31.6167, -2.2167), "09. البليدة": (36.4700, 2.8277), "13. تلمسان": (34.8783, -1.3150),
    "16. الجزائر": (36.7538, 3.0588), "19. سطيف": (36.1911, 5.4133), "23. عنابة": (36.9000, 7.7667),
    "25. قسنطينة": (36.3650, 6.6147), "30. ورقلة": (31.9493, 5.3250), "31. وهران": (35.6987, -0.6359),
    "39. الوادي": (33.3683, 6.8674), "47. غرداية": (32.4909, 3.6733), "51. أولاد جلال": (34.4170, 5.0660)
}

# قائمة الولايات الـ 58 (كاملة للعرض في القائمة)
wilayas_names = list(coords.keys()) + [
    "06. بجاية", "10. البويرة", "11. تمنراست", "12. تبسة", "14. تيارت", "15. تيزي وزو",
    "17. جلفة", "18. جيجل", "20. سعيدة", "21. سكيكدة", "22. سيدي بلعباس", "24. قالمة",
    "26. المدية", "27. مستغانم", "28. المسيلة", "29. معسكر", "32. البيض", "33. إليزي",
    "34. برج بوعريريج", "35. بومرداس", "36. الطارف", "37. تندوف", "38. تيسمسيلت",
    "40. خنشلة", "41. سوق أهراس", "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة",
    "46. عين تموشنت", "48. غليزان", "49. تيميمون", "50. برج باجي مختار", "52. بني عباس",
    "53. عين صالح", "54. عين قزام", "55. تقرت", "56. جانت", "57. المغير", "58. المنيعة"
]

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# --- كود CSS لتجميل الواجهة ---
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: white; }
    .main-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; border: 1px solid #d4af37; }
    .result-card { background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 20px; border-radius: 15px; color: black; text-align: center; }
    h1, h2, h3 { color: #d4af37 !important; }
</style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""
    <div style="text-align:center; padding:50px; border:2px solid #d4af37; border-radius:20px; background:rgba(0,0,0,0.5);">
        <h1>مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
        <h3>جامعة محمد خيضر - كلية العلوم الاقتصادية</h3>
        <hr style="border-color:#d4af37;">
        <p style="font-size:18px;">المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة <b>keras</b> للتنبؤ بتكاليف النقل اللوجستي.</p>
        <h4>إعداد طلبة أولى ماستر لوجستيك ونقل دولي:</h4>
        <p style="font-size:20px; font-weight:bold;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل", use_container_width=True):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
    if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

    st.markdown("<h1 style='text-align:center;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 تفاصيل المسار")
        start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6) # بسكرة افتراضياً
        end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=9) # الجزائر افتراضياً
        
        # --- منطق حساب المسافة أوتوماتيكياً ---
        calculated_dist = 500.0 # قيمة افتراضية في حال عدم توفر الإحداثيات
        if start in coords and end in coords:
            calculated_dist = geodesic(coords[start], coords[end]).km
        
        dist = st.number_input("📏 المسافة المحسوبة أوتوماتيكياً (كم)", value=round(calculated_dist, 2))
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
            <h1 style="font-size:40px;">{total:,.2f} د.ج</h1>
            <p style="font-size:18px; font-weight:bold;">🕒 الوقت المتوقع: {travel_hours:.1f} ساعة</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📋 التقرير التفصيلي للتكاليف")
        st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 الربح"], 
                               "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

        # جدول المقارنة
        comparison = []
        valid_options = {}
        for name, s in truck_specs.items():
            cost = (((dist * 0.8) + ((wght/1000) * 400)) * s["factor"] + (dist/5)*fuel) * 1.32
            status = "✅ مناسب" if wght <= s["cap"] else "❌ حمولة زائدة"
            comparison.append({"الوسيلة": name, "الحالة": status, "التكلفة التقديرية": f"{cost:,.2f}"})
            if wght <= s["cap"]: valid_options[name] = cost

        st.markdown("### 🔄 تحليل البدائل (جدول المقارنة)")
        st.table(pd.DataFrame(comparison))

        st.write("---")
        best_v = min(valid_options, key=valid_options.get) if valid_options else "غير محدد"
        report_data = {
            "البيان": ["نوع البضاعة", "الوزن", "المسافة", "الوسيلة الأفضل", "الوقت", "التكلفة الكلية"],
            "القيمة": [cargo_type, f"{wght} كغ", f"{dist} كم", best_v, f"{travel_hours:.1f} ساعة", f"{total:,.2f} د.ج"]
        }
        st.table(pd.DataFrame(report_data))

    st.markdown(f"""
    <div style="text-align:center; color:#d4af37; margin-top:50px; border-top:1px solid #d4af37; padding-top:20px;">
        من إعداد طلبة أولى ماستر لوجستيك ونقل دولي: <br>
        سهيل عطالي | محمد الحسين موسي | عبد الله سايب <br>
        جامعة محمد خيضر بسكرة - كلية العلوم الاقتصادية - دفعة 2026
    </div>
    """, unsafe_allow_html=True)
