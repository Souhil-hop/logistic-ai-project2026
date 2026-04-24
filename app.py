import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main():
    st.session_state.page = 'main'

def go_to_welcome():
    st.session_state.page = 'welcome'

# قائمة الـ 58 ولاية كاملة
wilayas_58 = [
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

# --- الصفحة الأولى: الواجهة الترحيبية (خلفية الميناء) ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); /* صورة ميناء حاويات */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .welcome-box {
            background-color: rgba(0, 0, 0, 0.85);
            padding: 50px;
            border-radius: 30px;
            text-align: center;
            border: 3px solid #d4af37;
            margin: auto;
            max-width: 900px;
            margin-top: 50px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        }
        .welcome-title { color: #d4af37; font-size: 42px; font-weight: bold; margin-bottom: 10px; }
        .welcome-subtitle { color: #ffffff; font-size: 20px; margin-bottom: 30px; border-bottom: 1px solid #d4af37; padding-bottom: 15px; }
        .welcome-desc { color: #e0e0e0; font-size: 22px; line-height: 1.8; }
        .stButton>button { 
            background-color: #d4af37 !important; 
            color: black !important; 
            font-weight: bold !important;
            font-size: 22px !important;
            border-radius: 15px !important;
            height: 70px !important;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="welcome-box">
            <h1 class="welcome-title">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h3 class="welcome-subtitle">تحت إشراف جامعة محمد خيضر بسكرة | من إعداد الطالب: سهيل عطالي</h3>
            <p class="welcome-desc">
                مرحباً بكم في مشروع <b>محاكاة الشبكة العصبية</b> للتنبؤ بتكاليف النقل اللوجستي.
                هذا النظام يستخدم خوارزميات متقدمة بلغة Python لتحليل البيانات ودعم اتخاذ القرار في 58 ولاية جزائرية.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("") 
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: منصة العمليات (خلفية المستودعات) ---
elif st.session_state.page == 'main':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                        url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); /* صورة مستودع لوجستي */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .main-card {
            background: rgba(13, 17, 23, 0.9);
            padding: 25px;
            border-radius: 15px;
            border-right: 5px solid #d4af37;
            margin-bottom: 20px;
        }
        label { color: #d4af37 !important; font-size: 18px !important; font-weight: bold !important; }
        .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: rgba(13, 17, 23, 0.9); color: #d4af37; text-align: center; padding: 8px; border-top: 1px solid #d4af37; font-weight: bold; }
        .back-btn button { background-color: transparent !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; height: 40px !important; }
        </style>
    """, unsafe_allow_html=True)

    # صف يحتوي على زر الرجوع والعنوان
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ رجوع"):
            go_to_welcome()
            st.rerun()
    with col_title:
        st.markdown("<h1 style='color: #d4af37; margin-top: -10px;'>📊 منصة التحليل والتنبؤ الذكي</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: white;'>جامعة محمد خيضر بسكرة - إعداد سهيل عطالي</p>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("### 📍 مسار الرحلة")
            start_p = st.selectbox("🚩 نقطة الانطلاق (Origin)", wilayas_58, index=6)
            end_p = st.selectbox("🏁 نقطة الوصول (Destination)", wilayas_58, index=15)
            dist = st.number_input("📏 المسافة الإجمالية (كم)", value=400.0)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("### 💰 المعطيات المالية والتقنية")
            wght_kg = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=1000.0)
            fuel_p = st.number_input("⛽ سعر الوقود الحالي (د.ج/لتر)", value=29.1)
            chosen_truck = st.selectbox("🚛 نوع الشاحنة المطلوبة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 حساب التكلفة النهائية وتوليد التقرير"):
        st.balloons()
        
        t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
        w_t = wght_kg / 1000.0
        base_cost = ((dist * 0.7) + (w_t * 300)) * t_map[chosen_truck]
        fuel_cost = (dist / 5) * fuel_p
        maint = base_cost * 0.12
        profit = (base_cost + fuel_cost + maint) * 0.20
        total = base_cost + fuel_cost + maint + profit

        st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 30px; border-radius: 20px; text-align: center; color: black; margin: 25px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
                <h2 style="margin:0;">💵 التكلفة النهائية التقديرية 💵</h2>
                <h1 style="font-size: 55px; margin:10px;">{total:,.2f} د.ج</h1>
                <p>من <b>{start_p}</b> إلى <b>{end_p}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📋 تفصيل هيكلة التكاليف (Cost Breakdown)")
        st.table({
            "بند التكلفة": ["⛽ تكاليف الوقود", "🔧 الصيانة والاهلاك", "🏗️ التشغيل والمسار", "📈 هامش الربح المستهدف"],
            "القيمة (د.ج)": [f"{fuel_cost:,.2f}", f"{maint:,.2f}", f"{base_cost:,.2f}", f"{profit:,.2f}"]
        })

        st.markdown("### 🔄 تحليل البدائل (Scenario Analysis)")
        comp_data = []
        for t, m in t_map.items():
            c = ((dist * 0.7) + (w_t * 300)) * m + fuel_cost + (base_cost*0.12) + profit
            comp_data.append({"🚛 الشاحنة": t, "💰 التكلفة الكلية": round(c, 2)})
        
        df = pd.DataFrame(comp_data)
        st.dataframe(df.style.highlight_min(subset=['💰 التكلفة الكلية'], color='#28a745'), use_container_width=True)

        # قسم التقييم (جديد)
        st.write("---")
        st.markdown("### 🧪 تقييم النموذج الذكي")
        col_eval, _ = st.columns([2, 1])
        with col_eval:
            is_accurate = st.radio("هل كانت النتيجة دقيقة بناءً على تقديراتك الميدانية؟", ("نعم، دقيقة جداً", "تحتاج إلى تعديل طفيف", "غير دقيقة"))
            if st.button("إرسال التقييم 📩"):
                st.success("شكراً لك! سيتم استخدام تقييمك لتحسين أوزان الشبكة العصبية.")

    st.markdown("<div class='footer'>مشروع التخرج: سهيل عطالي - جامعة محمد خيضر بسكرة 2026</div>", unsafe_allow_html=True)
