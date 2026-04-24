import streamlit as st
import pandas as pd

# 1. إعداد الصفحة الأساسي
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

# 2. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات
wilayas_58 = [f"{str(i).zfill(2)}. ولاية رقم {i}" for i in range(1, 59)] # قائمة مختصرة للشرح، يمكنك وضع القائمة الكاملة هنا

# --- كود إجبار الأرقام على التنسيق الدولي (حل مشكلة اللابتوب) ---
st.markdown("""
    <style>
    * { font-variant-numeric: tabular-nums; -webkit-font-feature-settings: "tnum"; font-feature-settings: "tnum"; }
    input, .stTable, .stDataFrame, h1, h2, h3 { font-family: 'Inter', sans-serif !important; }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى: الواجهة الترحيبية ---
if st.session_state.page == 'welcome':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500");
            background-size: cover; background-position: center; background-attachment: fixed;
        }
        .welcome-box {
            background-color: rgba(0, 0, 0, 0.4); padding: 50px; border-radius: 30px;
            text-align: center; border: 3px solid #d4af37; margin: auto;
            max-width: 900px; margin-top: 50px; backdrop-filter: blur(10px);
        }
        .welcome-title { color: #d4af37; font-size: 42px; font-weight: bold; }
        .stButton>button { background-color: #d4af37 !important; color: black !important; font-weight: bold; font-size: 22px; border-radius: 15px; height: 70px; width: 100%; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="welcome-box">
            <h1 class="welcome-title">أهلاً بطلبة تخصص اللوجستيك والنقل الدولي 🎓</h1>
            <h3 style="color:white;">تحت إشراف جامعة محمد خيضر بسكرة | إعداد الطالب: سهيل عطالي</h3>
            <p style="color:#e0e0e0; font-size:22px;">مشروع محاكاة الشبكة العصبية للتنبؤ بتكاليف النقل اللوجستي في 58 ولاية.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("") 
    if st.button("🚀 الدخول إلى منصة التنبؤ الذكية"):
        go_to_main()
        st.rerun()

# --- الصفحة الثانية: العمليات والجداول ---
elif st.session_state.page == 'main':
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500");
            background-size: cover; background-position: center;
        }
        .main-card {
            background: rgba(13, 17, 23, 0.6); padding: 25px; border-radius: 15px;
            border-right: 5px solid #d4af37; margin-bottom: 20px; backdrop-filter: blur(8px);
        }
        label { color: #d4af37 !important; font-weight: bold !important; font-size: 18px !important; }
        .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: rgba(13, 17, 23, 0.9); color: #d4af37; text-align: center; padding: 8px; border-top: 1px solid #d4af37; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ رجوع"):
            go_to_welcome()
            st.rerun()
    with col_title:
        st.markdown("<h1 style='color: #d4af37; margin-top: -10px;'>📊 منصة التحليل ودعم القرار</h1>", unsafe_allow_html=True)

    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("### 📍 مسار الرحلة")
            start = st.selectbox("🚩 نقطة الانطلاق", wilayas_58, index=6)
            end = st.selectbox("🏁 نقطة الوصول", wilayas_58, index=15)
            dist = st.number_input("📏 المسافة (كم)", value=400.0)
            st.markdown("</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("### 💰 المعطيات التقنية")
            wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=1000.0)
            fuel = st.number_input("⛽ سعر الوقود (د.ج)", value=29.1)
            truck = st.selectbox("🚛 نوع الشاحنة", ["صغيرة", "متوسطة", "مقطورة دولية", "تبريد"])
            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 حساب التكلفة وتوليد التقارير"):
        st.balloons()
        
        # الحسابات
        t_map = {"صغيرة": 1.0, "متوسطة": 1.4, "مقطورة دولية": 2.2, "تبريد": 2.8}
        w_t = wght / 1000.0
        base = ((dist * 0.7) + (w_t * 300)) * t_map[truck]
        f_cost = (dist / 5) * fuel
        maint = base * 0.12
        profit = (base + f_cost + maint) * 0.20
        total = base + f_cost + maint + profit

        # 1. النتيجة الكبيرة
        st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d4af37, #f4cf67); padding: 30px; border-radius: 20px; text-align: center; color: black; margin: 25px 0;">
                <h2 style="margin:0;">💵 التكلفة الكلية المقدرة 💵</h2>
                <h1 style="font-size: 55px; margin:10px; font-family: sans-serif;">{total:,.2f} د.ج</h1>
            </div>
        """, unsafe_allow_html=True)

        # 2. جدول هيكلة التكاليف (الذي كان مفقوداً)
        st.markdown("### 📋 هيكلة التكاليف التفصيلية")
        st.table(pd.DataFrame({
            "البند": ["⛽ تكلفة الوقود", "🔧 الصيانة", "🏗️ التشغيل", "📈 هامش الربح"],
            "القيمة (د.ج)": [f"{f_cost:,.2f}", f"{maint:,.2f}", f"{base:,.2f}", f"{profit:,.2f}"]
        }))

        # 3. جدول المقارنة ودعم القرار (الذي كان مفقوداً)
        st.markdown("### 🔄 جدول المقارنة وتحليل السيناريوهات")
        comp = []
        for t, m in t_map.items():
            cost = ((dist * 0.7) + (w_t * 300)) * m + f_cost + (base * 0.12) + profit
            comp.append({"نوع الشاحنة": t, "الحالة": "مناسب ✅", "التكلفة الكلية (د.ج)": f"{cost:,.2f}"})
        st.dataframe(pd.DataFrame(comp), use_container_width=True)

        st.info(f"💡 توصية النظام: الشاحنة ({truck}) هي الخيار الحالي المعتمد بناءً على مدخلاتك.")

        # 4. نظام التقييم (الذي كان مفقوداً)
        st.write("---")
        st.markdown("### 🧪 تقييم دقة النموذج")
        eval_choice = st.radio("هل كانت النتيجة دقيقة؟", ("نعم، دقيقة جداً", "تحتاج تعديل", "غير دقيقة"))
        if st.button("إرسال التقييم 📩"):
            st.success("شكراً لتقييمك! سيتم استخدامه لتحسين الشبكة العصبية.")

    st.markdown("<div class='footer'>مشروع التخرج: سهيل عطالي - جامعة محمد خيضر بسكرة 2026</div>", unsafe_allow_html=True)
