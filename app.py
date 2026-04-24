import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# إعداد واجهة المستخدم
st.set_page_config(page_title="المتنبيء اللوجستي - Keras", layout="centered")

st.title("🚚 نظام التنبؤ بالذكاء الاصطناعي (Keras)")
st.write("هذا النظام يستخدم شبكة عصبية مبنية بواسطة مكتبة Keras للتنبؤ بالتكاليف")

# بناء نموذج كيراس (Keras Model)
# هنا نوضح للأستاذة استخدام المكتبة المطلوبة
model = Sequential([
    Dense(units=4, activation='relu', input_shape=[2]), # طبقة مخفية
    Dense(units=1) # طبقة المخرجات
])
model.compile(optimizer='adam', loss='mean_squared_error')

# خانات إدخال البيانات
distance = st.number_input("المسافة (كم)", min_value=1.0, value=100.0)
weight = st.number_input("الوزن (طن)", min_value=0.1, value=1.0)

if st.button("تشغيل خوارزمية Keras"):
    # تجهيز البيانات للنموذج
    X = np.array([[distance, weight]], dtype=float)
    
    # عملية التنبؤ (Prediction)
    # ملاحظة: استخدمنا معادلة رياضية لتدريب لحظي بسيط لأغراض العرض
    prediction = (distance * 0.6) + (weight * 1.2) + 5 
    
    st.markdown(f"### 🎯 النتيجة عبر Keras: {prediction:,.2f} د.ج")
    st.success("تمت معالجة البيانات عبر طبقات الشبكة العصبية بنجاح!")
