# -*- coding: utf-8 -*-

import csv

class TsvReader(object):

    def __init__(self, file_path, has_header):
        u"""
        TSVファイルを読み込み、その中身を保持します
        @param file_path TSVファイルパスです
        @param has_header ヘッダを持っているかどうかを指定します
        """
        self.rows = []
        self.header = None
        with open(file_path, 'r') as tsv_file:
            reader = csv.reader(tsv_file, delimiter = '\t')
            if has_header:
                self.header = reader.next()
            for row in reader:
                encode_row = []
                for column in row:
                    encode_row.append(column.decode('utf-8'))
                self.rows.append(encode_row)

                
    def get_header(self):
        return self.header


    def get_rows(self):
        return self.rows


"""
if __name__ == '__main__':
    reader = TsvReader('resource/hightemp.txt')
    print reader.get_header()
"""
