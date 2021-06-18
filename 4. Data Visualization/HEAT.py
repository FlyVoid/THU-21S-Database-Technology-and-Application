import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Calendar
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#文件路径
cs2016spring=r'D:\线上课程学习数据分析\计算机文化基础2016\2016春\学生行为\course-v1_TsinghuaX+20740042X+2016_T1-video_study_export.xlsx'
cs2016autumn=r'D:\线上课程学习数据分析\计算机文化基础2016\2016秋\学生行为\course-v1_TsinghuaX+20740042X+2016-T2-video_study_export.xlsx'
cs2016summer=r'D:\线上课程学习数据分析\计算机文化基础2016\2016暑期\学生行为\course-v1_TsinghuaX+20740042X+2016_TS-video_study_export.xlsx'
art2016spring=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016春\学生行为\course-v1_TsinghuaX+00670122X+2016_T1-video_study_export.xlsx'
art2016autumn=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016秋\学生行为\course-v1_TsinghuaX+00670122X+2016-T2-video_study_export.xlsx'
art2016summer=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016暑期\学生行为\course-v1_TsinghuaX+00670122X+2016_TS-video_study_export.xlsx'


def main():
    # 绘图函数
    def plot(path, name):  # path文件路径，name图标标题
        data = pd.read_excel(path)
        data['开始观看日期时间'] = pd.to_datetime(data['开始观看日期时间'])  # 开始观看日期转为时间列
        data = data.set_index('开始观看日期时间')  # 设置为索引
        data = data.resample('d')['学堂号'].count()  # 按天重新采样数据，对学堂号进行技术
        data = [[str(d)[:10], v] for d, v in zip(data.index, data)]  # 构建数据

        c = (
            Calendar()
                .add(
                "",
                data,
                calendar_opts=opts.CalendarOpts(
                    range_="2016",
                    daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
                    monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
                ),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}每日学习人数".format(name)),
                visualmap_opts=opts.VisualMapOpts(
                    max_=2000,
                    min_=1,
                    orient="horizontal",
                    is_piecewise=True,
                    pos_top="230px",
                    pos_left="100px",
                ),
            )
                .render(f"{name}heatmap.html")
        )

    # 绘图
    plot(cs2016spring, 'cs2016spring')
    plot(cs2016autumn, 'cs2016autumn')
    plot(cs2016summer, 'cs2016summer')
    plot(art2016spring, 'art2016spring')
    plot(art2016autumn, 'art2016autumn')
    plot(art2016summer, 'art2016summer')

if __name__=='__main__':
    main()