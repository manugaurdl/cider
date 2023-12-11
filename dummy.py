# demo script for running CIDEr
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pydataformat.loadData import LoadData
import pdb
import json
from pyciderevalcap.eval import CIDErEvalCap as ciderEval
from collections import defaultdict
from pyciderevalcap.ciderD.ciderD import CiderD
from pyciderevalcap.cider.cider import Cider
from pyciderevalcap.tokenizer.ptbtokenizer import PTBTokenizer

pathToData = 'data/'

refName = 'pascal50S.json'
candName = 'pascal_candsB.json'

result_file = 'results.json'
df_mode = 'coco-val-df'
# load reference and candidate sentences
loadDat = LoadData(pathToData)
gts, res = loadDat.readJson(refName, candName)

#res = res[:100]
#gts = {img['image_id']: gts[img['image_id']] for img in res}
# for k,v in gts.items():
#     print(k)
#     print(v)
#     print(len(v))
#     break

gts.keys()
new_gts = {}
new_gts['2008_006488.jpg'] = gts['2008_006488.jpg'] 
new_res = []
for i in res:
    if i['image_id'] == '2008_006488.jpg':
        new_res.append(i)

print(new_gts)
print(new_res)

tokenizer = PTBTokenizer('gts')
_gts = tokenizer.tokenize(new_gts)
tokenizer = PTBTokenizer('res')
_res = tokenizer.tokenize(new_res)

_gts
import ipdb;ipdb.set_trace()
scorer = Cider(df='coco-val')
scorerD = CiderD(df='coco-val')