from listfoldername import listfoldername, getfiles
from createdocx import createdoc
import os

# 確認資料匣是否存在
currentpath = os.getcwd()
OUTPATH = os.path.join(os.getcwd(), 'report')
exitfolder1 = os.path.join(os.getcwd(), '__pycache__')

if os.path.isdir(OUTPATH):
    print('輸出目錄已存在..')
else:
    os.mkdir(OUTPATH)

listfolder = listfoldername(currentpath)
ex1 = listfolder.index(exitfolder1)
ex2 = listfolder.index(OUTPATH)
if ex1 is not None:
    del listfolder[ex1]
if ex2 is not None:
    del listfolder[ex2]

for folder in listfolder:
    # print('笑笑:', folder)
    lowfolder = listfoldername(folder)
    for ff in lowfolder:
        # print('哭哭:', ff)
        files = getfiles(ff)
        createdoc(
            folder,
            currentpath,
            ff,
            files,
            OUTPATH,
        )
