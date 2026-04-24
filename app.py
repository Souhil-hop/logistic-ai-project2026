import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات الكاملة والواضحة (إصلاح مشكلة الأرقام فقط)
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

# --- كود CSS الشامل (للأرقام، الجداول، والوضوح التام) ---
st.markdown("""
    <style>
    /* إجبار الأرقام على التنسيق الدولي */
    * { font-variant-numeric: tabular-nums; font-feature-settings: "tnum"; }
    
    /* تحسين وضوح الجداول مع الحفاظ على الخلفية */
    .stTable { 
        background-color: rgba(0, 0, 0, 0.75) !important; 
        border: 1px solid #d4af37 !important;
        border-radius: 12px;
    }
    th { color: #d4af37 !important; background-color: rgba(0,0,0,0.9) !important; font-size: 18px !important; text-align: center !important; }
    td { color: #ffffff !important; font-size: 16px !important; text-align: center !important; border-bottom: 1px solid rgba(212, 175, 55, 0.2) !important; }

    /* التوصية الذكية (ذهبي واضح غير شفاف) */
    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.25);
        border: 2px solid #d4af37;
        padding: 20px;
        border-radius: 15px;
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        backdrop-filter: blur(8px);
        margin: 20px 0;
    }
    
    /* العناوين والبطاقات */
    .main-card {
        background: rgba(13, 17, 23, 0.75); padding: 25px; border-radius: 15px;
        border-right: 5px solid #d4af37; margin-bottom: 20px;
    }
    label { color: #d4af37 !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500");
            background-size: cover; background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; margin-top:80px; padding:50px; background:rgba(0,0,0,0.6); border:3px solid #d4af37; border-radius:30px;"><h1 style="color:#d4af37; font-size:45px;">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1><h2 style="color:white;">جامعة محمد خيضر بسكرة</h2><h3 style="color:#e0e0e0;">إعداد الطالب: سهيل عطالي</h3></div>', unsafe_allow_html=True)
    st.write("")
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: العمليات والتحليل الخبير ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()
    with col_title:
        st.markdown("<h1 style='color: #d4af37; margin-top: -15px;'>📊 منصة التحليل ودعم القرار</h1>", unsafe_allow_html=True)

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
            st.markdown("### 💰 المعطيات التقنية")
            wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
            fuel = st.number_input("⛽ سعر الوقود الحالي (د.ج)", value=29.1)
            st.markdown("<p style='color: #e0e0e0; font-size: 14px;'>سيقوم النظام آلياً بتحليل كفاءة التحميل لكل نوع</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 حساب التكلفة وتوليد التحليل اللوجستي"):
        # تعريف الشاحنات وقدراتها (لوجستيك حقيقي)
        truck_specs = {
            "صغيرة": {"cap": 1500, "factor": 1.0},
            "متوسطة": {"cap": 5000, "factor": 1.4},
            "تبريد": {"cap": 18000, "factor": 2.2},
            "مقطورة دولية": {"cap": 25000, "factor": 2.8}
        }

        comparison_results = []
        valid_options = {}

        for name, spec in truck_specs.items():
            # الحسابات الاقتصادية
            base = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
            f_cost = (dist / 5) * fuel
            maint = base * 0.12
            profit = (base + f_cost + maint) * 0.20
            total_cost = base + f_cost + maint + profit

            # نظام التحليل الخبير (ملاحظات سهيل)
            analysis_note = ""
            if wght > spec["cap"]:
                analysis_note = "❌ حمولة أكبر من الشاحنة"
            else:
                valid_options[name] = total_cost
                # إذا كانت الحمولة تشغل أقل من 40% من سعة الشاحنة
                if wght < (spec["cap"] * 0.4):
                    analysis_note = "⚠️ مساحة فارغة (تكاليف ضائعة)"
                else:
                    analysis_note = "✅ خيار متاح"

            comparison_results.append({
                "نوع الشاحنة": name,
                "السعة": f"{spec['cap']} كغ",
                "التكلفة الكلية (د.ج)": f"{total_cost:,.2f}",
                "التحليل اللوجستي": analysis_note
            })

        # تحديد "الأفضل" و "البديل" بين الخيارات الآمنة
        if valid_options:
            best_truck_name = min(valid_options, key=valid_options.get)
            min_price = valid_options[best_truck_name]
            
            for row in comparison_results:
                if row["نوع الشاحنة"] == best_truck_name:
                    row["التحليل اللوجستي"] = "⭐ الخيار الأفضل"
                elif row["التحليل اللوجستي"] == "✅ خيار متاح":
                    row["التحليل اللوجستي"] = "🔄 خيار بديل"

            # عرض التكلفة المثالية
            st.markdown(f"""
                <div style="background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 25px; border-radius: 20px; text-align: center; color: black; margin-bottom: 25px;">
                    <h2 style="margin:0;">التكلفة التقديرية (للخيار الأمثل)</h2>
                    <h1 style="font-size: 50px; margin:5px; font-family: sans-serif;">{min_price:,.2f} د.ج</h1>
                </div>
            """, unsafe_allow_html=True)

            # عرض جدول المقارنة المطور
            st.markdown("### 📋 جدول المقارنة وتحليل كفاءة التحميل")
            st.table(pd.DataFrame(comparison_results))

            # التوصية النهائية
            st.markdown(f"""
                <div class="recommendation-box">
                    💡 توصية النظام الخبير: الخيار <b>({best_truck_name})</b> هو الأنسب تقنياً ومالياً لحمولة تزن {wght/1000} طن. 
                    تم استبعاد الخيارات غير الآمنة وتنبيهك من الهدر المالي.
                </div>
            """, unsafe_allow_html=True)

        # نظام التقييم
        st.write("---")
        st.markdown("### 🧪 تقييم دقة النموذج")
        eval_choice = st.radio("هل النتيجة دقيقة ومنطقية؟", ("نعم، دقيقة جداً", "تحتاج تعديل بسيط", "غير منطقية"))
        if st.button("إرسال التقييم 📩"):
            st.success("تم استلام التقييم بنجاح، شكراً يا سهيل!")

    st.markdown("<p style='text-align:center; color:#d4af37; font-weight:bold; margin-top:40px;'>مشروع التخرج: سهيل عطالي - جامعة بسكرة 2026</p>", unsafe_allow_html=True)
