import pandas as pd
import numpy as np
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
    global result
    # 添加到列表
    cspath = [cs2016spring, cs2016summer, cs2016autumn]
    artpath = [art2016spring, art2016summer, art2016autumn]

    # 得分计算函数
    def calculate(path, drop=True):
        scores = []
        for p in path:
            filepath = glob.glob(p + '\*.xlsx')
            data = pd.read_excel(filepath[0])
            if drop:
                data = data[data.总得分 > 0]
            scores.append(data.总得分.mean())
        return scores

    result = pd.DataFrame()  # 新建空表格
    result['csdrop'] = calculate(cspath)  # cs专业去掉零分的
    result['cs'] = calculate(cspath, drop=False)  # cs专业不去掉零分的
    result['artdrop'] = calculate(artpath)  # 生活美学去掉零分的
    result['art'] = calculate(artpath, drop=False)  # 生活美学不去掉零分的
    result.index = ['2016春', '2016夏', '2016秋']  # x轴日期
    result.plot(title='平均分比较')  # 设置图标标题
    plt.savefig('lineplot.png')  # 保存
    plt.show()  # 显示


if __name__=='__main__':
    main()