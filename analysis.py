import matplotlib.pyplot as plt
import pandas as pd

from load_data import *

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    # print('----------加载数据----------')
    # G = build_graph()
    # lexicons = load_lexicon()
    # print('加载完毕！')

    df = pd.read_csv('word_fre_community.csv', header=None)

    fig = plt.figure(figsize=(13, 6))
    plt.bar(x=df[0], height=df[1], color='#c0dcf0')
    # 去掉上边框和有边框
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    for tick in plt.gca().get_yticklabels():
        plt.axhline(y=tick.get_position()[1], color='#b8bcbf', linestyle='--', linewidth=1, zorder=-1)
    plt.xlabel('关键词')
    plt.ylabel('出现频次')
    plt.tight_layout()
    for x, y in enumerate(df[1].tolist()):
        plt.text(x, y + 20, "%s" % round(y, 1), ha='center')  # round(y,1)是将y值四舍五入到一个小数位
    plt.show()
    print(df)

    # d = [0] * 16007
    # with open(link_path, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         numbers = [int(num) for num in re.findall(r'\d+', line)]
    #         d[numbers[0]] += 1
    #         d[numbers[1]] += 1
    # d = dict(zip(list(range(1, 16008)), d))
    # sort_keys = sorted(d, key=lambda k: -d[k])
    #
    # for key in sort_keys[:10]:
    #     with open(attributes_path + str(key) + '.txt', 'r', encoding='utf-8') as f:
    #         description = f.read().replace('\n', ',')
    # G.add_node(key, description=set(description.split(',')))
    # print(key, description, d[key], sep=' & ')

    # word_dict = {}
    # for i in range(1, 16008):
    #     with open(attributes_path + str(i) + '.txt', 'r', encoding='utf-8') as f:
    #         description = f.read().replace('\n', ',')
    #         words = description.split(',')
    #         for word in words:
    #             if word not in word_dict.keys():
    #                 word_dict[word] = 0
    #             word_dict[word] += 1
    # sort_keys = sorted(word_dict, key=lambda k: -word_dict[k])
    # word_data = []
    # for key in sort_keys[:100]:
    #     word_data.append([key, word_dict[key]])
    # print(word_data)
    # df = pd.DataFrame(word_data)
    # df.to_csv('word_fre.csv', index=False, header=False, encoding='utf-8')
    # print(d)

    # linkstxt2csv()
