# -*- coding: utf-8 -*-

from work.tsv_reader import TsvReader
from work.subprocess_wrapper import SubprocessWrapper
import subprocess


class Chapter2Answer(object):

    def __init__(self):
        self.filename = 'resource/hightemp.txt'
        reader = TsvReader(self.filename, False)
        self.rows = reader.get_rows()
        self.sub_wrap = SubprocessWrapper()

    
    def answer_q10(self):
        rows_count = len(self.rows)
        wc_count = self.sub_wrap.wc_line_count(self.filename)
        answer_str  = u'行数:' + str(rows_count) + '\n'
        answer_str += u'wcと一致するか:' + str(wc_count == rows_count) + '\n'
        return answer_str


    def answer_q11(self):
        answer_str = ''
        change_str = ''
        for row in self.rows:
            change_str += u' '.join(row) + '\n'
        answer_str += change_str
        sed_result = self.sub_wrap.sed(self.filename, u's/\t/ /g')
        answer_str += u'sedと一致するか:' + str(change_str == sed_result.decode('utf-8'))
        return answer_str
        

if __name__ == '__main__':
    answer_obj = Chapter2Answer()
    answer_str  = ''
    answer_str += u'answer_q10\n' + answer_obj.answer_q10() + '\n'
    answer_str += u'answer_q11\n' + answer_obj.answer_q11() + '\n'
    print answer_str
