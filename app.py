import streamlit as st
import time

# 1. إعداد الصفحة
st.set_page_config(page_title="منصة سهيل اللوجستية الذكية", layout="wide")

# 2. التنسيق الفخم (أسود وذهبي)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 8px; width: 100%; height: 50px; }
    .university-header { text-align: center; color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #d4af37; text-align: center; padding: 10px; border-top: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# 3. وظيفة المساعد الصوتي (JavaScript) - خارج الصندوق فعلاً!
def speak_result(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'ar-SA';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# 4. الهيدر الرسمي
st.markdown("<div class='university-header'>🎓 برعاية جامعة محمد خيضر - بسكرة | كلية العلوم الاقتصادية والتجارية</div>", unsafe_allow_html=True)
st.title("📦 نظام التنبؤ اللوجستي المتحدث")
st.markdown("<h3 style='text-align: center; color: #d4af37;'>إعداد الطالب: سهيل</h3>", unsafe_allow_html=True)

# 5. المدخلات
col1, col2 = st.columns(2)
with col1:
    start_p = st.text_input("نقطة الانطلاق", "بسكرة")
    dist = st.number_input("المسافة (كم)", value=400.0)
with col2:
    end_p = st.text_input("نقطة الوصول", "الجزائر العاصمة")
    truck = st.selectbox("نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة", "تبريد"])

# 6. زر التحليل مع الصوت
if st.button("بدء التحليل الصوتي والتقني"):
    # الحسابات
    t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة": 2.2, "تبريد": 2.8}
    prediction = ((dist * 0.6) + (1 * 250)) * t_map[truck] + (dist/5 * 29) + 1500
    
    # عرض النتيجة
    st.markdown(f"""
        <div style="background-color: #d4af37; padding: 20px; border-radius: 15px; text-align: center; color: black;">
            <h2>التكلفة التقديرية</h2>
            <h1>{prediction:,.2f} د.ج</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # تشغيل المساعد الصوتي
    voice_text = f"تم تحليل البيانات. التكلفة التقديرية للرحلة من {start_p} إلى {end_p} هي {int(prediction)} دينار جزائري. شكراً لاستخدام نظام سهيل الذكي."
    speak_result(voice_text)
    
    st.balloons()

st.markdown(f'<div class="footer">مشروع الطالب سهيل - جامعة بسكرة 2026</div>', unsafe_allow_html=True)
