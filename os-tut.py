import os
from datetime import datetime
print(dir(os))
print(os.getcwd())
print(os.chdir('/Users/viveksuyal/Documents/'))
print(os.getcwd())
print(os.listdir())
# os.mkdir('os-demo')
# print(os.listdir())
# os.mkdirs('os-demo2/demo')
# os.rmdir('os-demo')
# os.removedirs('os-demo2/demo')

# os.rename('','')

# READ
print(os.stat('intro.py'))

m_time = os.stat('intro.py').st_mtime
data = datetime.fromtimestamp(m_time)
print(m_time)
print(data)

# tree
# for dirpath,dirname,filename in os.walk(os.getcwd()):
#     print('Current Path',dirpath)
#     print('Directory Name', dirname)
#     print('Files :',filename)

print(os.environ)
print(os.environ.get("HOME"))

# NOT GOOD
file_path = os.environ.get("HOME")+'/test.txt'
print(file_path)

file_path = os.path.join(os.environ['HOME'],'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

