



def net_classifier(data):
    info = ('TCP', 'UDP', 'RTP', 'MPLS')
    ls = data.split()
    for i in range(len(ls)):
        if ls[i] in info:
            ls[i] = 'CLASSIFIED'
    return ' '.join(ls)

