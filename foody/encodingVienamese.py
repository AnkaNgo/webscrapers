# -*- coding: utf-8 -*-

import re

patterns = {
    u'[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    u'[đ]': 'd',
    u'[èéẻẽẹêềếểễệ]': 'e',
    u'[ìíỉĩị]': 'i',
    u'[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    u'[ùúủũụưừứửữự]': 'u',
    u'[ỳýỷỹỵ]': 'y'
}

re_patterns = {}
for pattern, repl in patterns.items():
    re_patterns.update({ re.compile(pattern) : repl })
    re_patterns.update({ re.compile(pattern.upper()) : repl.upper() })

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    source: https://sangnd.wordpress.com/2014/01/03/python-chuyen-tieng-viet-co-dau-thanh-khong-dau/
    """
    output = text
    for regex, replace in re_patterns.items():
        output = regex.sub(replace, output)
    return output
