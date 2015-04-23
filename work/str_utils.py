# -*- coding: utf-8 -*-

from random import shuffle


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
    BREAK_CHARS = [u' ', u'.', u',', u'\"']
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


def make_char_ngram(n, sentence):
    u"""
    入力された値のn-gramのリストを作成する
    @param n n-gramのnを指定します
    @param sentence 対象文字列
    @return 作成したn-gramのリスト
    """
    return __make_ngram(n, sentence)
    

def make_word_ngram(n, sentence):
    u"""
    入力された値のn-gramのリストを作成する
    @param n n-gramのnを指定します
    @param sentence 対象文字列
    @return 作成したn-gramのリスト
    """
    words = split_sentence_to_words(sentence)
    return __make_ngram(n, words)


def __make_ngram(n, target):
    u"""
    入力された値のn-gramのリストを作成する
    @param n n-gramのnを指定します
    @param target 処理対象。文とリストに対応
    @return 作成したn-gramのリスト
    """
    ngram_list = []
    target_len = len(target)
    for i in range(target_len - n + 1):
        ngram_value = target[i: i + n]
        ngram_list.append(ngram_value)
    return ngram_list


def make_time_sentence(x, y, z):
    u"""
    x時のyはzという文字列を出力する
    """
    if not isinstance(x, (unicode, str)):
        x = str(x)
    if not isinstance(y, (unicode, str)):
        y = str(y)
    if not isinstance(z, (unicode, str)):
        z = str(z)
    return x + u'時の' + y + u'は' + z


def cipher(sentence):
    u"""
    入力された文字列の英小文字のみ変換して返す
    """
    sentence_len = len(sentence)
    encrypt_str = ""
    for i in range(sentence_len):
        codepoint = ord(sentence[i])
        if codepoint >= 97 and codepoint <= 122:
            encrypt_str += unichr(219 - codepoint)
        else:
            encrypt_str += unichr(codepoint)
    return encrypt_str


def make_typoglycemia(word):
    u"""
    入力された文字列の先頭と末尾を残し、それ以外の順序をランダムに入れ替える
    文字数が四以下の場合には、そのままの値を返す
    """
    word_len = len(word)
    if word_len <= 4:
        return word
    typo_word = word[0]
    random_range = range(1, word_len - 1)
    shuffle(random_range)
    for i in random_range:
        typo_word += word[i]
    typo_word += word[word_len - 1]
    return typo_word

    
"""
if __name__ == '__main__':
    print split_sentence_to_words('Hello Goodbye')
"""
