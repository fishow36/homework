import re

reg_construction = r'([А-Яа-яѢѣ]+\s){3}([А-Яа-яѢѣ]+аго\s[А-Яа-яѢѣ]+[ыиая])(\s[А-Яа-яѢѣ]+){3}'

text = '— Нѣтъ, прежде извольте отсчитать деньги Великорусскаго языка Прекраснаго Хорошо не ? — Хорошо. Прежде.'
##constr = re.findall(reg_construction, text)
constr = re.search(reg_construction, text).group()
print(constr)
