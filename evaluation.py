from math import log2


def Density(G, communities):
    cnt = 0
    for community in communities:
        H = G.subgraph(community)
        cnt += H.number_of_edges()
    return cnt / G.number_of_edges()


def Entropy(G, communities, lexicons):
    ans = 0
    num = G.number_of_nodes()
    Hs = []
    for community in communities:
        H = G.subgraph(community)
        Hs.append(H)
    for index, lexicon in enumerate(lexicons):
        for H in Hs:
            ans += H.number_of_nodes() / num * entropy(lexicon, H)
        if index % 100 == 0:
            print(f'Entropy: {index}/{len(lexicons)}')
    return ans


def entropy(lexicon, H):
    cnt = 0
    for node in H.nodes():
        if lexicon in H.nodes[node]['description']:
            cnt += 1
    p = cnt / H.number_of_nodes()
    if p == 0:
        return 0
    return -p * log2(p)
