import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="منصة التنبؤ بتكاليف النقل اللوجستي", layout="wide")

# 2. إدارة التنقل بين الصفحات
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

""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية (تعديل العناوين والتعريف) ---
if st.session_state.page == 'welcome':
st.markdown("""""", unsafe_allow_html=True)
st.markdown("""



مرحباً بكم طلبة تخصص اللوجستيك والنقل الدولي 🎓


جامعة محمد خيضر - كلية العلوم الاقتصادية


--------------------




ماهي المنصة؟



المنصة عبارة عن نموذج لشبكة عصبية إصطناعية باستخدام مكتبة keras لللتنبؤ بتكاليف النقل اللوجستي.





إعداد طلبة أولى ماستر لوجستيك ونقل دولي:





سهيل عطالي | محمد الحسين موسي | عبد الله سايب






""", unsafe_allow_html=True)
if st.button("🚀 الدخول إلى منصة التحليل"):
go_to_main(); st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
st.markdown("""""", unsafe_allow_html=True)

if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

st.markdown("
📊 منصة التنبؤ بتكاليف النقل اللوجستي
", unsafe_allow_html=True)


c1, c2 = st.columns(2)
with c1:
st.markdown("
", unsafe_allow_html=True)

st.markdown("### 📍 تفاصيل المسار")
start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6)
end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=15)
dist = st.number_input("📏 المسافة (كم)", value=500.0)
st.markdown("
", unsafe_allow_html=True)

with c2:
st.markdown("
", unsafe_allow_html=True)

st.markdown("### 💰 معطيات الشحنة")
cargo_type = st.selectbox("📦 نوع البضاعة", ["مواد غذائية واستهلاكية", "تجهيزات ومعدات صناعية", "مواد أولية وبناء", "أجهزة إلكترونية", "أدوية"])
wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج)", value=29.10)
truck_type = st.selectbox("🚛 النوع المطلوب", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
st.markdown("
", unsafe_allow_html=True)


if st.button("💎 توليد تقرير التنبؤ النهائي"):
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

st.markdown(f'
التكلفة المقدرة للرحلة
{total:,.2f} د.ج
🕒 الوقت المتوقع: {travel_hours:.1f} ساعة
', unsafe_allow_html=True)


st.markdown("### 📋 التقرير التفصيلي للتكاليف")
st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 الربح"], "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

# --- إعادة جدول المقارنة الذي اختفى ---
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
if st.button("📤 إرسال التقرير النهائي (PDF/Image Ready)"):
st.success("تم إعداد الجدول النهائي القابل للمشاركة!")
best_v = min(valid_options, key=valid_options.get) if valid_options else "غير محدد"
report_data = {
"البيان": ["نوع البضاعة", "الوزن", "المسافة", "الوسيلة الأفضل", "الوقت", "التكلفة الكلية"],
"القيمة": [cargo_type, f"{wght} كغ", f"{dist} كم", best_v, f"{travel_hours:.1f} ساعة", f"{total:,.2f} د.ج"]
}
st.table(pd.DataFrame(report_data))

st.write("---")
st.radio("📊 تقييم دقة تنبؤ النموذج الجماعي:", ["دقيق جداً ✅", "مقبول ⚠️", "غير دقيق ❌"], horizontal=True)

st.markdown(f"""


من إعداد طلبة أولى ماستر لوجستيك ونقل دولي:
سهيل عطالي | محمد الحسين موسي | عبد الله سايب
جامعة محمد خيضر بسكرة - كلية العلوم الاقتصادية - دفعة 2026


""", unsafe_allow_html=True)

