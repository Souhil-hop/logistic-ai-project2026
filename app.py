import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. التنسيق الفخم
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { 
        background-color: #d4af37; 
        color: black; 
        width: 100%; 
        font-weight: bold; 
        border-radius: 8px; 
        border: none; 
        height: 50px; 
    }
    label { color: #d4af37 !important; font-size: 16px; }
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .best-choice-box {
        background-color: rgba(212, 175, 55, 0.1);
        border: 2px solid #d4af37;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: #d4af37;
        margin: 20px 0;
    }
    .footer { 
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0d1117; color: #d4af37; 
        text-align: center; padding: 10px; border-top: 1px solid #d4af37; 
    }
    </style>
    """, unsafe_allow_html=True)

wilayas = [
    "1. أدرار", "2. الشلف", "3. الأغواط", "4. أم البواقي", "5. باتنة", "6. بجاية", "7. بسكرة", "8. بشار", "9. البليدة", "10. البويرة",
    "11. تمنراست", "12. تبسة", "13. تلمسان", "14. تيارت", "15. تيزي وزو", "16. الجزائر", "17. الجلفة", "18. جيجل", "19. سطيف", "20. سعيدة",
    "21. سكيكدة", "22. سيدي بلعباس", "23. عنابة", "24. قالمة", "25. قسنطينة", "26. المدية", "27. مستغانم", "28. المسيلة", "29. معسكر", "30. ورقلة",
    "31. وهران", "32. البيض", "33. إليزي", "34. برج بوعريريج", "35. بومرداس", "36. الطارف", "37. تندوف", "38. تيسمسيلت", "39. الوادي", "40. خنشلة",
    "41. سوق أهراس", "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة", "46. عين تموشنت", "47. غرداية", "48. غليزان", "49. تيميمون", "50. برج باجي مختار",
    "51. أولاد جلال", "52. بني عباس", "53. عين صالح", "54. عين قزام", "55. تقرت", "56. جانت", "57. المغير", "58. المنيعة"
]

st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ بالتكاليف اللوجستية")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 📍 تفاصيل المسار")
        start_p = st.selectbox("نقطة الانطلاق (Origin)", wilayas, index=6)
        end_p = st.selectbox("نقطة الوصول (Destination)", wilayas, index=15)
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0, step=10.0)
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms)", ["EXW - تسليم المصنع", "FOB - تسليم السفينة", "CIF - التكلفة والتأمين"])
    with col_b:
        st.markdown("### 💵 المعطيات والأسعار")
        wght_kg = st.number_input("الوزن القائم (كغ)", value=1000.0, step=10.0)
        fuel_price = st.number_input("سعر الوقود (د.ج/لتر)", value=29.1, step=0.1)
        profit_perc = st.slider("هامش الربح (%)", 5, 50, 20)
        chosen_truck = st.selectbox("نوع الشاحنة المختارة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])

if st.button("التكلفة النهائية"): # الزر المختصر
    t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    t_names = list(t_map.keys())
    t_capacities = [1.5, 5.0, 25.0, 20.0]
    
    def get_cost(t_type_key):
        w_t = wght_kg / 1000.0
        base = ((dist * 0.6) + (w_t * 250)) * t_map[t_type_key]
        fuel = (dist / 5) * fuel_price
        maint = base * 0.15
        total = (base + fuel + maint) * (1 + profit_perc/100) + 1500
        return total, fuel, maint, base

    # 1. عرض النتيجة الفورية (أولاً)
    total_dzd, f_c, m_c, b_c = get_cost(chosen_truck)
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 20px; border-radius: 15px; text-align: center; color: black; margin-bottom: 20px;">
            <h2>💰 التكلفة التقديرية (الخيار المختار)</h2>
            <h1 style="font-size: 50px;">{total_dzd:,.2f} د.ج</h1>
        </div>
    """, unsafe_allow_html=True)

    # 2. هيكلة التكاليف
    st.markdown(f"### 📋 تفصيل تكاليف شاحنة {chosen_truck}")
    st.table({
        "بند التكلفة": ["الوقود", "الصيانة", "التشغيل", "هامش الربح"],
        "القيمة (د.ج)": [f"{f_c:,.2f}", f"{m_c:,.2f}", f"{b_c:,.2f}", f"{(total_dzd - (f_c+m_c+b_c+1500)):,.2f}"]
    })

    # 3. جدول المقارنة مع التلوين (ثانياً)
    st.write("---")
    st.markdown("### 📊 جدول المقارنة ودعم القرار")
    results = []
    for t in t_names:
        cost, _, _, _ = get_cost(t)
        status = "✅ مناسب" if (wght_kg/1000.0) <= t_capacities[t_names.index(t)] else "❌ وزن زائد"
        results.append({"نوع الشاحنة": t, "التكلفة الكلية (د.ج)": round(cost, 2), "الحالة": status})
    
    df = pd.DataFrame(results)
    
    # وظيفة التلوين بالأخضر لأقل سعر مناسب
    def highlight_min(s):
        is_min = s == df[df['الحالة'] == "✅ مناسب"]['التكلفة الكلية (د.ج)'].min()
        return ['background-color: #00ff00; color: black; font-weight: bold' if v else '' for v in is_min]

    st.dataframe(df.style.apply(highlight_min, subset=['التكلفة الكلية (د.ج)']), use_container_width=True)

    # 4. التوصية (في الأخير)
    valid_df = df[df["الحالة"] == "✅ مناسب"]
    if not valid_df.empty:
        best = valid_df.loc[valid_df["التكلفة الكلية (د.ج)"].idxmin()]
        st.markdown(f"<div class='best-choice-box'>💡 التوصية الذكية: الشاحنة <b>({best['نوع الشاحنة']})</b> هي الخيار الأرخص والأنسب حالياً.</div>", unsafe_allow_html=True)

    # 5. التقييم
    st.write("---")
    st.markdown("### 🧪 رأيك في دقة النظام")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("✅ دقيق جداً"): st.success("شكراً لتقييمك!"); st.balloons()
    with c2: 
        if st.button("❌ يحتاج تحسين"): st.warning("سيتم العمل على تطوير الخوارزمية.")

st.markdown(f'<div class="footer">مشروع التخرج: سهيل - تخصص اللوجستيك - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
