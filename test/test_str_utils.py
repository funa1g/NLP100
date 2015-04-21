# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import eq_, ok_
from work.str_utils import reverse_string, get_odd_string, connect_string_alternately, split_sentence_to_words, count_words_length

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


    def test_count_words_length(self):
        # 正常系
        eq_(count_words_length([u'Get', u'Back']), [3, 4])
