import gensim
import os
import uuid


def ParsData(info):
    info = info.replace('\n', ' ').replace(',', '').replace('.', '').replace('/', ' ')
    info = info.upper()

    file_path = str(uuid.uuid4().hex) + '.txt'
    model_path = str(uuid.uuid4().hex) + '.model'
    tag_path = 'tags.txt'

    fw = open(file_path, 'w')
    fw.write(info)
    fw.close()

    data = gensim.models.word2vec.LineSentence(file_path)

    model = gensim.models.Word2Vec(data, size=500, window=500, min_count=1, sg=0)
    model.init_sims(replace=True)
    model.save(model_path)

    model = gensim.models.Word2Vec.load(model_path)
    model.init_sims(replace=True)

    fr = open(tag_path, 'r')

    result = []
    for word in fr.read().split():
        if word.upper() in model:
            result.append(word)

    fr.close()

    os.remove(file_path)
    os.remove(model_path)

    return ' '.join(result)
