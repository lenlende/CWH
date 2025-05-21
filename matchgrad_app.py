import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="MatchGrad智能读研推荐平台", layout="wide")

# 页面标题
st.title("🎓 MatchGrad：AI智能读研与导师匹配平台")
st.markdown("为考研学生提供个性化学校、专业、导师推荐和自荐材料生成")

# --- 左栏：考生信息输入 ---
st.sidebar.header("📝 填写你的考生信息")
name = st.sidebar.text_input("姓名")
edu_bg = st.sidebar.selectbox("本科专业", ["建筑环境与能源应用工程", "给排水科学与工程", "土木工程", "其他"])
gpa = st.sidebar.slider("本科成绩绩点 (GPA)", 2.0, 4.5, 3.2, 0.1)
location_pref = st.sidebar.multiselect("意向地区", ["北京", "上海", "西安", "成都", "不限"])
interest_field = st.sidebar.selectbox("科研兴趣方向", ["绿色建筑", "建筑节能", "暖通系统仿真", "碳中和/碳达峰", "智能控制"])

if st.sidebar.button("🔍 获取推荐"):
    st.subheader(f"👤 推荐结果为：{name}")

    # 模拟推荐数据
    rec_data = pd.DataFrame({
        "学校": ["同济大学", "西安建筑科技大学", "重庆大学"],
        "专业": ["建筑环境与能源应用工程"] * 3,
        "匹配度": [random.randint(85, 98) for _ in range(3)],
        "推荐导师": ["张教授", "李教授", "王教授"],
        "研究方向": [interest_field] * 3
    })

    st.dataframe(rec_data, use_container_width=True)

    st.markdown("---")
    st.markdown("### ✉️ AI自荐信生成")
    auto_letter = f"尊敬的导师：\n\n您好！我叫{name}，本科专业为{edu_bg}，GPA为{gpa}，对{interest_field}方向具有浓厚兴趣……希望能加入您的研究团队……"
    st.text_area("自荐信草稿", auto_letter, height=200)

    st.markdown("---")
    st.markdown("### 🎥 视频脚本参考")
    st.markdown(f"""
    > 大家好，我是{name}，本科期间主修{edu_bg}，GPA为{gpa}。我热衷于{interest_field}方向，未来希望在贵校继续深造，并参与科研项目实现自我成长。谢谢！
    """)
else:
    st.info("请在左侧输入考生信息并点击“获取推荐”")