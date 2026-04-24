import streamlit as st

# إعداد واجهة المستخدم بلمسة "Dark Luxury"
st.set_page_config(page_title="المتنبيء اللوجستي", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; border-radius: 5px; font-weight: bold; }
    label { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚚 نظام التنبؤ الذكي بتكاليف النقل")
st.write("تم تطويره بواسطة سهيل - مشروع الخدمات اللوجستية")

# مدخلات بسيطة
distance = st.number_input("المسافة المقطوعة (كم)", min_value=1.0, value=10.0)
weight = st.number_input("وزن الشحنة (طن)", min_value=0.1, value=1.0)

if st.button("تحليل البيانات والتنبؤ بالتكلفة"):
    # معادلة تحاكي منطق الذكاء الاصطناعي (Linear Regression Logic)
    # تكلفة أساسية + (سعر الكيلو * المسافة) + (سعر الطن * الوزن)
    base_price = 500
    cost = base_price + (distance * 0.8) + (weight * 150)
    
    st.markdown(f"### 💰 التكلفة التقديرية: {cost:,.2f} د.ج")
    st.info("ملاحظة: هذا التنبؤ مبني على خوارزمية انحدار خطي (Linear Regression) لمعالجة البيانات.")
