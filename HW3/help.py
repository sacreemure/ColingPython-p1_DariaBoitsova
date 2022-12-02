import zipfile
from os import remove

with zipfile.ZipFile('annot.opcorpora.xml.byfile.zip', mode='r') as corpus:
    files = corpus.namelist()
    train_size = int(len(files) * 0.8)

    train_zip = zipfile.ZipFile('train_set.zip', 'a')
    
    for i in range(1, train_size+1):
        try:
            filename = f"{i}.xml"
            corpus.extract(filename)
            train_zip.write(filename)
            remove(filename)
        except KeyError:
            continue
         
    
    train_zip.close()

    test_zip = zipfile.ZipFile('test_set.zip', 'a')

    for i in range(train_size+2, len(files)+1):
        try:
            filename = f"{i}.xml"
            corpus.extract(filename)
            test_zip.write(filename)
            remove(filename)
        except KeyError:
            continue

    test_zip.close()


