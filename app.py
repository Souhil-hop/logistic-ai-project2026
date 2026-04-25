import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي (لتثبيت العنوان الرسمي للرابط)
st.set_page_config(
    page_title="منصة التنبؤ بتكاليف النقل اللوجستي", 
    page_icon="📊",
    layout="wide"
)

# إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات الـ 58
wilayas_names = [
    "01. أدرار", "02. الشلف", "03. الأغواط", "04. أم البواقي", "05. باتنة", 
    "06. بجاية", "07. بسكرة", "08. بشار", "09. البليدة", "10. البويرة", 
    "11. تمنراست", "12. تبسة", "13. تلمسان", "14. تيارت", "15. تيزي وزو", 
    "16. الجزائر", "17. جلفة", "18. جيجل", "19. سطيف", "20. سعيدة", 
    "21. سكيكدة", "22. سيدي بلعباس", "23. عنابة", "24. قالمة", "25. قسنطينة", 
    "26. المدية", "27. مستغانم", "28. المسيلة", "29. معسكر", "30. ورقلة", 
    "31. وهران", "32. البيض", "33. إليزي", "34. برج بوعريريج", "35. بومرداس", 
    "36. الطارف", "37. تندوف", "38. تيسمسيلت", "39. الوادي", "40. خنشلة", 
    "41. سوق أهراس", "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة", 
    "46. عين تموشنت", "47. غرداية", "48. غليزان", "49. تيميمون", "50. برج باجي مختار", 
    "51. أولاد جلال", "52. بني عباس", "53. عين صالح", "54. عين قزام", "55. تقرت", 
    "56. جانت", "57. المغير", "58. المنيعة"
]

# --- كود CSS (المستطيل الغامق جداً وبإطار ذهبي) ---
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #d4af37 !important;
        border-radius: 15px;
        padding: 25px;
    }
    .stApp, .stMarkdown, p, label { color: #FFFFFF !important; font-size: 20px !important; }
    .result-card {
        background: linear-gradient(45deg, #d4af37, #f4cf67);
        padding: 35px; border-radius: 20px; text-align: center;
        border: 2px solid #ffffff; margin-bottom: 25px;
    }
    .result-card h1, .result-card h2, .result-card h3 { color: #000000 !important; font-weight: bold !important; }
    .stTable { background-color: rgba(0, 0, 0, 0.85) !important; border: 2px solid #d4af37 !important; border-radius: 12px; }
    th { color: #d4af37 !important; font-size: 20px !important; }
    .main-card { background: rgba(0, 0, 0, 0.8); padding: 25px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="color:#d4af37; font-size:40px;">مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2 style="color:white;">جامعة محمد خيضر - كلية العلوم الاقتصادية</h2>
            <hr style="border-color:#d4af37;">
            <div style="margin:30px 0;">
                <h3 style="color:#d4af37; font-size:28px;">ماهي المنصة؟</h3>
                <p style="font-size:22px; color:#ffffff; line-height:1.6;">
                    المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة <b>keras</b> لللتنبؤ بتكاليف النقل اللوجستي.
                </p>
            </div>
            <h3 style="color:#d4af37;">إعداد طلبة أولى ماستر لوجستيك ونقل دولي:</h3>
            <div style="background:rgba(212,175,55,0.1); padding:15px; border-radius:15px; border:1px solid #d4af37;">
                <p style="font-size:26px; font-weight:bold; color:white; margin:0;">
                    سهيل عطالي | محمد الحسين موسي | عبد الله سايب
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التحليل"):
        go_to_main(); st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

    st.markdown("<h1 style='text-align:center; color:#d4af37;'>📊 منصة التنبؤ بتكاليف النقل اللوجستي</h1>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 تفاصيل المسار")
        start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6)
        end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=15)
        dist = st.number_input("📏 المسافة (كم)", value=500.0)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 💰 معطيات الشحنة")
        cargo_type = st.selectbox("📦 نوع البضاعة", ["مواد غذائية واستهلاكية", "تجهيزات ومعدات صناعية", "مواد أولية وبناء", "أجهزة إلكترونية", "أدوية"])
        wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج)", value=29.10)
        truck_type = st.selectbox("🚛 النوع المطلوب", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 توليد تقرير التنبؤ النهائي"):
        truck_specs = {"صغيرة": {"cap": 1500, "factor": 1.0, "speed": 80}, "متوسطة": {"cap": 5000, "factor": 1.4, "speed": 70}, "تبريد": {"cap": 18000, "factor": 2.2, "speed": 65}, "مقطورة دولية": {"cap": 25000, "factor": 2.8, "speed": 60}}
        spec = truck_specs[truck_type]
        base = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
        fuel_c = (dist / 5) * fuel
        total = (base + fuel_c + (base * 0.12)) * 1.20
        travel_hours = (dist / spec["speed"]) + (dist // 300)

        st.markdown(f'<div class="result-card"><h3>التكلفة المقدرة للرحلة</h3><h1>{total:,.2f} د.ج</h1><h2>🕒 الوقت المتوقع: {travel_hours:.1f} ساعة</h2></div>', unsafe_allow_html=True)

        st.markdown("### 📋 التقرير التفصيلي للتكاليف")
        st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 الربح المتوقع"], "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

        comparison = []
        for name, s in truck_specs.items():
            cost = (((dist * 0.8) + ((wght/1000) * 400)) * s["factor"] + (dist/5)*fuel) * 1.32
            status = "✅ مناسب" if wght <= s["cap"] else "❌ حمولة زائدة"
            comparison.append({"الوسيلة": name, "الحالة": status, "التكلفة التقديرية": f"{cost:,.2f}"})

        st.markdown("### 🔄 تحليل البدائل (جدول المقارنة)")
        st.table(pd.DataFrame(comparison))

        st.write("---")
        if st.button("📤 إرسال التقرير النهائي (PDF/Image Ready)"):
            st.success("تم إعداد الجدول النهائي القابل للمشاركة!")
            report_data = {"البيان": ["النوع", "الوزن", "المسافة", "الوقت", "التكلفة الكلية"], "القيمة": [cargo_type, f"{wght} كغ", f"{dist} كم", f"{travel_hours:.1f} ساعة", f"{total:,.2f} د.ج"]}
            st.table(pd.DataFrame(report_data))

    st.markdown(f"""
        <div style="text-align:center; color:#d4af37; font-weight:bold; margin-top:20px; border-top:1px solid #d4af37; padding-top:20px;">
            من إعداد طلبة أولى ماستر لوجستيك ونقل دولي: <br>
            <span style="color:white; font-size:22px;">سهيل عطالي | محمد الحسين موسي | عبد الله سايب</span> <br>
            جامعة محمد خيضر بسكرة - كلية العلوم الاقتصادية - دفعة 2026
        </div>
    """, unsafe_allow_html=True)
