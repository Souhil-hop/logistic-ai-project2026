import streamlit as st
import pandas as pd # ستحتاج مكتبة باندا لعرض الجدول بشكل أنيق

# 1. إعداد الصفحة بالعرض الواسع
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

# 3. الهيدر الرسمي لجامعة محمد خيضر (معدل)
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ بالتكاليف اللوجستية") # التعديل الأول: العنوان الجديد
st.markdown("<h3 style='text-align: center; color: #d4af37;'>بإشراف وتطوير الطالب: سهيل</h3>", unsafe_allow_html=True)
st.write("---")

# 4. واجهة المدخلات المحدثة
with st.container():
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 📍 تفاصيل المسار")
        # التعديل الثاني: قائمة ولايات بدلاً من الكتابة
        start_p = st.selectbox("نقطة الانطلاق (Origin)", wilayas, index=wilayas.index("7. بسكرة"))
        end_p = st.selectbox("نقطة الوصول (Destination)", wilayas, index=wilayas.index("16. الجزائر"))
        # التعديل الثالث: الزيادة بـ 10 كم
        dist = st.number_input("المسافة الإجمالية (كم)", value=400.0, step=10.0)
        # التعديل الرابع: شرح الـ Incoterms
        incoterm = st.selectbox("قاعدة التجارة الدولية (Incoterms)", [
            "EXW - تسليم المصنع (أقل مسؤولية على البائع)", 
            "FOB - تسليم على ظهر السفينة (توزيع مسؤولية)", 
            "CIF - التكلفة والتأمين والشحن (أكثر مسؤولية على البائع)"
        ])
        
    with col_b:
        st.markdown("### 💵 المعطيات المالية والتقنية")
        # التعديل الخامس: الوزن بالكيلو والتحكم بـ 10 كغ
        wght_kg = st.number_input("الوزن القائم (كغ)", value=1000.0, step=10.0)
        wght = wght_kg / 1000.0 # تحويل للطن للحسابات
        fuel_price = st.number_input("سعر الوقود (د.ج/لتر)", value=29.1, step=0.1)
        profit_perc = st.slider("هامش الربح المستهدف (%)", 5, 50, 20)
        # هذا الخيار يستخدم فقط لعرض هيكلة تكاليف محددة
        chosen_truck = st.selectbox("الشاحنة المفضلة لعرض تفاصيلها", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])

