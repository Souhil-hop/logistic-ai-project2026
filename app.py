import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام التنبؤ اللوجستي - سهيل", layout="wide")

# 2. إدارة التنقل بين الصفحات (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main():
    st.session_state.page = 'main'

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    # تصميم الواجهة الترحيبية بخلفية صورة احترافية
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80");
            background-size: cover;
            background-position: center;
        }
        .welcome-container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 50px;
            border-radius: 20px;
            text-align: center;
            border: 2px solid #d4af37;
            margin-top: 50px;
        }
        .welcome-title { color: #d4af37; font-size: 45px; font-weight: bold; margin-bottom: 20px; }
        .welcome-text { color: white; font-size: 24px; line-height: 1.6; }
        .stButton>button { 
            background-color: #d4af37 !important; 
            color: black !important; 
            font-size: 20px !important;
            height: 60px !important;
            border-radius: 10px !important;
            margin-top: 30px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="welcome-container">
            <h1 class="welcome-title">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <p class="welcome-text">
                مرحباً بكم في منصتنا الذكية. هذا النظام عبارة عن <b>مشروع محاكاة لشبكة عصبية</b> 
                باستخدام لغة البايثون (Python) تم تطويره خصيصاً للتنبؤ بتكاليف النقل اللوجستي بدقة عالية، 
                مما يدعم اتخاذ القرارات الاستراتيجية في سلاسل الإمداد.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("الدخول إلى النظام الرئيسي 🚀"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: الواجهة الرئيسية (الكود السابق) ---
elif st.session_state.page == 'main':
    # إعادة تعيين التنسيق للواجهة الرئيسية (أسود وذهبي)
    st.markdown("""
        <style>
        .stApp { background-image: none; background-color: #0d1117; }
        .main { color: #d4af37; }
        label { color: #d4af37 !important; }
        .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; }
        .best-choice-box { background-color: rgba(212, 175, 55, 0.1); border: 2px solid #d4af37; padding: 20px; border-radius: 10px; text-align: center; color: #d4af37; margin: 20px 0; }
        .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 10px; border-top: 1px solid #d4af37; }
        </style>
    """, unsafe_allow_html=True)

    # قائمة الولايات والشاحنات (نفس الكود السابق)
    wilayas = ["1. أدرار", "2. الشلف", "3. الأغواط", "4. أم البواقي", "5. باتنة", "6. بجاية", "7. بسكرة", "8. بشار", "9. البليدة", "10. البويرة", "11. تمنراست", "12. تبسة", "13. تلمسان", "14. تيارت", "15. تيزي وزو", "16. الجزائر", "17. الجلفة", "18. جيجل", "19. سطيف", "20. سعيدة", "21. سكيكدة", "22. سيدي بلعباس", "23. عنابة", "24. قالمة", "25. قسنطينة", "26. المدية", "27. مستغانم", "28. المسيلة", "29. معسكر", "30. ورقلة", "31. وهران", "32. البيض", "33. إليزي", "34. برج بوعريريج", "35. بومرداس", "36. الطارف", "37. تندوف", "38. تيسمسيلت", "39. الوادي", "40. خنشلة", "41. سوق أهراس", "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة", "46. عين تموشنت", "47. غرداية", "48. غليزان", "49. تيميمون", "50. برج باجي مختار", "51. أولاد جلال", "52. بني عباس", "53. عين صالح", "54. عين قزام", "55. تقرت", "56. جانت", "57. المغير", "58. المنيعة"]

    st.markdown("<div class='university-header'>🎓 جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>📦 نظام التنبؤ بالتكاليف اللوجستية</h1>", unsafe_allow_html=True)
    
    if st.button("⬅️ العودة للترحيب"):
        st.session_state.page = 'welcome'
        st.rerun()

    with st.container():
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### 📍 تفاصيل المسار")
            start_p = st.selectbox("نقطة الانطلاق", wilayas, index=6)
            end_p = st.selectbox("نقطة الوصول", wilayas, index=15)
            dist = st.number_input("المسافة (كم)", value=400.0, step=10.0)
            incoterm = st.selectbox("Incoterms", ["EXW - تسليم المصنع", "FOB - تسليم السفينة", "CIF - التكلفة والتأمين"])
        with col_b:
            st.markdown("### 💵 المعطيات")
            wght_kg = st.number_input("الوزن (كغ)", value=1000.0, step=10.0)
            fuel_price = st.number_input("سعر الوقود (د.ج/لتر)", value=29.1, step=0.1)
            profit_perc = st.slider("هامش الربح (%)", 5, 50, 20)
            chosen_truck = st.selectbox("نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])

    if st.button("التكلفة النهائية"):
        st.balloons()
        t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
        t_names = list(t_map.keys()); t_capacities = [1.5, 5.0, 25.0, 20.0]
        
        def get_cost(t_type_key):
            w_t = wght_kg / 1000.0
            base = ((dist * 0.6) + (w_t * 250)) * t_map[t_type_key]
            fuel = (dist / 5) * fuel_price
            maint = base * 0.15
            total = (base + fuel + maint) * (1 + profit_perc/100) + 1500
            return total, fuel, maint, base

        total_dzd, f_c, m_c, b_c = get_cost(chosen_truck)
        st.markdown(f"""<div style="background-color: #d4af37; padding: 20px; border-radius: 15px; text-align: center; color: black; margin-bottom: 20px; border: 3px solid #fff;"><h2>💰 التكلفة النهائية</h2><h1 style="font-size: 50px;">{total_dzd:,.2f} د.ج</h1></div>""", unsafe_allow_html=True)
        
        # المقارنة والتوصية
        st.markdown("### 📊 المقارنة ودعم القرار")
        results = []
        for t in t_names:
            cost, _, _, _ = get_cost(t)
            status = "✅ مناسب" if (wght_kg/1000.0) <= t_capacities[t_names.index(t)] else "❌ وزن زائد"
            results.append({"نوع الشاحنة": t, "التكلفة (د.ج)": round(cost, 2), "الحالة": status})
        
        df = pd.DataFrame(results)
        valid_indices = df[df['الحالة'] == "✅ مناسب"].index
        def style_df(df_in):
            style = pd.DataFrame('', index=df_in.index, columns=df_in.columns)
            if not valid_indices.empty:
                min_val = df_in.loc[valid_indices, "التكلفة (د.ج)"].min()
                style.loc[df_in["التكلفة (د.ج)"] == min_val, "التكلفة (د.ج)"] = 'background-color: #28a745; color: white;'
            return style
        st.dataframe(df.style.apply(style_df, axis=None), use_container_width=True)

        if not valid_indices.empty:
            best_t = df.loc[df[df['الحالة'] == "✅ مناسب"]["التكلفة (د.ج)"].idxmin(), "نوع الشاحنة"]
            st.markdown(f"<div class='best-choice-box'>💡 توصية النظام: الشاحنة ({best_t}) هي الأنسب لحمولتك.</div>", unsafe_allow_html=True)

    st.markdown(f'<div class="footer">مشروع التخرج: سهيل - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
