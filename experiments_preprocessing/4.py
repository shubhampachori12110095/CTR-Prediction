____author__ = 'mars'


import sys,subprocess,os
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]


cmd='python feature_engineering/csv2vw_statistical.py {0} {1}'.format(data_path,result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)



cmd='vw {path}train.vw  -f {path}model  -b 20  --quiet --loss_function logistic  --holdout_off'.format(path=result_path)

subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='vw {path}test.vw  -t -i {path}model  -p {path}preds.txt --quiet --loss_function logistic'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='rm {path}train.vw {path}test.vw '.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


cmd='python utils/vw_to_kaggle.py {path}'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)