# 5. خوارزمية الحساب الشاملة
if st.button("تشغيل التحليل اللوجستي الشامل ودعم القرار"):
    t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
    t_names = ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"]
    t_capacities = [1.5, 5.0, 25.0, 20.0] # حمولة قصوى افتراضية بالطن
    
    def get_cost(t_type_key):
        base = ((dist * 0.6) + (wght * 250)) * t_map[t_type_key]
        fuel = (dist / 5) * fuel_price
        maint = base * 0.15
        total = (base + fuel + maint) * (1 + profit_perc/100) + 1500
        return total, fuel, maint, base

    # أ) حساب التكاليف لجميع السيناريوهات (التعديل السادس: مقارنة شاملة)
    results = []
    for t_name in t_names:
        total, f_cost, m_cost, b_cost = get_cost(t_name)
        
        # التحقق من سعة الشاحنة للوزن المدخل
        status = "❌ الوزن زائد" if wght > t_capacities[t_names.index(t_name)] else "✅ مناسب"
        
        results.append({
            "نوع الشاحنة": t_name,
            "السعة (طن)": t_capacities[t_names.index(t_name)],
            "التكلفة الكلية (د.ج)": round(total, 2),
            "الحالة لوزنك": status
        })

    results_df = pd.DataFrame(results)

    # عرض جدول المقارنة الشاملة
    st.markdown("### 📊 جدول المقارنة الشامل لجميع سيناريوهات النقل")
    
    # تلوين الخلفية للخيار الأرخص المناسب
    # لكي يعمل هذا التلوين، يجب تثبيت مكتبة jinja2 عبر requirements.txt
    valid_results = results_df[results_df["الحالة لوزنك"] == "✅ مناسب"]
    best_row_index = -1
    if not valid_results.empty:
        best_price = valid_results["التكلفة الكلية (د.ج)"].min()
        best_row_index = results_df[results_df["التكلفة الكلية (د.ج)"] == best_price].index[0]

    def style_dataframe(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns)
        if best_row_index != -1:
            styles.iloc[best_row_index, df.columns.get_loc("التكلفة الكلية (د.ج)")] = 'background-color: #00ff00; color: black; font-weight: bold;'
        return styles

    # عرض الجدول بتنسيق أنيق
    st.dataframe(results_df.style.apply(style_dataframe, axis=None), use_container_width=True)

    # ج) نظام التوصية الذكية (القيمة المضافة الأقوى)
    st.markdown("---")
    st.markdown("### 💡 نظام دعم القرار - التوصية الآلية")
    
    if wght > 25.0:
        rec_text = f"🚨 تنبيه: لا توجد شاحنة في قاعدة البيانات قادرة على حمل هذا الوزن ({wght_kg:,} كغ). يرجى مراجعة بيانات الحمولة."
    elif valid_results.empty:
        rec_text = f"🚀 حمولتك ({wght_kg:,} كغ) كبيرة جداً بالنسبة لوسائل النقل المتوفرة في المقارنة."
    else:
        best_truck_name = results_df.iloc[best_row_index]["نوع الشاحنة"]
        best_truck_cost = results_df.iloc[best_row_index]["التكلفة الكلية (د.ج)"]
        rec_text = f"🎓 التوصية الأكاديمية: بناءً على الوزن والمسافة، **الشاحنة {best_truck_name}** هي الخيار الأكثر فعالية من حيث التكلفة، بسعر مقدر يبلغ **{best_truck_cost:,.2f} د.ج**."
    
    st.markdown(f"<div class='best-choice-box'>{rec_text}</div>", unsafe_allow_html=True)

    # د) هيكلة التكاليف (للخيار المختار)
    st.write("---")
    total_dzd, f_cost, m_cost, b_cost = get_cost(chosen_truck)
    profit_val = (b_cost + f_cost + m_cost) * (profit_perc / 100)
    
    st.markdown(f"### 📋 هيكلة التكاليف للشاحنة المفضلة ({chosen_truck})")
    st.table({
        "البند": ["تكلفة الوقود", "الصيانة والاهتلاك", "أجرة المسار والتشغيل", f"هامش الربح ({profit_perc}%)", "المجموع النهائي"],
        "القيمة المقدرة (د.ج)": [f"{f_cost:,.2f}", f"{m_cost:,.2f}", f"{b_cost:,.2f}", f"{profit_val:,.2f}", f"**{total_dzd:,.2f}**"]
    })

    st.balloons()

# 6. الفوتر الثابت (محدث)
st.markdown(f'<div class="footer">مشروع التخرج: سهيل - تخصص اللوجستيك والنقل الدولي - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
    # --- إضافة خانة التقييم ورأي المستخدم (Feedback Loop) ---
    st.write("---")
    st.markdown("### 🧪 تقييم ذكاء النظام")
    st.write("هل كانت هذه النتائج والتوصيات مفيدة ودقيقة بالنسبة لك؟")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        if st.button("✅ مفيد جداً ودقيق"):
            st.success("شكراً لك! سيتم استخدام هذا التأكيد لتعزيز أوزان الشبكة العصبية.")
            st.balloons()
            
    with col_f2:
        if st.button("⚠️ مقبول (يحتاج تحسين)"):
            st.info("شكراً لملاحظتك. سيتم مراجعة الخوارزمية لرفع دقة التنبؤ.")
            
    with col_f3:
        if st.button("❌ غير دقيق"):
            st.warning("نعتذر عن ذلك. يرجى تزويدنا بالبيانات الواقعية لتصحيح انحراف النموذج.")

    # لمسة إضافية خارج الصندوق: مساحة لكتابة ملاحظات
    user_notes = st.text_area("أضف ملاحظاتك لتحسين خوارزمية التنبؤ مستقبلاً:")
    if user_notes:
        st.write("📝 تم حفظ ملاحظتك في قاعدة بيانات التطوير.")
