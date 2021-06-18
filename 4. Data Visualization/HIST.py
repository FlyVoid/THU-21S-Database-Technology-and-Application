import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#文件路径
cs2016spring=r'D:\线上课程学习数据分析\计算机文化基础2016\2016春\成绩评价'
cs2016autumn=r'D:\线上课程学习数据分析\计算机文化基础2016\2016秋\成绩评价'
cs2016summer=r'D:\线上课程学习数据分析\计算机文化基础2016\2016暑期\成绩评价'
art2016spring=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016春\成绩评价'
art2016autumn=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016秋\成绩评价'
art2016summer=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016暑期\成绩评价'


def main():
    # 文件标题
    titles = ['csspring', 'cssummer', 'csautumn', 'artspring', 'artsummer', 'artautumn']
    # 路径添加到列表
    path = [cs2016spring, cs2016summer, cs2016autumn, art2016spring, art2016summer, art2016autumn]
    # 新建2行3列子6个图 共享xy轴
    fig, ax = plt.subplots(2, 3, figsize=[9, 6], sharex=True, sharey=True)
    # 绘图
    for idx, ax in enumerate(ax.flat):
        filepath = glob.glob(path[idx] + '\*.xlsx')
        data = pd.read_excel(filepath[0])
        data = data[data.总得分 > 0]
        sns.histplot(x='总得分', data=data, bins=10, ax=ax)
        ax.set_title(titles[idx])
    plt.tight_layout()
    plt.savefig('histplot.png')
    plt.show()

if __name__=='__main__':
    main()

