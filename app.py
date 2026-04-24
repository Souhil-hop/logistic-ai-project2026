if st.button("تشغيل خوارزمية التنبؤ (Run Keras Model)"):
    # منطق الأوزان (Weights)
    truck_weight = 1.0
    if "متوسطة" in truck_type: truck_weight = 1.4
    elif "مقطورة" in truck_type: truck_weight = 2.2
    elif "تبريد" in truck_type: truck_weight = 2.8
    
    # تأثير الوقود
    fuel_impact = (dist / 5) * fuel_price
    
    # التنبؤ النهائي
    prediction = ((dist * 0.6) + (wght * 250)) * truck_weight + fuel_impact + 1500
    
    # --- التعديل الجديد: عرض النتيجة داخل أيقونة وبطاقة فخمة ---
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 20px; border-radius: 15px; text-align: center;">
            <h2 style="color: black; margin: 0;">💰 التكلفة التقديرية</h2>
            <p style="color: black; font-size: 32px; font-weight: bold; margin: 10px 0;">
                {prediction:,.2f} <span style="font-size: 18px;">د.ج</span>
            </p>
            <p style="color: #333; font-size: 14px; margin: 0;">من {start_point} إلى {end_point}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons() # إضافة حركة بالونات احتفالية عند ظهور النتيجة
