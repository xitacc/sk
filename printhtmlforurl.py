from requests import *
r = request('GET','https://openloadmov.net/movies/howls-moving-castle-2004/')
print(r)
print('________TEXT___________')
print(r.text)
print('________CONTENT___________')
print(r.content)
with open('howls_movingcastle_text','+w') as f:
    f.write(r.text)

with open('howls_movingcastle_content','+w') as f:
    f.write(str(r.content))


