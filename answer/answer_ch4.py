# -*- coding: utf-8 -*- 

from nlp100.wrapper import mecab

u"""
NLP100本ノック2015 Chapter4 の解答を作成し、実行する
"""

class Chapter4:

    def __init__(self, path):
        # answer_q30
        self.reader = mecab.reader(path)

    def q31(self):
        return self.reader.make_surfaces_set("動詞")

    def q32(self):
        return self.reader.make_bases_set("動詞")

    def q33(self):
        return self.reader.make_bases_set("名詞", "サ変接続")

    def q34(self):
        return self.reader.make_no_connect_words()

    def q35(self):
        return self.reader.make_connect_words()

    def q36(self):
        return self.reader.make_hist_list()

    def q37(self):
        return self.reader.make_hist_list(10)

if __name__ == '__main__':
    answer = Chapter4('resource/neko.txt.mecab')
    # 全件表示すると非常に大きくなるので、先頭５項目のみ表示
    print 'answer_q31\n' + ",".join([word for i, word in enumerate(answer.q31()) if i < 6]) + '\n'
    print 'answer_q32\n' + ",".join([word for i, word in enumerate(answer.q32()) if i < 6]) + '\n'
    print 'answer_q33\n' + ",".join([word for i, word in enumerate(answer.q33()) if i < 6]) + '\n'
    print 'answer_q34\n' + ",".join([word for i, word in enumerate(answer.q34()) if i < 6]) + '\n'
    print 'answer_q35\n' + ",".join([word for i, word in enumerate(answer.q35()) if i < 6]) + '\n'
    print 'answer_q36'
    answer_q36 = answer.q36()
    q36_str = ""
    for i in range(5):
        tuple = answer_q36.pop()
        q36_str += "(" + tuple[0] + ":" + str(tuple[1]) + "),"
    print q36_str
    print 'answer_q36'
    answer_q37 = answer.q37()
    q37_str = ""
    for tuple in answer_q37:
        q37_str += "(" + tuple[0] + ":" + str(tuple[1]) + "),"
    print q37_str
