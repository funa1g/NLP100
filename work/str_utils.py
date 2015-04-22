
# -*- coding: utf-8 -*-

def reverse_string(target_str):
    u"""
    入力された文字列を逆順で返すメソッドです
    サロゲートペア未対応, unicode入力に対応しています
    @param target_str 入力文字列
    @return 入力された文字列を逆順にした文字列
    """
    reverse_str = ""
    target_len = len(target_str)
    for i in range(target_len):
        reverse_str += target_str[target_len - i - 1]
    return reverse_str


def get_odd_string(target_str):
    u"""
    入力された文字列の奇数番目のみを出力します
    サロゲートペア未対応, unicode入力に対応しています
    @param target_str 入力文字列
    @return 入力された文字列の奇数番目の文字を連結した文字列
    """
    odd_string = ""
    for i in range(len(target_str)):
        if i % 2 == 0:
            odd_string += target_str[i]
    return odd_string



def connect_string_alternately(first_str, second_str):
    u"""
    二種類の文字列を交互に連結する
    実例：connect_string_alternately(u"パトカー", u"タクシー") = u"パタトクカシーー"
    両者の文字数が異なる場合はエラーとして、空文字列を返す
    @param first_str 前側に連結される文字列
    @param second_str 後側に連結される文字列
    @return 連結した文字列
    """
    str_len = len(first_str)
    if str_len != len(second_str):
        return ""
    connect_str = ""
    for i in range(str_len):
        connect_str += first_str[i] + second_str[i]
    return connect_str


def split_sentence_to_words(sentence):
    u"""
    文を分割し、単語のリストとして返します
    英文, unicodeにのみ対応しています
    @param sentence 分割対象文字列
    @return 各単語のリスト
    """
    words = []
    BREAK_CHARS = [u' ', u'.', u',', u'\'', u'\"']
    sentence_len = len(sentence)
    word_start = 0
    for i in range(sentence_len):
        if sentence[i] in BREAK_CHARS:
            if word_start != i:
                word = sentence[word_start: i]
                words.append(word)
            word_start = i + 1
    if word_start != sentence_len:
        word = sentence[word_start: sentence_len]
        words.append(word)
    return words


def count_words_length(words):
    u"""
    入力された文字列のリストを、その文字数のリストにして返す
    """
    return [len(word) for word in words]


"""
if __name__ == '__main__':
    print split_sentence_to_words('Hello Goodbye')
"""
