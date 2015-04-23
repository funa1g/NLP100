# -*- coding: utf-8 -*-

from work.str_utils import reverse_string, get_odd_string, connect_string_alternately, split_sentence_to_words, count_words_length, make_char_ngram, make_word_ngram, make_time_sentence, cipher, make_typoglycemia

u"""
NLP100本ノック 2015 Chapter1 の解答を作成し、実行する
"""

def answer_q00():
    problem_str = u'stressed'
    return reverse_string(problem_str)


def answer_q01():
    problem_str = u'パタトクカシーー'
    return get_odd_string(problem_str)
    

def answer_q02():
    problem_str1 = u"パトカー"
    problem_str2 = u"タクシー"
    return connect_string_alternately(problem_str1, problem_str2)


def answer_q03():
    problem_sentence = u'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    words = split_sentence_to_words(problem_sentence)
    return count_words_length(words)


def answer_q04():
    problem_sentence = u'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    words = split_sentence_to_words(problem_sentence)
    first_char_word_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    element_dict = {}
    for i, word in enumerate(words):
        if i in first_char_word_index:
            element_word = word[0]
        else:
            element_word = word[0:2]
        element_dict[i] = element_word
    return element_dict


def answer_q05():
    problem_sentence = u'I am an NLPer'
    answer_word_bigram = u'単語bi-gram:' + str(make_word_ngram(2, problem_sentence)) + '\n'
    answer_char_bigram = u'文字bi-gram:' + str(make_char_ngram(2, problem_sentence))
    return answer_word_bigram + answer_char_bigram


def answer_q06():
    problem_word1 = u'paraparaparadise'
    problem_word2 = u'paragraph'
    problem_word3 = u'se'
    word1_char_bigram = make_char_ngram(2, problem_word1)
    word2_char_bigram = make_char_ngram(2, problem_word2)
    x = set(word1_char_bigram)
    y = set(word2_char_bigram)
    answer_str  = '\n'
    answer_str += u'和集合:' + str(x.union(y)) + '\n'
    answer_str += u'積集合:' + str(x.intersection(y)) + '\n'
    answer_str += u'差集合(X):' + str(x.difference(y)) + '\n'
    answer_str += u'差集合(Y):' + str(y.difference(x)) + '\n'
    answer_str += problem_word3 + u'を含んでいるかどうか(X):' + str(problem_word3 in x) + '\n'
    answer_str += problem_word3 + u'を含んでいるかどうか(Y):' + str(problem_word3 in y) + '\n'
    return answer_str


def answer_q07():
    return make_time_sentence(12, u'気温', 22.4)


def answer_q08():
    original_str = "supercalifragilisticexpialidocious"
    encrypt_str = cipher(original_str)
    decrypt_str = cipher(encrypt_str)
    answer_str  = '\n'
    answer_str += u'暗号化前:' + original_str + '\n'
    answer_str += u'暗号化後:' + encrypt_str + '\n'
    answer_str += u'復号化後:' + decrypt_str + '\n'
    return answer_str


def answer_q09():
    problem_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = split_sentence_to_words(problem_sentence)
    typo_words = []
    for word in words:
        typo_words.append(make_typoglycemia(word))
    return u' '.join(typo_words)

    
if __name__ == '__main__':
    answer_string = ''
    answer_string += 'answer_q00: ' + answer_q00() + '\n\n'
    answer_string += 'answer_q01: ' + answer_q01() + '\n\n'
    answer_string += 'answer_q02: ' + answer_q02() + '\n\n'
    answer_string += 'answer_q03: ' + str(answer_q03()) + '\n\n'
    answer_string += 'answer_q04: ' + str(answer_q04()) + '\n\n'
    answer_string += 'answer_q05: ' + answer_q05() + '\n\n'
    answer_string += 'answer_q06: ' + answer_q06() + '\n\n'
    answer_string += 'answer_q07: ' + answer_q07() + '\n\n'
    answer_string += 'answer_q08: ' + answer_q08() + '\n\n'
    answer_string += 'answer_q09: ' + answer_q09() + '\n\n'
    print answer_string
