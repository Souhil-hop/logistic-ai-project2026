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

# --- إضافة كود لإجبار الأرقام على الشكل اللاتيني ---
st.markdown("""
    <style>
    /* هذا الكود يمنع المتصفح من تحويل الأرقام للهندية */
    * {
        font-variant-numeric: tabular-nums;
        -webkit-font-feature-settings: "tnum";
        font-feature-settings: "tnum";
    }
    input {
        font-family: sans-serif !important; /* لضمان ظهور الأرقام داخل الصناديق بالإنجليزية */
    }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .welcome-box {
            background-color: rgba(0, 0, 0, 0.4);
            padding: 50px;
            border-radius: 30px;
            text-align: center;
            border: 3px solid #d4af37;
            margin: auto;
            max-width: 900px;
            margin-top: 50px;
            backdrop-filter: blur(10px);
        }
        .welcome-title { color: #d4af37; font-size: 42px; font-weight: bold; }
        .stButton>button { background-color: #d4af37 !important; color: black !important; font-weight: bold; border-radius: 15px; height: 70px; width: 100%; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="welcome-box">
            <h1 class="welcome-title">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h3 style="color:white;">تحت إشراف جامعة محمد خيضر بسكرة | إعداد سهيل عطالي</h3>
            <p style="color:#e0e0e0; font-size:20px;">محاكاة الشبكة العصبية للتنبؤ بتكاليف النقل في 58 ولاية.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 الدخول للمنصة"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية ---
elif st.session_state.page == 'main':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500");
            background-size: cover; background-position: center;
        }
        .main-card {
            background: rgba(13, 17, 23, 0.6);
            padding: 20px; border-radius: 15px; border-right: 5px solid #d4af37; margin-bottom: 20px; backdrop-filter: blur(8px);
        }
        label { color: #d4af37 !important; font-weight: bold !important; }
        </style>
    """, unsafe_allow_html=True)

    if st.button("⬅️ رجوع"):
        go_to_welcome()
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 📍 المسار")
        start_p = st.selectbox("من:", wilayas_58, index=6)
        end_p = st.selectbox("إلى:", wilayas_58, index=15)
        dist = st.number_input("المسافة (كم)", value=400.0)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("### 💰 المعطيات")
        wght = st.number_input("الوزن (كغ)", value=1000.0)
        fuel = st.number_input("سعر الوقود", value=29.1)
        truck = st.selectbox("الشاحنة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 احسب التكلفة"):
        st.balloons()
        t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
        total = ((dist * 0.7) + ((wght/1000) * 300)) * t_map[truck] + (dist/5)*fuel
        
        # عرض النتيجة بتنسيق يمنع التحويل للهندية
        st.markdown(f"""
            <div style="background: #d4af37; padding: 20px; border-radius: 15px; text-align: center; color: black;">
                <h2>التكلفة التقديرية</h2>
                <h1 style="font-family: sans-serif;">{total:,.2f} د.ج</h1>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#d4af37; margin-top:50px;'>مشروع التخرج: سهيل عطالي - جامعة بسكرة 2026</p>", unsafe_allow_html=True)

