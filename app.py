import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام سهيل للتنبؤ اللوجستي", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main(): st.session_state.page = 'main'
def go_to_welcome(): st.session_state.page = 'welcome'

# قائمة الولايات
wilayas_names = [f"{str(i).zfill(2)}. ولاية رقم {i}" for i in range(1, 59)] 

# --- تنسيق CSS لتحسين مظهر الجدول والتوصيات ---
st.markdown("""
    <style>
    * { font-variant-numeric: tabular-nums; font-feature-settings: "tnum"; }
    .stTable { background-color: rgba(0, 0, 0, 0.7) !important; border-radius: 10px; }
    th { color: #d4af37 !important; background-color: rgba(0,0,0,0.8) !important; text-align: center !important; }
    td { color: white !important; font-family: sans-serif !important; text-align: center !important; vertical-align: middle !important; }
    .recommendation-box {
        background-color: rgba(212, 175, 55, 0.2);
        border: 2px solid #d4af37;
        padding: 20px; border-radius: 15px; color: #fff; text-align: center;
        font-size: 18px; backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

# --- الصفحة الأولى ---
if st.session_state.page == 'welcome':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("https://images.unsplash.com/photo-1524522173746-f628baad3644?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; margin-top:50px; border:3px solid #d4af37; padding:40px; border-radius:20px; background:rgba(0,0,0,0.6);"><h1 style="color:#d4af37;">🎓 مشروع التخرج: محاكاة التنبؤ اللوجستي</h1><h2 style="color:white;">جامعة محمد خيضر بسكرة</h2><h3 style="color:#e0e0e0;">إعداد الطالب: سهيل عطالي</h3></div>', unsafe_allow_html=True)
    if st.button("🚀 الدخول للمنصة"): go_to_main(); st.rerun()

# --- الصفحة الثانية ---
elif st.session_state.page == 'main':
    st.markdown("""<style>.stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1500"); background-size: cover; }</style>""", unsafe_allow_html=True)
    
    if st.button("⬅️ رجوع"): go_to_welcome(); st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='background:rgba(13,17,23,0.7); padding:20px; border-radius:15px; border-right:5px solid #d4af37;'>", unsafe_allow_html=True)
        start = st.selectbox("🚩 نقطة الانطلاق", wilayas_names, index=6)
        end = st.selectbox("🏁 نقطة الوصول", wilayas_names, index=15)
        dist = st.number_input("📏 المسافة (كم)", value=500.0)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='background:rgba(13,17,23,0.7); padding:20px; border-radius:15px; border-right:5px solid #d4af37;'>", unsafe_allow_html=True)
        wght = st.number_input("⚖️ الوزن الإجمالي (كغ)", value=3000.0)
        fuel = st.number_input("⛽ سعر الوقود (د.ج)", value=29.1)
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("سيقوم النظام آلياً بترشيح الشاحنة الأنسب")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💎 تحليل البيانات وتوليد النتائج"):
        # خصائص الشاحنات: القدرة (Cap) ومعامل التكلفة (Factor)
        truck_specs = {
            "صغيرة": {"cap": 1500, "factor": 1.0},
            "متوسطة": {"cap": 5000, "factor": 1.4},
            "تبريد": {"cap": 18000, "factor": 2.2},
            "مقطورة دولية": {"cap": 25000, "factor": 2.8}
        }

        comparison_data = []
        valid_options = {}

        # حساب التكاليف لكل سيناريو
        for name, spec in truck_specs.items():
            base_cost = ((dist * 0.8) + ((wght/1000) * 400)) * spec["factor"]
            total = (base_cost + (dist/5)*fuel) * 1.35 # شامل الصيانة والربح
            
            # منطق الملاحظات اللوجستية (Core Logic)
            note = ""
            if wght > spec["cap"]:
                note = "❌ حمولة أكبر من الشاحنة"
            elif wght <= spec["cap"]:
                valid_options[name] = total
                # إذا كان الوزن أقل من نصف قدرة الشاحنة فهي تكاليف ضائعة
                if wght < (spec["cap"] * 0.4):
                    note = "⚠️ مساحة فارغة (تكاليف ضائعة)"
                else:
                    note = "✅ خيار متاح"
            
            comparison_data.append({
                "نوع الشاحنة": name,
                "القدرة القصوى": f"{spec['cap']} كغ",
                "التكلفة التقديرية": f"{total:,.2f} د.ج",
                "التحليل اللوجستي": note
            })

        # تحديد "الأفضل" و "البديل" من الخيارات المتاحة
        if valid_options:
            best_truck = min(valid_options, key=valid_options.get)
            for item in comparison_data:
                if item["نوع الشاحنة"] == best_truck:
                    item["التحليل اللوجستي"] = "⭐ الخيار الأفضل"
                elif item["التحليل اللوجستي"] == "✅ خيار متاح":
                    item["التحليل اللوجستي"] = "🔄 خيار بديل"

        # عرض النتائج
        st.markdown(f'<div style="background:#d4af37; padding:20px; border-radius:15px; text-align:center; color:black;"><h2>النتيجة النهائية (لأقل تكلفة آمنة)</h2><h1>{min(valid_options.values()):,.2f} د.ج</h1></div>', unsafe_allow_html=True)

        st.markdown("### 📋 جدول المقارنة وتحليل كفاءة التحميل")
        st.table(pd.DataFrame(comparison_data))

        st.markdown(f"""
            <div class="recommendation-box">
                💡 <b>ملخص القرار:</b> تم اختيار <b>{best_truck}</b> لأنها توفر أعلى كفاءة امتلاء بأقل سعر مسار. 
                تجنب الخيارات الموسومة بـ (تكاليف ضائعة) لتقليل الهدر المالي في مشروعك.
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#d4af37; margin-top:30px;'>مشروع التخرج: سهيل عطالي - جامعة بسكرة 2026</p>", unsafe_allow_html=True)
