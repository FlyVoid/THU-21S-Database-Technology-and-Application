import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#文件路径
cs2016spring=r'D:\线上课程学习数据分析\计算机文化基础2016\2016春\学生数据\course-v1_TsinghuaX+20740042X+2016_T1_video.csv'
cs2016autumn=r'D:\线上课程学习数据分析\计算机文化基础2016\2016秋\学生数据\course-v1_TsinghuaX+20740042X+2016-T2_video.csv'
cs2016summer=r'D:\线上课程学习数据分析\计算机文化基础2016\2016暑期\学生数据\course-v1_TsinghuaX+20740042X+2016_TS_video.csv'
art2016spring=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016春\学生数据\course-v1_TsinghuaX+00670122X+2016_T1_video.xlsx'
art2016autumn=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016秋\学生数据\course-v1_TsinghuaX+00670122X+2016_T2_video.xlsx'
art2016summer=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016暑期\学生数据\course-v1_TsinghuaX+00670122X+2016_TS_video.xlsx'


def main():
    global result

    # 计算观看率
    def watchrate(path, drop=True):
        try:
            data = pd.read_csv(path)
        except:
            data = pd.read_excel(path)
        data = data.iloc[:, 5:]
        data = data.applymap(lambda x: float(x.split('.')[0]) / 100)
        if not drop:
            return data.mean(axis=1).mean()
        result = data.mean(axis=1)
        return result[result > 0.05].mean()

    # cs专业去掉小于5%观看率
    cs_spring_drop = watchrate(cs2016spring)
    cs_summary_drop = watchrate(cs2016summer)
    cs_autumn_drop = watchrate(cs2016autumn)
    # cs专业观看率
    cs_spring = watchrate(cs2016spring, False)
    cs_summary = watchrate(cs2016summer, False)
    cs_autumn = watchrate(cs2016autumn, False)
    # 生活美学专业去掉小于5%观看率
    art_spring_drop = watchrate(art2016spring)
    art_summer_drop = watchrate(art2016summer)
    art_autumn_drop = watchrate(art2016autumn)
    # 生活美学专业观看率
    art_spring = watchrate(art2016spring, False)
    art_summer = watchrate(art2016summer, False)
    art_autumn = watchrate(art2016autumn, False)
    # 构建空dataframe
    result = pd.DataFrame()
    # 对应的数据填进去
    result['cs_drop'] = [cs_spring_drop, cs_summary_drop, cs_autumn_drop]
    result['cs'] = [cs_spring, cs_summary, cs_autumn]
    result['art_drop'] = [art_spring_drop, art_summer_drop, art_autumn_drop]
    result['art'] = [art_spring, art_summer, art_autumn]
    # x轴
    result.index = ['2016春', '2016夏', '2016秋']
    result.plot(title='平均观看率')
    plt.savefig('lineplot.png')
    plt.show()

if __name__=='__main__':
    main()