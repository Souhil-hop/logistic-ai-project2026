import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# إعدادات الصفحة (تظهر في المتصفح)
st.set_page_config(page_title="تنبؤ تكاليف النقل", layout="centered")

# --- 1. بناء وتدريب النموذج (سيتم تدريبه مرة واحدة عند التشغيل) ---
@st.cache_resource
def initial_model_setup():
    # بيانات تدريب افتراضية (المسافة بالكلم، الوزن بالطن) -> التكلفة بالدينار
    X_train = np.array([
        [100, 2], [200, 5], [350, 7], [600, 10], 
        [50, 1], [800, 15], [1000, 20], [150, 3],
        [450, 8], [300, 4], [700, 12], [550, 9]
    ], dtype=float)
    
    # مخرجات التدريب (التكلفة)
    y_train = np.array([1500, 3200, 4800, 8200, 900, 11500, 15500, 2100, 5100, 3400, 9300, 6200], dtype=float)

    # بناء الشبكة العصبية
    model = Sequential([
        Dense(units=16, activation='relu', input_shape=[2]), # طبقة الإدخال
        Dense(units=8, activation='relu'),                  # طبقة مخفية
        Dense(units=1)                                       # طبقة المخرجات (السعر)
    ])
    
    # ضبط الإعدادات
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # تدريب النموذج
    model.fit(X_train, y_train, epochs=400, verbose=0)
    
    return model

# تحميل النموذج
with st.spinner('جاري تشغيل محرك الذكاء الاصطناعي...'):
    model = initial_model_setup()

# --- 2. تصميم الواجهة (Streamlit) ---

# كتابة العناوين باللغة العربية
st.title("🚚 نظام التنبؤ الذكي بتكاليف النقل")
st.write("هذا النموذج يستخدم **الشبكات العصبية (Keras)** لتقدير أسعار الشحن بناءً على المسافة والحمولة.")

st.divider() # خط فاصل

# إنشاء خانات الإدخال
col1, col2 = st.columns(2)

with col1:
    distance = st.number_input("المسافة المقطوعة (كيلومتر):", min_value=1, max_value=2000, value=100)

with col2:
    weight = st.number_input("وزن الحمولة (طن):", min_value=0.1, max_value=50.0, value=1.0)

# زر التنبؤ
if st.button("احسب التكلفة المتوقعة"):
    # تجهيز المدخلات للنموذج
    features = np.array([[distance, weight]])
    
    # التنبؤ
    prediction = model.predict(features)
    final_cost = max(0, prediction[0][0]) # التأكد أن السعر ليس سالباً
    
    # عرض النتيجة
    st.info(f"بناءً على النماذج اللوجستية، التكلفة التقديرية هي:")
    st.success(f"### {final_cost:,.2f} دينار جزائري")
    
    # تفاصيل إضافية للبحث
    with st.expander("شرح تقني للنتيجة"):
        st.write(f"""
        تم حساب هذه القيمة باستخدام شبكة عصبية مكونة من 3 طبقات. 
        المدخلات المعالجة: {distance} كلم و {weight} طن.
        الخوارزمية المستخدمة للتصحيح: Adam Optimizer.
        """)

# تذييل الصفحة
st.markdown("---")
st.caption("مشروع واجب منزلي - نموذج تجريبي للتنبؤ اللوجستي")
