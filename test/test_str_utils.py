# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import eq_, ok_
from work.str_utils import reverse_string, get_odd_string, connect_string_alternately, split_sentence_to_words, count_words_length, make_char_ngram, make_word_ngram, make_time_sentence

class StrUtilTestCase(TestCase):

    def test_reverse_string(self):
        # 正常系
        eq_(reverse_string('reverse'), 'esrever')
        eq_(reverse_string(u'reverse'), u'esrever')
        eq_(reverse_string(u'あいう'), u'ういあ')

        # 異常系
        ok_(reverse_string('あいう') != 'ういあ')
        ok_(reverse_string(u'𠮟る') != u'る𠮟')

        
    def test_get_odd_string(self):
        # 正常系
        eq_(get_odd_string('rest'), 'rs')
        eq_(get_odd_string(u'takehiro'), u'tkhr')
        eq_(get_odd_string(u'デス博士の島その他の物語'), u'デ博のそ他物')
        # 異常系
        ok_(get_odd_string('あいう') != 'あう')
        ok_(get_odd_string(u'𠮟る') != u'𠮟')


    def test_connect_string_alternately(self):
        # 正常系
        eq_(connect_string_alternately('ace', 'bdf'), 'abcdef')
        eq_(connect_string_alternately(u'bta', u'amn'), u'batman')
        eq_(connect_string_alternately(u'柴勝', u'田家'), u'柴田勝家')
        # 異常系
        eq_(connect_string_alternately('abcd', 'ef'), '')
        ok_(connect_string_alternately('柴勝', '田家') != '柴田勝家')


    def test_split_sentence_to_words(self):
        # 正常系
        eq_(split_sentence_to_words(u'stand by me'), [u'stand', u'by', u'me'])
        eq_(split_sentence_to_words(u'You say "Yes", I say "No".'), [u'You', u'say', u'Yes', u'I', u'say', u'No'])

        # 異常系(未対応)
        ok_(split_sentence_to_words(u'Born in the U.S.A.') != [u'Born', u'in', u'the', u'U.S.A.'])


    def test_count_words_length(self):
        # 正常系
        eq_(count_words_length([u'Get', u'Back']), [3, 4])


    def test_make_char_ngram(self):
        # 正常系
        eq_(make_char_ngram(4, u'word'), [u'word'])
        eq_(make_char_ngram(2, u'bigram'), [u'bi', u'ig', u'gr', u'ra', u'am'])
        eq_(make_char_ngram(2, u'I\'m happy.'), [u'I\'', u'\'m', u'm ', u' h', u'ha', u'ap', u'pp', u'py', u'y.'])
        eq_(make_char_ngram(3, u'trigram'), [u'tri', u'rig', u'igr', u'gra', u'ram'])

        # 異常系
        eq_(make_char_ngram(2, u'a'), [])

    def test_make_word_ngram(self):
        # 正常系
        eq_(make_word_ngram(2, u'I\'m happy.'), [[u'I\'m', u'happy']])
        eq_(make_word_ngram(2, u'one two three four'), [[u'one', u'two'], [u'two', u'three'], [u'three', u'four']])
        eq_(make_word_ngram(3, u'one two three four'), [[u'one', u'two', u'three'], [u'two', u'three', u'four']])

        # 異常系
        eq_(make_word_ngram(2, u'bigram'), [])


    def test_make_time_sentence(self):
        # 正常系
        eq_(make_time_sentence(3, u'天気', u'晴れ'), u'3時の天気は晴れ')
        eq_(make_time_sentence(True, False, True), u'True時のFalseはTrue')
