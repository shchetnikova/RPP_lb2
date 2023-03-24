#2.3
s = list(input())
print('Количество удаленных символов: ', s.count('.'))
s_len = len(s)
for i in range (s_len):
  if s[i] == '.':
      s[i] = ''
print(s)