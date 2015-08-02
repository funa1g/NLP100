# -*- coding: utf-8 -*-

from sets import Set

class MeCabReader:

    def __init__(self):
        self.__morphs = []
        self.__sentence_pos = []
        self.__paragraph_pos = []

    def _read(self, path):
        f = open(path, 'r')
        sstart_pos = 0
        send_pos = 0
        pstart_pos = 0
        pend_pos = 0
        prePeriod = False
        for i, line in enumerate(f):
            # 各形態素をリストとして保存
            morph = Morphology(line)
            self.__morphs.append(morph)
            # 文の位置を計算
            if morph.isEOS():
                if not prePeriod:
                    send_pos = i - 1
                    prePeriod = True
            elif morph.isPeriod():
                send_pos = i
                prePeriod = True
            elif morph.isSpace():
                pass
            elif prePeriod:
                self.__sentence_pos.append((sstart_pos, send_pos))
                sstart_pos = i
                prePeriod = False
        if sstart_pos != 0 and send_pos != 0:
            self.__sentence_pos.append((sstart_pos, send_pos))                

    def get_paragraph_count(self):
        return len(self.__paragraph_pos)

    def get_sentence_count(self):
        return len(self.__sentence_pos)

    def sentence_pos(self, index):
        u"""
        文の品詞の出現順に並んだリストを返す
        @param index 取得する文
        """
        pos_list = []
        start_pos, end_pos = self.__sentence_pos[index]
        for i in range(start_pos, end_pos + 1):
            pos_list.append(self.__morphs[i].pos)
        return pos_list

    def surfaces_set(self, pos, pos1=None):
        u"""
        読み込んだ文書全体の表層形のSetを返す
        @param pos 品詞
        @param pos1 品詞細分類
        """
        surfaces = Set()
        for morph in self.__morphs:
            if not self.__is_invalid_morph(morph, pos, pos1):
                surfaces.add(morph.surface)
        return surfaces

    def bases_set(self, pos, pos1=None):
        u"""
        読み込んだ文書全体の原形のSetを返す
        @param pos 品詞
        @param pos1 品詞細分類
        """
        surfaces = Set()
        for morph in self.__morphs:
            if not self.__is_invalid_morph(morph, pos, pos1):
                surfaces.add(morph.base)
        return surfaces

    def __is_invalid_morph(self, morph, pos, pos1):
        if morph.isEOS():
            return True
        if pos != None and morph.pos != pos:
            return True
        if pos1 != None and morph.pos1 != pos1:
            return True
        return False

    def no_connect_words(self):
        connect_words = Set()
        temp_morphs = []
        for morph in self.__morphs:
            if morph.isEOS():
                del temp_morphs[0 : len(temp_morphs)]
                continue
            temp_morphs.append(morph)
            if len(temp_morphs) == 3:
                if temp_morphs[0].pos == "名詞" and temp_morphs[1].surface == "の" and temp_morphs[2].pos == "名詞":
                    connect_words.add("".join([morph.surface for morph in temp_morphs]))
                temp_morphs.pop(0)
        return connect_words

    def connect_words(self):
        connect_words = Set()
        temp_words = []
        for morph in self.__morphs:
            if morph.isEOS():
                self.__append_temp_word(temp_words, connect_words)
            elif morph.pos == "名詞":
                temp_words.append(morph.surface)
            else:
                self.__append_temp_word(temp_words, connect_words)
        return connect_words

    def __append_temp_word(self, temp_words, connect_words):
        if len(temp_words) > 1:
            connect_words.add("".join(temp_words))
        del temp_words[0 : len(temp_words)]

    def hist_list(self, threshold=0):
        u"""
        各単語の原形と出現回数の組のリストを返す
        @param threshold 上位何件を取得するかを指定する
        """
        hist_map = {}
        for morph in self.__morphs:
            if morph.isEOS():
                continue
            if morph.base in hist_map:
                hist_map[morph.base] += 1
            else:
                hist_map[morph.base] = 1
        hist_list = []
        for word in sorted(hist_map, key=hist_map.__getitem__, reverse=True):
            if threshold != 0 and len(hist_list) >= threshold:
                break
            hist_list.append((word, hist_map[word]))
        return hist_list


class Morphology:

    def __init__(self, line):
        word = line.split("\t")
        self.surface = word[0].strip()
        if len(word) > 1:
            parts = word[1].split(",")
            self.base = parts[6].strip()
            self.pos = parts[0]
            self.pos1 = parts[1]

    def __eq__(self, other):
        u"""
        原形と品詞、品詞細分類が同一であれば、同一の語とみなす
        """
        return self.base == other.base and self.pos == other.pos and self.pos1 == other.pos1

    def isEOS(self):
        u"""
        この形態素が文末を示すものであるかを返す
        日本語の場合は、文末より段落末と解釈するのが妥当なので注意
        """
        return self.surface == "EOS"

    def isPeriod(self):
        u"""
        この形態素が文末を示す語句であるかを返す
        現在は、「。」！？」を対象としている。
        """
        return self.surface in ["。", "」", "！", "？"]

    def isSpace(self):
        u"""
        この形態素が空白を示すかを返す
        """
        return self.pos1 == "空白"


def reader(path):
    mb = MeCabReader()
    mb._read(path)
    return mb

if __name__ == '__main__':
    mb = reader("../../resource/neko.txt.mecab")
    sentence_count = mb.get_sentence_count()
    pos_set = Set()
    for i in range(sentence_count):
        pos_set.add(",".join(mb.sentence_pos(i)))
    print len(pos_set), sentence_count
    # for pos in pos_set:
        # print pos

    """
    print mb.get_paragraph_count()
    print mb.get_sentence_count()
    surfaces = mb.surfaces_set("名詞")
    print len(surfaces)
    surfaces = mb.surfaces_set("名詞", "サ変接続")
    print len(surfaces)
    bases = mb.bases_set("名詞", "サ変接続")
    print len(bases)
    hist_list = mb.hist_list()
    f = open("neko.txt.hist", "w")
    for word in hist_list:
        f.write(word[0] + "\t" + str(word[1]) + "\n")
    connect_words = mb.no_connect_words()
    #for word in connect_words:
    #    print word
    #for base in bases:
    #    print base
    """
