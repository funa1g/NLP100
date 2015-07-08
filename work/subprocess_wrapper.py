# -*- coding: utf-8 -*-

import subprocess

class SubprocessWrapper(object):

    def wc_line_count(self, file_path):
        u"""
        wcコマンドにより行数を確認する
        @param file_path 対象ファイルパス
        @return <int> 行数
        """
        wc_result = subprocess.check_output(['wc', '-l', file_path])
        wc_count = int(wc_result.split(' ')[0])
        return wc_count


    def sed(self, file_path, pattern):
        u"""
        sedコマンドにより、ファイルの値を置換した結果を返す
        @param file_path 対象ファイルパス
        @param pattern 変換パターンを示す文字列 ex. s/xx/XXX/g
        @return 変換結果文字列
        """
        return subprocess.check_output(['sed', pattern, file_path])
