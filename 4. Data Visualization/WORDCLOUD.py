import jieba
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#文件路径
cs2016srping=r'D:\线上课程学习数据分析\计算机文化基础2016\2016春\学生行为\course-v1_TsinghuaX+20740042X+2016_T1-comments_info.xlsx'
cs2016summer=r'D:\线上课程学习数据分析\计算机文化基础2016\2016暑期\学生行为\course-v1_TsinghuaX+20740042X+2016_TS-comments_info.xlsx'
cs2012autumn=r'D:\线上课程学习数据分析\计算机文化基础2016\2016秋\学生行为\course-v1_TsinghuaX+20740042X+2016-T2-comments_info.xlsx'
art2016spring=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016春\学生行为\course-v1_TsinghuaX+00670122X+2016_T1-comments_info.xlsx'
art2016summer=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016暑期\学生行为\course-v1_TsinghuaX+00670122X+2016_TS-comments_info.xlsx'
art2016autumn=r'D:\线上课程学习数据分析\现代生活美学2016\现代生活美学2016秋\学生行为\course-v1_TsinghuaX+00670122X+2016-T2-comments_info.xlsx'


def main():
    global remove_stop_words, gen

    def remove_stop_words(x):  # 移除停用词
        # 设置停用词
        with open('stop_words.txt', encoding='utf-8')as f:  # 读取stop_words里面的停用词列表
            stop_words = [line.strip() for line in f.readlines()]
        for word in stop_words:
            while word in x:
                x.remove(word)
                if not word:
                    break
        return x

    def gen(series):  # 将每一条评论合并成一个列表
        sequence = []
        for s in series:
            sequence.extend(s)
        return sequence

    def plot(path, title):
        data = pd.read_excel(path)  # 读取数据
        comments = data.内容.map(lambda x: jieba.lcut(x, cut_all=False))  # 分词
        comments = comments.map(lambda x: remove_stop_words(x))  # 移除停用词
        g = gen(comments)  # 评论合并成一个列表
        text = ','.join(g)  # 列表合并，按逗号隔开
        # 词云图 背景 宽 高 边缘距离 字体
        wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2,
                              font_path='C:/Windows/Fonts/simkai.ttf').generate(text)
        # 画布显示
        plt.figure(figsize=[7, 7])
        plt.title(f'{title}')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig(f'{title}.png')
        plt.show()

    plot(cs2016srping, 'cs2016srping')
    plot(cs2016summer, 'cs2016summer')
    plot(cs2012autumn, 'cs2012autumn')
    plot(art2016spring, 'art2016spring')
    plot(art2016summer, 'art2016summer')
    plot(art2016autumn, 'art2016autumn')


if __name__=='__main__':
    main()
