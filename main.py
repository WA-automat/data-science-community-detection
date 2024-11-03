import matplotlib.pyplot as plt
import pandas as pd
from load_data import *
import networkx as nx
from evaluation import Density, Entropy
from graspologic.partition import hierarchical_leiden

if __name__ == '__main__':
    print('----------加载数据----------')
    G = build_graph()
    lexicons = load_lexicon()
    print('加载完毕！')

    # print('----------图像绘制----------')
    # nx.draw(G, with_labels=False)
    # plt.show()

    print('----------社区发现----------')
    # communities = nx.community.kernighan_lin_bisection(G)

    # communities = nx.community.label_propagation_communities(G)

    communities = nx.community.louvain_communities(G)

    # communities = hierarchical_leiden(
    #     graph=G
    # )
    # final_groups = {}
    # for cluster in communities:
    #     if cluster.level == 0:
    #         if cluster.cluster not in final_groups:
    #             final_groups[cluster.cluster] = []
    #         final_groups[cluster.cluster].append(cluster.node)
    # communities = []
    # for group_num, members in final_groups.items():
    #     communities.append(set(members))
    # for i in range(1, 16008):
    #     flag = False
    #     for community in communities:
    #         if i in community:
    #             flag = True
    #             break
    #     if not flag:
    #         communities.append({i})

    sorted_communities = sorted(communities, key=lambda x: -len(x))
    word_dict = {}
    for i in sorted_communities[0]:
        with open(attributes_path + str(i) + '.txt', 'r', encoding='utf-8') as f:
            description = f.read().replace('\n', ',')
            words = description.split(',')
            for word in words:
                if word not in word_dict.keys():
                    word_dict[word] = 0
                word_dict[word] += 1
    sort_keys = sorted(word_dict, key=lambda k: -word_dict[k])
    word_data = []
    for key in sort_keys[:100]:
        word_data.append([key, word_dict[key]])
    print(word_data)
    df = pd.DataFrame(word_data)
    df.to_csv('word_fre_community.csv', index=False, header=False, encoding='utf-8')

    # for index, community in enumerate(sorted_communities[:10]):
    #     H = G.subgraph(community)
    #     mx = 0
    #     idx = 0
    #     for i in community:
    #         if H.degree(i) >= mx:
    #             mx = H.degree(i)
    #             idx = i
    #     with open(attributes_path + str(idx) + '.txt', 'r', encoding='utf-8') as f:
    #         description = f.read().replace('\n', ',')
    #         print(index + 1, len(community), idx, description, mx, sep=' & ', end='\\\\\n')

    # print(len(communities))
    # result = []
    # for i in range(1, 16008):
    #     for j, community in enumerate(communities):
    #         if i in community:
    #             result.append([i, j])
    #             break
    # df = pd.DataFrame(result, columns=['id', 'community'])
    # df.to_csv('leiden.csv', index=False)

    print('----------结果检验----------')
    print(f'Density: {Density(G, communities)}')
    print(f'Modularity: {nx.algorithms.community.quality.modularity(G, communities)}')
    print(f'Entropy: {Entropy(G, communities, lexicons)}')
