import re 

timeDate = '''time timeDate = "202-11-11T17:00:00+0"></time>
time timeDate = "2020-12-08T29:00:00+0"></time>
time timeDate = "2021-09-17T14:00:00+0"></time>
time timeDate = "2021-11-11==05T11:00:00+0"></time>'''

patten = r'(20\d+)([-]+(0[1-9]|1[012])([-]+))(0[1-9]|([12)[1-9]|3[01])'

for math in re.finditer(patten, timeDate):
    start = math.start()
    end = math.end()
    span = math.span()

print('Found {}at {}:{}, span: {}'.format(timeDate[start:end], start, end, span))