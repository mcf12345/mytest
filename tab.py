import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它
#页面配置
st.set_page_config(
    page_title="王鹤棣 - 个人数字档案",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 标题
st.title("🌟 王鹤棣 - 个人数字档案")

# 基础信息 + 头像 平行布局（分两列，与基础信息平行）
col_info, col_avatar = st.columns([2, 1])  # 左侧信息区宽，右侧头像区适配
with col_info:
    # 基础信息（基于真实资料整理）
    st.header("📝 基础信息")
    st.text("姓名：王鹤棣")
    st.text("昵称：棣棣")
    st.text("出生日期：1998年12月20日（射手座）")
    st.text("出生地：四川省乐山市")
    st.text("毕业院校：西南航空专修学院")
    st.text("职业：中国内地影视男演员")
    st.text("出道节点：2017年《超次元偶像》总冠军")
    st.text("核心标签：演员 | 篮球爱好者 | 综艺嘉宾")
    st.text("当前状态：活跃 🟢")

with col_avatar:
    # 加载用户提供的王鹤棣头像地址
    avatar_url = "https://tse4-mm.cn.bing.net/th/id/OIP-C.4DBUPkZSkPjaLfvV1pqNWAAAAA?w=204&h=327&c=7&r=0&o=7&pid=1.7&rm=3"
    st.image(avatar_url, width=180)  # 适配布局的头像宽度

# 核心能力矩阵（贴合王鹤棣职业特点）
st.header("📊 核心能力矩阵")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="影视演技", value="90%", delta="↑5%")  # 《苍兰诀》后口碑提升
with col2:
    st.metric(label="综艺表现力", value="85%", delta="↑2%")  # 多综艺常驻表现亮眼
with col3:
    st.metric(label="篮球技能", value="88%", delta="→0%")  # 连续入选NBA名人赛，水平稳定

# 近期任务日志（参考真实活动+合理虚构）
st.header("📅 近期任务日志")
task_data = {
    "日期": ["2025-02-15", "2025-05-20", "2025-08-10"],
    "任务名称": ["NBA旧金山全明星名人赛", "电视剧《星河入梦》宣传", "综艺《我们的宿舍》录制"],
    "状态": ["🟢 已完成", "🟡 进行中", "🔴 待启动"],
    "难度评级": ["★★★★★", "★★★☆☆", "★★★★☆"]
}
task_df = pd.DataFrame(task_data)
st.table(task_df)

# 代表作品与成就（替换原歌词，贴合演员身份）
st.header("🏆 代表作品与关键成就")
work_achievement = """
# 代表作品（影视/综艺）
1. 电视剧：《苍兰诀》（饰 东方青苍）、《流星花园》（饰 道明寺）、《浮图缘》（饰 肖铎）、《大奉打更人》（饰 许七安）
2. 电影：《抬头见喜》（饰 郭文翰）
3. 综艺：《超次元偶像》（总冠军）、《五十公里桃花坞》系列、《你好星期六》（常驻）

# 关键成就
1. 2019年：2018-2019中国文娱金数据盛典 年度电视剧综合影响力新人奖
2. 2022年：入选2022星辰大海青年演员优选计划（优秀学员）
3. 2023年：第9届横店影视文荣奖 最佳青年剧集男演员（《苍兰诀》）
4. 2023年：2022微博之夜 微博年度瞩目演员
5. 2024-2025年：连续两年入选NBA全明星周末名人赛名单
"""
st.code(work_achievement, language="plaintext")

# 系统消息（适配人物场景）
st.markdown("---")
st.markdown("🖥️ 系统提示：电视剧《星河入梦》最新片花已同步至云端")
st.markdown("⏰ 数据更新时间：2025-12-18 17:30:00")
st.markdown("当前状态：在线 | 数据已备份")
