# -*- coding: utf-8 -*-


class Config(object):
    dic_dir = 'keyword_generator/kw_generator/dic/'
    raw_dic_dir = 'raw_dic/'
    root_dir = '.'

    # Threshold set for keywords filter
    kw_threshold = {
        'brand': 11,
        'category': 12,
        'color': 7,
        'country': 3,
        'currency': 1,
        'group': 10,
        'material': 9,
        'scene': 5,
        'ship': 4,
        'size': 6,
        'style': 8,
        'other': 2
    }

    # number of titles
    num_titles = 1
