import os
print(os.getcwd())
print(os.listdir(r'C:\GitHubDesktop\hyc\xiaojiayu3.7.1'))

os.makedirs  (r'C:\GitHubDesktop\hyc\xiaojiayu3.7.1\a\b')
os.removedirs(r'C:\GitHubDesktop\hyc\xiaojiayu3.7.1\a\b')
print(os.listdir(os.curdir))

print(os.path.getsize(r'C:\GitHubDesktop\hyc\xiaojiayu3.7.1'))