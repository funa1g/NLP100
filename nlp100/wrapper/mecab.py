# -*- coding: utf-8 -*-

class MeCabReader:

    def __init__(self, path):
        self.paragraphs = []
        f = open(path, 'r')

        paragraph = Paragraph()
        sentence = Sentence()
        preEOS = False
        for line in f:
            morph = Morphology(line)
            if morph.isEOS():
                if preEOS:
                    self.paragraphs.append(paragraph)
                    paragraph = Paragraph()
                else:
                    paragraph.append(sentence)
                    sentence = Sentence()
                preEOS = True
            else:
                sentence.append(morph)
                preEOS = False
        self.paragraphs.append(paragraph)

    def getParagraphCount(self):
        return len(self.paragraphs)

    def countSentences(self):
        count = 0
        for paragraph in self.paragraphs:
            count += len(paragraph)
        return count

    def makeParagraphSurface(self, i):
        return self.paragraphs[i].makeSurface()

    def getSurfaces(self, pos, pos1=None):
        result = []
        for paragraph in self.paragraphs:
            result.extend(paragraph.getSurfaces(pos, pos1))
        return result

    def getBases(self, pos, pos1=None):
        result = []
        for paragraph in self.paragraphs:
            result.extend(paragraph.getBases(pos, pos1))
        return result


class Paragraph(list):
    
    def makeSurface(self):
        surface = ""
        for sentence in self:
            surface += sentence.makeSurface()
        return surface

    def getSurfaces(self, pos, pos1=None):
        surfaces = []
        for sentence in self:
            surfaces.extend(sentence.getSurfaces(pos, pos1))
        return surfaces

    def getBases(self, pos, pos1=None):
        bases = []
        for sentence in self:
            bases.extend(sentence.getBases(pos, pos1))
        return bases

class Sentence(list):

    def __init__(self):
        self._is_narrative = False

    def makeSurface(self):
        surface = ""
        for morph in self:
            surface += morph.surface
        return surface

    def getSurfaces(self, pos, pos1=None):
        return [morph.surface for morph in self if morph.pos == pos and (pos1 == None or morph.pos1 == pos1)]

    def getBases(self, pos, pos1=None):
        return [morph.base for morph in self if morph.pos == pos and (pos1 == None or morph.pos1 == pos1)]

class Morphology:

    def __init__(self, line):
        word = line.split("\t")
        self.surface = word[0].strip()
        if len(word) > 1:
            parts = word[1].split(",")
            self.base = parts[6].strip()
            self.pos = parts[0]
            self.pos1 = parts[1]

    def isEOS(self):
        u"""
        この形態素が文末を示すものであるかを返す
        日本語の場合は、文末より段落末と解釈するのが妥当なので注意
        """
        return self.surface == "EOS"

    def isPeriod(self):
        u"""
        この形態素が文末を示す語句であるかを返す
        現在は、「。」」を対象としている。
        """
        return self.surface in ["。", "」"]



if __name__ == '__main__':
    mb = MeCabReader("../../resource/neko.txt.mecab")
    print mb.getParagraphCount()
    print mb.countSentences()
    bases = mb.getBases("名詞", "サ変接続")
    print len(bases)
    for base in bases:
        print base
