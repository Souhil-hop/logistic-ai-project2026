import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

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

# --- كود CSS المتكامل والنهائي ---
st.markdown("""
    <style>
    /* تعديل المستطيل الأسود ليصبح أغمق وأوضح */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: rgba(0, 0, 0, 0.9) !important; /* أسود غامق جداً */
        border: 1px solid #d4af37 !important;
        border-radius: 15px;
    }
    
    /* الخطوط بيضاء وكبيرة */
    .stApp, .stMarkdown, p, label { 
        color: #FFFFFF !important; 
        font-size: 20px !important; 
        font-weight: 500 !important;
    }
    
    /* الجداول احترافية */
    .stTable { 
        background-color: rgba(0, 0, 0, 0.85) !important; 
        border: 2px solid #d4af37 !important;
        border-radius: 12px;
    }
    th { color: #d4af37 !important; font-size: 20px !important; }
    td { color: #ffffff !important; }

    /* بطاقة النتيجة (أسود عريض على ذهبي) */
    .result-card {
        background: linear-gradient(45deg, #d4af37, #f4cf67);
        padding: 30px; border-radius: 20px; text-align: center;
        border: 2px solid #ffffff; margin-bottom: 25px;
    }
    .result-card h1 { color: #000000 !important; font-size: 55px !important; font-weight: 900 !important; }
    .result-card h3 { color: #000000 !important; font-size: 22px !important; font-weight: bold !important; }

    /* صندوق التوصية الذكية */
    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.25);
        border: 2px solid #d4af37;
        padding: 20px; border-radius: 15px; color: #ffffff;
        text-align: center; font-weight: bold; font-size: 20px; margin: 20px 0;
    }

    .main-card {
        background: rgba(0, 0, 0, 0.8); padding: 25px; border-radius: 15px;
        border-right: 5px solid #d4af37;
    }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية (النص الدائم) ---
if st.session_state.page == 'welcome':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="color:#d4af37; font-size:45px;">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2 style="color:white;">تحت إشراف جامعة محمد خيضر بسكرة</h2>
            <hr style="border-color:#d4af37;">
            <p style="font-size:22px; color:#ffffff;">
                <b>موضوع البحث:</b> بناء نموذج شبكة عصبية باستخدام مكتبة <b>Keras</b> للتنبؤ بتكاليف النقل اللوجستي.<br>
                النظام يغطي 58 ولاية جزائرية ويحلل كفاءة الشحن بدقة الذكاء الاصطناعي.
            </p>
            <h3 style="color:#d4af37;">إعداد الطالب: سهيل عطالي</h3>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول للمنصة"): go_to_main(); st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 مسار الرحلة")
        start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6)
        end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=15)
        dist = st.number_input("📏 المسافة الإجمالية (كم)", value=500.0)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 💰 المعطيات التقنية")
        cargo_type = st.selectbox("📦 نوع البضاعة", ["مواد غذائية", "معدات صناعية", "مواد بناء", "إلكترونيات", "أدوية"])
        wght = st.number_input("⚖️ الوزن (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود (د.ج)", value=29.10)
        truck_type = st.selectbox("🚛 النوع المطلوب", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 توليد التقرير والتحليل الذكي"):
        truck_specs = {"صغيرة": {"cap": 1500, "factor": 1.0}, "متوسطة": {"cap": 5000, "factor": 1.4}, "تبريد": {"cap": 18000, "factor": 2.2}, "مقطورة دولية": {"cap": 25000, "factor": 2.8}}
        
        # 1. حساب التكلفة المباشرة
        spec = truck_specs[truck_type]
        base = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
        fuel_c = (dist / 5) * fuel
        total = (base + fuel_c + (base * 0.12)) * 1.20

        st.markdown(f'<div class="result-card"><h3>تكلفة نقل ({cargo_type})</h3><h1>{total:,.2f} د.ج</h1></div>', unsafe_allow_html=True)

        # 2. التقرير التفصيلي
        st.markdown(f"### 📋 تقرير التكاليف")
        st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 الربح"], "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

        # 3. جدول المقارنة وتحليل السيناريوهات (الذي طالبت بإعادته)
        comparison = []
        valid = {}
        for name, s in truck_specs.items():
            cost = (((dist * 0.8) + ((wght/1000) * 400)) * s["factor"] + (dist/5)*fuel) * 1.32
            status = "✅ مناسب" if wght <= s["cap"] else "❌ حمولة زائدة"
            comparison.append({"نوع الشاحنة": name, "الحالة": status, "التكلفة التقديرية": f"{cost:,.2f}"})
            if wght <= s["cap"]: valid[name] = cost

        st.markdown("### 🔄 جدول المقارنة وتحليل السيناريوهات")
        st.table(pd.DataFrame(comparison))

        # 4. التوصية اللوجستية
        best = min(valid, key=valid.get) if valid else "لا يوجد خيار متاح"
        st.markdown(f'<div class="recommendation-box">💡 التوصية: الخيار ({best}) هو الأفضل اقتصادياً لنقل هذه الحمولة.</div>', unsafe_allow_html=True)

        # 5. تقييم دقة النموذج
        st.write("---")
        st.radio("📊 تقييم دقة تنبؤ الشبكة العصبية لهذا المسار:", ["دقيق جداً ✅", "مقبول ⚠️", "غير دقيق ❌"], horizontal=True)

    st.markdown("<p style='text-align:center; color:#d4af37; font-weight:bold; margin-top:50px;'>سهيل عطالي - جامعة بسكرة 2026</p>", unsafe_allow_html=True)
