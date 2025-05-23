import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="MatchGrad智能读研推荐平台", layout="wide")
st.title("🎓 MatchGrad：AI智能读研与导师匹配平台")
st.markdown("为考研学生提供个性化学校、专业、导师推荐和自荐材料生成")

# --- 左栏：考生信息输入 ---
st.sidebar.header("📝 填写你的考生信息")
name = st.sidebar.text_input("姓名")
edu_bg = st.sidebar.selectbox("本科专业", [
    "建筑环境与能源应用工程", "给排水科学与工程", "土木工程", "环境工程", "建筑电气与智能化",
    "能源与动力工程", "城市地下空间工程", "机械工程", "自动化", "计算机科学与技术", "其他"
])
gpa = st.sidebar.slider("本科成绩绩点 (GPA)", 2.0, 4.5, 3.2, 0.1)
location_pref = st.sidebar.multiselect("意向地区", [
    "北京", "上海", "西安", "成都", "武汉", "广州", "南京", "哈尔滨", "重庆", "青岛", "不限"
])
interest_field = st.sidebar.selectbox("科研兴趣方向", [
    "绿色建筑", "建筑节能", "暖通系统仿真", "碳中和/碳达峰", "智能控制", "热舒适",
    "可再生能源", "环境健康", "其他"
])

@st.cache_data
def load_school_data():
    return pd.read_csv("majors_data_large.csv")

school_data = load_school_data()

if st.sidebar.button("🔍 获取推荐"):
    st.subheader(f"👤 推荐结果：{name} 同学的智能推荐如下")

    filtered = school_data[
        school_data["专业方向"].str.contains(interest_field, case=False, na=False) &
        (school_data["地区"].isin(location_pref) | school_data["地区"] == "不限")
    ]

    rec_data = filtered.head(3) if not filtered.empty else school_data.sample(3)

    rec_data = rec_data.rename(columns={
        "学校": "推荐学校",
        "导师": "推荐导师",
        "推荐建议": "匹配建议"
    })

    st.dataframe(rec_data, use_container_width=True)

    st.markdown("### ✉️ AI生成自荐信建议")
    ai_letter = f"""
尊敬的导师：

您好！我是{name}，本科专业为{edu_bg}，GPA为{gpa}。我长期关注{interest_field}方向的发展，在课程学习和项目中积累了基础。希望能在研究生阶段继续深入探索该领域，特别是在实践工程中结合建筑节能与智能控制策略。若能加入您的课题组，我将积极投入科研，贡献力量。

期待有机会与您进一步交流！

此致  
敬礼！
"""
    st.text_area("自荐信草稿（可修改）", ai_letter.strip(), height=240)

    st.markdown("🔍 建议：建议在信中补充项目/实习经历，强调你在该方向的实践基础。")

else:
    st.info("请在左侧填写信息后点击“获取推荐”")
