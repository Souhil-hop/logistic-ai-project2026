import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. التنسيق الفخم (أسود وذهبي)
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

# قائمة ولايات الجزائر الـ 58
wilayas = [
    "1. أدرار", "2. الشلف", "3. الأغواط", "4. أم البواقي", "5. باتنة", "6. بجاية", "7. بسكرة", "8. بشار", "9. البليدة", "10. البويرة",
    "11. تمنراست", "12. تبسة", "13. تلمسان", "14. تيارت", "15. تيزي وزو", "16. الجزائر", "17. الجلفة", "18. جيجل", "19. سطيف", "20. سعيدة",
    "21. سكيكدة", "22. سيدي بلعباس", "23. عنابة", "24. قالمة", "25. قسنطينة", "26. المدية", "27. مستغانم", "28. المسيلة", "29. معسكر", "30. ورقلة",
    "31. وهران", "32. البيض", "33. إليزي", "34. برج بوعريريج", "35. بومرداس", "36. الطارف", "37. تندوف", "38. تيسمسيلت", "39. الوادي", "40. خنشلة",
    "41. سوق أهراس", "42. تيبازة", "43. ميلة", "44. عين الدفلى", "45. النعامة", "46. عين تموشنت", "47. غرداية", "48. غليزان", "49. تيميمون", "50. برج باجي مختار",
    "51. أولاد جلال", "52. بني عباس", "53. عين صالح", "54. عين قزام", "55. تقرت", "56. جانت", "57. المغير", "58. المنيعة"
]

# 3. الهيدر الرسمي
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ بالتكاليف اللوجستية")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. واجهة المدخلات
with st.container():
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📍 تفاصيل المسار")
        start_p = st.selectbox("نقطة الانطلاق (Origin)", wilayas, index=wilayas.index("7. بسكرة"))
        end_p = st.selectbox("نقطة الوصول (Destination)", wilayas, index=wilayas.index("16. الجزائر"))
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0, step=10.0)
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms)", [
            "EXW - تسليم المصنع (أقل مسؤولية على البائع)", 
            "FOB - تسليم على ظهر السفينة (توزيع مسؤولية)", 
            "CIF - التكلفة والتأمين والشحن (أكثر مسؤولية على البائع)"
        ])
        
    with col_b:
        st.markdown("### 💵 المعطيات المالية والتقنية")
        wght_kg = st.number_input("الوزن القائم (كغ)", value=1000.0, step=10.0)
        wght = wght_kg / 1000.0 
        fuel_price = st.number_input("سعر الوقود (د.ج/لتر)", value=29.1, step=0.1)
        profit_perc = st.slider("هامش الربح المستهدف (%)", 5, 50, 20)
        chosen_truck = st.selectbox("الشاحنة المفضلة لعرض تفاصيلها", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])

# 5. الحسابات
if st.button("تشغيل التحليل اللوجستي الشامل ودعم القرار"):
    t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    t_names = ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"]
    t_capacities = [1.5, 5.0, 25.0, 20.0]
    
    def get_cost(t_type_key):
        base = ((dist * 0.6) + (wght * 250)) * t_map[t_type_key]
        fuel = (dist / 5) * fuel_price
        maint = base * 0.15
        total = (base + fuel + maint) * (1 + profit_perc/100) + 1500
        return total, fuel, maint, base

    # أ) جدول المقارنة الشاملة
    results = []
    for t_name in t_names:
        total, f_cost, m_cost, b_cost = get_cost(t_name)
        status = "❌ الوزن زائد" if wght > t_capacities[t_names.index(t_name)] else "✅ مناسب"
        results.append({
            "نوع الشاحنة": t_name,
            "السعة (طن)": t_capacities[t_names.index(t_name)],
            "التكلفة الكلية (د.ج)": round(total, 2),
            "الحالة لوزنك": status
        })

    df = pd.DataFrame(results)
    st.markdown("### 📊 جدول المقارنة الشامل")
    st.dataframe(df, use_container_width=True)

    # ب) التوصية الذكية
    st.markdown("---")
    valid_df = df[df["الحالة لوزنك"] == "✅ مناسب"]
    if not valid_df.empty:
        best_row = valid_df.loc[valid_df["التكلفة الكلية (د.ج)"].idxmin()]
        rec_text = f"💡 التوصية: الشاحنة **({best_row['نوع الشاحنة']})** هي الأفضل اقتصادياً لحمولتك بسعر {best_row['التكلفة الكلية (د.ج)']:,.2f} د.ج."
    else:
        rec_text = "🚨 تنبيه: الوزن المدخل يتجاوز قدرة جميع الشاحنات المتاحة."
    
    st.markdown(f"<div class='best-choice-box'>{rec_text}</div>", unsafe_allow_html=True)

    # ج) هيكلة التكاليف
    total_dzd, f_cost, m_cost, b_cost = get_cost(chosen_truck)
    profit_val = (b_cost + f_cost + m_cost) * (profit_perc / 100)
    st.markdown(f"### 📋 هيكلة تكاليف الشاحنة المختارة ({chosen_truck})")
    st.table({
        "البند": ["تكلفة الوقود", "الصيانة", "أجرة المسار", "هامش الربح", "المجموع النهائي"],
        "القيمة (د.ج)": [f"{f_cost:,.2f}", f"{m_cost:,.2f}", f"{b_cost:,.2f}", f"{profit_val:,.2f}", f"{total_dzd:,.2f}"]
    })

    # د) خانة الرأي والتقييم (التي طلبتها)
    st.write("---")
    st.markdown("### 🧪 تقييم النظام ودقة التنبؤ")
    st.write("هل تجد أن هذه الحسابات منطقية وتطابق واقع السوق؟")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("✅ نعم، التنبؤ دقيق"):
            st.success("شكراً لك! تم تسجيل رأيك لتحسين أوزان النظام.")
            st.balloons()
    with col_f2:
        if st.button("❌ لا، يحتاج تعديل"):
            st.warning("شكراً لك! سيتم مراجعة الخوارزمية لتقليل هامش الخطأ.")
    
    st.text_area("أضف أي اقتراحات أخرى لتحسين المشروع:")

st.markdown(f'<div class="footer">مشروع التخرج: سهيل - تخصص اللوجستيك والنقل الدولي - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
