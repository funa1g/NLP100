# -*- coding: utf-8 -*-

from work.str_utils import reverse_string

u"""
NLP100本ノック 2015 Chapter1 の解答を作成し、実行する
"""

def answer_q00():
    problem_string = u'stressed'
    return reverse_string(problem_string)


if __name__ == '__main__':
    answer_string = ''
    answer_string += 'answer_q00: ' + answer_q00()
    print answer_string
