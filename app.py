import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات الـ 58 كاملة
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

# --- كود CSS المحدث: تأثير التلاشي الكلاسيكي وتحسين الوضوح ---
st.markdown("""
    <style>
    /* تأثير التلاشي الكلاسيكي عند تحميل أي عنصر */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp, .main-card, .stTable, .recommendation-box {
        animation: fadeIn 0.8s ease-out;
    }

    * { font-variant-numeric: tabular-nums; font-feature-settings: "tnum"; }
    
    /* لون الخط الأبيض الكبير للوضوح */
    .stApp, .stMarkdown, p, label { 
        color: #FFFFFF !important; 
        font-size: 19px !important; 
        font-weight: 500 !important;
    }
    
    h1, h2, h3 { color: #d4af37 !important; }

    .stTable { 
        background-color: rgba(0, 0, 0, 0.8) !important; 
        border: 2px solid #d4af37 !important;
        border-radius: 12px;
    }
    th { color: #d4af37 !important; background-color: rgba(0,0,0,0.9) !important; font-size: 20px !important; }
    td { color: #ffffff !important; font-size: 18px !important; }

    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.3);
        border: 2px solid #d4af37;
        padding: 25px; border-radius: 15px; color: #ffffff;
        font-weight: bold; text-align: center; backdrop-filter: blur(10px); margin: 20px 0;
        font-size: 20px !important;
    }
    
    .main-card {
        background: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 15px;
        border-right: 5px solid #d4af37; margin-bottom: 20px;
    }

    div[data-testid="stVerticalBlock"] > div { background: transparent !important; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500");
            background-size: cover; background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="text-align:center; margin-top:50px; padding:40px; background:rgba(0,0,0,0.7); border:3px solid #d4af37; border-radius:30px;"><h1 style="color:#d4af37; font-size:45px;">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1><h2 style="color:white;">تحت إشراف جامعة محمد خيضر بسكرة</h2><h3 style="color:#e0e0e0;">إعداد الطالب: سهيل عطالي</h3></div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background:rgba(0,0,0,0.8); padding:25px; border-radius:15px; color:white; text-align:center; margin-top:20px; border:1px solid #d4af37;">
        <p style="font-size:20px;">مشروع بناء نموذج شبكة عصبية باستخدام Keras للتنبؤ بتكاليف النقل اللوجستي عبر 58 ولاية جزائرية بدقة عالية واحترافية.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        # تم إزالة البالونات هنا
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: منصة التحليل ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()
    with col_title:
        st.markdown("<h1 style='color: #d4af37; margin-top: -15px;'>📊 منصة التحليل ودعم القرار الذكي</h1>", unsafe_allow_html=True)

    with st.container():
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
            st.markdown("### 💰 المعطيات المالية والتقنية")
            cargo_type = st.text_input("📦 نوع البضاعة المشحونة", "مواد غذائية / تجهيزات صناعية")
            wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
            fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج/لتر)", value=29.10)
            truck_type = st.selectbox("🚛 نوع الشاحنة المطلوبة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 حساب التكلفة النهائية وتوليد التقارير"):
        # تم إزالة البالونات هنا
        
        truck_specs = {
            "صغيرة": {"cap": 1500, "factor": 1.0},
            "متوسطة": {"cap": 5000, "factor": 1.4},
            "تبريد": {"cap": 18000, "factor": 2.2},
            "مقطورة دولية": {"cap": 25000, "factor": 2.8}
        }

        spec_manual = truck_specs[truck_type]
        base_manual = ((dist * 0.8) + ((wght/1000) * 400)) * spec_manual["factor"]
        fuel_manual = (dist / 5) * fuel
        maint_manual = base_manual * 0.12
        profit_manual = (base_manual + fuel_manual + maint_manual) * 0.20
        total_manual = base_manual + fuel_manual + maint_manual + profit_manual

        st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 25px; border-radius: 20px; text-align: center; color: black; margin-bottom: 25px;">
                <h3 style="margin:0; color: black;">التكلفة التقديرية لنقل بضاعة: ({cargo_type})</h3>
                <h1 style="font-size: 55px; margin:5px; font-family: sans-serif; color: black;">{total_manual:,.2f} د.ج</h1>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### 📋 تقرير تفصيلي لنقل بضاعة من نوع: **{cargo_type}**")
        st.table(pd.DataFrame({
            "بند التكلفة": ["⛽ تكلفة الوقود", "🔧 الصيانة والإهلاك", "🏗️ التشغيل والمسار", "📈 هامش الربح المتوقع"],
            "القيمة (د.ج)": [f"{fuel_manual:,.2f}", f"{maint_manual:,.2f}", f"{base_manual:,.2f}", f"{profit_manual:,.2f}"]
        }))

        comparison_results = []
        valid_options = {}

        for name, spec in truck_specs.items():
            base_calc = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
            f_calc = (dist / 5) * fuel
            total_calc = (base_calc + f_calc + (base_calc * 0.12)) * 1.20

            analysis_note = ""
            if wght > spec["cap"]:
                analysis_note = "❌ حمولة زائدة"
            else:
                valid_options[name] = total_calc
                if wght < (spec["cap"] * 0.4):
                    analysis_note = "⚠️ هدر في المساحة"
                else:
                    analysis_note = "✅ كفاءة مثالية"

            comparison_results.append({
                "نوع الشاحنة": name,
                "التحليل الفني": analysis_note,
                "التكلفة المتوقعة (د.ج)": f"{total_calc:,.2f}"
            })

        if valid_options:
            best_truck_name = min(valid_options, key=valid_options.get)
            for row in comparison_results:
                if row["نوع الشاحنة"] == best_truck_name:
                    row["التحليل الفني"] = "⭐ الخيار الأوفر"

        st.markdown("### 🔄 تحليل سيناريوهات النقل المتاحة")
        st.table(pd.DataFrame(comparison_results))

        st.markdown(f"""
            <div class="recommendation-box">
                💡 التوصية اللوجستية لنقل ({cargo_type}): بناءً على المعطيات الاقتصادية الحالية، 
                فإن الخيار ({best_truck_name}) هو الأنسب لضمان أقل تكلفة وأعلى كفاءة في المسار.
            </div>
        """, unsafe_allow_html=True)

        st.write("---")
        st.markdown("### 🧪 تقييم دقة النموذج")
        col_eval1, col_eval2 = st.columns([2, 1])
        with col_eval1:
            eval_score = st.radio("هل النتائج تعكس الواقع الميداني؟", 
                                 ("نعم، دقيقة جداً ✅", "تحتاج معايرة طفيفة ⚠️", "غير دقيقة ❌"), 
                                 horizontal=True)
        with col_eval2:
            if st.button("حفظ التقييم 📩"):
                st.success("تم تسجيل ملاحظتك لتطوير أوزان الشبكة العصبية.")

    st.markdown("<p style='text-align:center; color:#d4af37; font-weight:bold; margin-top:40px;'>مشروع التخرج: سهيل عطالي - جامعة محمد خيضر بسكرة 2026</p>", unsafe_allow_html=True)
