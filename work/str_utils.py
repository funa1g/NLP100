
# -*- coding: utf-8 -*-

def reverse_string(target_str):
    u"""
    入力された文字列を逆順で返すメソッドです
    サロゲートペア未対応
    @param target_str 入力文字列. string でも実行できますが、 unicode での入力を推奨
    @return 入力された文字列を逆順にした文字列
    """
    reverse_str = ""
    target_len = len(target_str)
    for i in range(target_len):
        reverse_str += target_str[target_len - i - 1]
    return reverse_str


"""
if __name__ == '__main__':
    print reverse_string(u'あいう')
"""
