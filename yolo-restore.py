import sys
import os
from BitTornado.Meta.Info import MetaInfo
from glob import glob

def file_size(fname):
    info = os.stat(fname)
    return info.st_size

sourceFiles = [y for x in os.walk(sys.argv[1]) for y in glob(os.path.join(x[0], '*'))]

source = []
for file in sourceFiles:
    source.append((file_size(file), file))
source = dict(source )

torrentsFiles = sourceFiles = [y for x in os.walk(sys.argv[2]) for y in glob(os.path.join(x[0], '*.torrent'))]

for torrentFile in torrentsFiles:
    metainfo = MetaInfo.read(torrentFile)
    info = metainfo['info']
    if 'length' in info:
        # let's assume we just have a file
        print(source[info['length']])
    else:
        for file in info['files']:
            path = ''
            for item in file['path']:
                if path != '':
                    path = path + "/"
                path = path + item
            if file['length'] in source:
                print('linking ' + source[file['length']] + ' to ' + sys.argv[3] + str(info['name']) + '/' + str(file['path'][0]))
                os.system("mkdir " + sys.argv[3] + '/' + str(info['name']) + '/')
                os.system('ln "' + source[file['length']] + '" "' + sys.argv[3] + str(info['name']) + '/' + str(file['path'][0]) + '"')