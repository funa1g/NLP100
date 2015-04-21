# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import eq_, ok_
from work.str_utils import reverse_string

class StrUtilTestCase(TestCase):

    def test_reverse_string(self):
        u"""
        str_util.reverse_string メソッドのテストです
        """
        # 正常系
        eq_(reverse_string('reverse'), 'esrever')
        eq_(reverse_string(u'reverse'), u'esrever')
        eq_(reverse_string(u'あいう'), u'ういあ')

        # 異常系
        ok_(reverse_string('あいう') != 'ういあ')
        ok_(reverse_string(u'𠮟る') != u'る𠮟')


