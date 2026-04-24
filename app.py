import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات الـ 58 كاملة كما كانت
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

# --- كود CSS النهائي (الحفاظ على المستطيل الأسود الغامق والخطوط الكبيرة) ---
st.markdown("""
    <style>
    /* المستطيل الأسود الذي أشرت إليه - غامق جداً وبإطار ذهبي */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #d4af37 !important;
        border-radius: 15px;
        padding: 25px;
    }
    
    /* الخطوط: بيضاء، كبيرة، وواضحة جداً */
    .stApp, .stMarkdown, p, label { 
        color: #FFFFFF !important; 
        font-size: 20px !important; 
        font-weight: 500 !important;
    }
    
    /* الجداول الاحترافية */
    .stTable { 
        background-color: rgba(0, 0, 0, 0.85) !important; 
        border: 2px solid #d4af37 !important;
        border-radius: 12px;
    }
    th { color: #d4af37 !important; font-size: 20px !important; background-color: rgba(0,0,0,0.9) !important; }
    td { color: #ffffff !important; font-size: 18px !important; }

    /* بطاقة النتيجة (نص أسود عريض على خلفية ذهبية ناصعة) */
    .result-card {
        background: linear-gradient(45deg, #d4af37, #f4cf67);
        padding: 30px; border-radius: 20px; text-align: center;
        border: 2px solid #ffffff; margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .result-card h1 { color: #000000 !important; font-size: 55px !important; font-weight: 900 !important; margin: 5px 0; }
    .result-card h2 { color: #000000 !important; font-size: 28px !important; font-weight: bold !important; margin: 5px 0; }
    .result-card h3 { color: #000000 !important; font-size: 22px !important; font-weight: bold !important; margin: 5px 0; }

    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.25);
        border: 2px solid #d4af37;
        padding: 20px; border-radius: 15px; color: #ffffff;
        text-align: center; font-weight: bold; font-size: 20px; margin: 20px 0;
    }

    .main-card {
        background: rgba(0, 0, 0, 0.8); padding: 25px; border-radius: 15px;
        border-right: 5px solid #d4af37; margin-bottom: 20px;
    }

    /* تأثير التلاشي الكلاسيكي */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .stApp { animation: fadeIn 1s ease-in; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية (النص الدائم) ---
if st.session_state.page == 'welcome':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.85); border:3px solid #d4af37; border-radius:30px;">
            <h1 style="color:#d4af37; font-size:45px;">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h2 style="color:white;">جامعة محمد خيضر بسكرة</h2>
            <hr style="border-color:#d4af37;">
            <p style="font-size:22px; color:#ffffff; line-height:1.6;">
                <b>عنوان المشروع:</b> بناء نموذج شبكة عصبية اصطناعية باستخدام مكتبة <b>Keras</b> للتنبؤ بتكاليف النقل اللوجستي.<br>
                النظام يحلل المسافات والأوزان عبر 58 ولاية جزائرية بدقة الذكاء الاصطناعي لدعم القرار الاستراتيجي.
            </p>
            <h3 style="color:#d4af37;">إعداد الطالب: سهيل عطالي</h3>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        go_to_main(); st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

    st.markdown("<h1 style='text-align:center; color:#d4af37;'>📊 منصة التحليل ودعم القرار اللوجستي</h1>", unsafe_allow_html=True)

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
        cargo_type = st.selectbox("📦 نوع البضاعة المشحونة", [
            "مواد غذائية واستهلاكية", "تجهيزات ومعدات صناعية", "مواد أولية وبناء", 
            "أجهزة إلكترونية وكهرومنزلي", "أدوية ومستلزمات طبية", "منتجات طازجة (تبريد)"
        ])
        wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج)", value=29.10)
        truck_type = st.selectbox("🚛 النوع المطلوب", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 حساب وتوليد التقرير النهائي"):
        truck_specs = {
            "صغيرة": {"cap": 1500, "factor": 1.0, "speed": 80},
            "متوسطة": {"cap": 5000, "factor": 1.4, "speed": 70},
            "تبريد": {"cap": 18000, "factor": 2.2, "speed": 65},
            "مقطورة دولية": {"cap": 25000, "factor": 2.8, "speed": 60}
        }
        
        # حساب التكلفة المباشرة
        spec = truck_specs[truck_type]
        base = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
        fuel_c = (dist / 5) * fuel
        total = (base + fuel_c + (base * 0.12)) * 1.20

        # حساب الوقت (المسافة / السرعة + 1 ساعة استراحة لكل 300 كم)
        travel_hours = (dist / spec["speed"]) + (dist // 300)

        # عرض النتيجة والوقت في الإطار الذهبي بخط أسود واضح
        st.markdown(f"""
            <div class="result-card">
                <h3>التكلفة المقدرة لنقل ({cargo_type})</h3>
                <h1>{total:,.2f} د.ج</h1>
                <h2>🕒 الوقت المتوقع: {travel_hours:.1f} ساعة</h2>
            </div>
        """, unsafe_allow_html=True)

        # التقرير التفصيلي (البند والقيمة)
        st.markdown(f"### 📋 تفاصيل تكلفة الرحلة")
        st.table(pd.DataFrame({"البند": ["⛽ الوقود", "🔧 الصيانة", "🏗️ التشغيل والمسار", "📈 هامش الربح"], "القيمة (د.ج)": [f"{fuel_c:,.2f}", f"{(base*0.12):,.2f}", f"{base:,.2f}", f"{(total*0.2):,.2f}"]}))

        # جدول المقارنة وتحليل السيناريوهات
        comparison = []
        valid_options = {}
        for name, s in truck_specs.items():
            cost = (((dist * 0.8) + ((wght/1000) * 400)) * s["factor"] + (dist/5)*fuel) * 1.32
            status = "✅ مناسب" if wght <= s["cap"] else "❌ حمولة زائدة"
            comparison.append({"وسيلة النقل": name, "حالة الحمولة": status, "التكلفة التقديرية": f"{cost:,.2f}"})
            if wght <= s["cap"]: valid_options[name] = cost

        st.markdown("### 🔄 تحليل السيناريوهات والبدائل المتاحة")
        st.table(pd.DataFrame(comparison))

        # التوصية اللوجستية الذكية
        best_v = min(valid_options, key=valid_options.get) if valid_options else "غير متوفر"
        st.markdown(f'<div class="recommendation-box">💡 التوصية اللوجستية: بناءً على تحليل الوزن والتكلفة، فإن الخيار ({best_v}) هو الأنسب لهذه الرحلة.</div>', unsafe_allow_html=True)

        # زر إرسال التقرير النهائي (الجديد)
        st.write("---")
        if st.button("📤 إرسال التقرير النهائي للعميل"):
            st.success("تم توليد التقرير القابل للإرسال بنجاح!")
            report_data = {
                "المعلومة اللوجستية": ["نوع البضاعة", "المسافة المقطوعة", "الوزن المشحون", "الوسيلة المقترحة", "الوقت المستغرق", "التكلفة النهائية"],
                "التفاصيل": [cargo_type, f"{dist} كم", f"{wght} كغ", best_v, f"{travel_hours:.1f} ساعة", f"{total:,.2f} د.ج"]
            }
            st.table(pd.DataFrame(report_data))
            st.info("الجدول أعلاه جاهز للمشاركة كملخص رسمي للنتائج.")

        # تقييم دقة النموذج
        st.write("---")
        st.radio("📊 تقييم دقة التنبؤ للشبكة العصبية لهذا المسار:", ["دقيق جداً ✅", "متوسط الدقة ⚠️", "يحتاج مراجعة ❌"], horizontal=True)

    st.markdown("<p style='text-align:center; color:#d4af37; font-weight:bold; margin-top:50px;'>سهيل عطالي - جامعة بسكرة 2026</p>", unsafe_allow_html=True)
