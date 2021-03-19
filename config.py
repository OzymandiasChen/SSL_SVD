# coding: utf-8

'''
用于存放全局路径和全局变量
最好都用全大写命名
'''
import os
import pathlib

#--------------------------------------------Path Settings---------------------------------------------#
'''
RUN_LOCATION:
 	It is an option for where to run the project, 'UBUNTU', 'SERVER2018', 'SERVER2019' or 'WIN'.
 	The dataset path or project path will change accordingly.
'''
RUN_LOCATION = 'UBUNTU'
'''
This setting is only useful when coding and testing.
USE_DEMO_DATASET: True/False
'''
USE_DEMO_DATASET = False
PROJECT_PATH = pathlib.Path(__file__).parent.absolute()
if RUN_LOCATION == 'UBUNTU':
	if USE_DEMO_DATASET == False:
		DATASET_PATH = ''
		JAMENDO_PATH = ''
		RWC_PATH = ''
		MIR1K_PATH = ''
		MELDEY_DB_PATH = ''
		MUSDB18_PATH = ''
		VIBRATO_PATH = ''
		UNLABEL_PATH = ''
	else:
		pass
elif RUN_LOCATION == 'WIN':
	pass
elif RUN_LOCATION == 'SERVER2018':
	pass
elif RUN_LOCATION == 'SERVER2019':
	pass
else:
	pass

#--------------------------------------------Data Loading Info---------------------------------------------#
'''
label: sing/nosing: 1/0
AUDIO_PROCESSSING_METHOD: 
	Raw data processing method, FRAME-LEN_HOP-EN_NMEL
	'1024_315_80'
'''
PITCH_SHIFTINF_RANGE = 2
TRAIN_STEP = 7
VALID_STEP = 5
TEST_STEP = 3
AUDIO_PROCESSSING_METHOD = '1024_315_80'
AUDIO_PROCESSSING_METHOD_LIST = ['1024_315_80', '2048_512_128']
if AUDIO_PROCESSSING_METHOD == '1024_315_80':
	PROCESSER_DATA_FOLDER_NAME = '1024_315_80'
	SR = 22050	# 1k := 1,000
	FRAME_LEN = 1024 # 0.046s/frame
	HOP_LENGTH = 315 # ~0.014s resolution
	N_MELS = 80
	CUTOFF = 8000  # fmax = 8kHz
	FMIN = 27.5
	FMAX = 8000
	WIN_SIZE = 115  # 1.6 sec
	# CNN_OVERLAP = 7  # Hopsize of 5 for training, 1 for inference
elif AUDIO_PROCESSSING_METHOD == '2048_512_128':
	PROCESSER_DATA_FOLDER_NAME = '2048_512_128'
	SR = 22050	# 1k := 1,000
	FRAME_LEN = 2048 # 0.096s/frame
	HOP_LENGTH = 512 # 0.023s resolution
	N_MELS = 128
	CUTOFF = 8000  # fmax = 8kHz, ... ...
	FMIN = 0
	FMAX = 8192
	WIN_SIZE = 25  # ~0.58s
	# CNN_OVERLAP = 7  # Hopsize of 5 for training, 1 for inference

ENERGY_THRESHOLD = 0.0001

#--------------------------------------------SchCNN Paramaters---------------------------------------------#
DROPOUTRATE = 0.2

#--------------------------------------------Training Settings---------------------------------------------#
'''
DATASET_LIST: which dataset are used
'''
'''
Possile:
batchNum: 256
LR: 0.00001
'''
THRESHOLD = 0.5  # threshold for binary classification
MODEL_NAME = 'SchCNN'
MODEL_NAME_LIST = ['SchCNN', 'Res_ZeroMean_StdPool']
if(MODEL_NAME == 'Res_ZeroMean_StdPool'):
	DEEPTH = 5
if(MODEL_NAME == 'SchCNN'):
	ZERO_MEAN = True # useful for 'SchCNN'
OPTIM = 'Adam'	# 'Adam', 'SGD'
LR =  0.00001
MOMENTUM = 0.9
MONITOR = 'acc'
SCHEDULER_FLAG = True	# only be useful when the optimizer is 'SGD'
PS_ARG_FLAG = False

# TRAINSET_LIST = ['Jamendo', 'RWC', 'MedleyDB']	# ['Jamendo', 'RWC', 'RWC_part', 'MIR1K', 'MIR1K_part', 'MedleyDB', 'MedleyDB_part']
TRAINSET_LIST = ['Jamendo', 'RWC']	# ['Jamendo', 'RWC', 'RWC_part', 'MIR1K', 'MIR1K_part', 'MedleyDB', 'MedleyDB_part']
# TRAINSET_LIST = ['Jamendo']	# ['Jamendo', 'RWC', 'RWC_part', 'MIR1K', 'MIR1K_part', 'MedleyDB', 'MedleyDB_part']
VALID_SET_NAME = 'Jamendo' # ['Jamendo', 'RWC', 'RWC_part', 'MIR1K', 'MIR1K_part', 'MedleyDB', 'MedleyDB_part']
# TEST_SET_NAME = 'MedleyDB'
TEST_SET_NAME = VALID_SET_NAME
# a certain generator might be used.
if('RWC' in TRAINSET_LIST): RWC_TRAIN = [0, 1, 2, 3, 4]
elif('RWC_part' in TRAINSET_LIST): RWC_TRAIN, RWC_VALID, RWC_TEST = [0,], [3], [4] #
# elif('RWC_part' in TRAINSET_LIST): RWC_TRAIN, RWC_VALID, RWC_TEST = [0, 1, 2], [3], [4] #
if(TEST_SET_NAME == 'RWC'): RWC_TEST = [0, 1, 2, 3, 4]
elif(TEST_SET_NAME == 'RWC_part'): pass
MIR1K_TRAIN, MIR1K_TEST = [0, 1, 2, 3, 4], [0, 1, 2, 3, 4] # 5 filelists
MedleyDB_TRAIN, MedleyDB_TEST = [10, 11, 12], [10, 11, 12] # 3 filelists
# if('MIR1K' in TRAINSET_LIST):	MIR1K_TRAIN = [0, 1, 2, 3, 4]	else:	MIR1K_TRAIN, MIR1K_VALID, MIR1K_TEST = [0, 1, 2], 3, 4
# 'MIR1K_part' is not currently considered


# UNLABEL_PERCENTAGE = 0.4 # 0.3
EPOCH_NUM = 192
# EPOCH_NUM = 2
BATCH_SIZE = 64
BATCH_SIZE_UNLABEL = 64
VALID_BATCH_SIZE = 512
GPU_FLAG = True
FINALLY_SAVED_MODEL = ['lastModel.pkl', 'bestModel_acc.pkl', 'bestModel_loss.pkl'] # all saved in cpu version
EARLY_STOPPING_TRIGGER = True
if(EARLY_STOPPING_TRIGGER == True):
	EARLY_STOPPING_EPOCH = 16
else:
	EARLY_STOPPING_EPOCH = EPOCH_NUM + 100

#--------------------------------------------Testing Settigs---------------------------------------------#
# TESTED_MODEL = 'bestModel_acc.pkl'

#--------------------------------------------unlabel data Info---------------------------------------------#
# ['audio_Grammy', 'audio_Oscars_old', audio_GrammyNominees20102020']
# [61, 58, 185]

#--------------------------------------------Experiment Settings-----------------------------------------#
TRAIN_MODE = 'SSL' # see below!!!!!!!!!!!!!!!!!!!!!
# TRAIN_MODE_LIST = ['NaiveNN', 'KD', 'KD_SSL', 'DA_KD', 'DA_KD_SSL', 'SSL']

TRAIN_MODE_LIST = ['NaiveNN', 'KD', 'SSL', 'KD_SSL'] # SSL on the way.

if(TRAIN_MODE == 'NaiveNN'):
	pass
elif(TRAIN_MODE == 'KD'): # to validate the similarity hypothesis.
	'''
	KD:= BCE_soft + BCE_hard
	lambda_KD * KD_T * KD_T * BCE_soft + (1 - lambda_KD) * BCE_hard
	'''
	DISTILLER_LIST = ['']
	KD_T = 8
	LAMBDA_KD = 0.5
elif(TRAIN_MODE == 'SSL'): # S2019
	'''
	BCE_hard + BCE_hard
	There is no concept of KD, T. only weight is neeeded.
	'''

	HARD_USING = False
	UNLABEL_FOLDER_LIST = [''] # G1
	DISTILLER_LIST = ['']

	DISTILLER_LIST = ['']
	LAMBDA_SSL = 0.7 # lambda_unlabel
elif(TRAIN_MODE == 'KD_SSL'):
	'''
	Both modes are organized by unlabeled data loss and well-labeled data loss.
	'soft':
		lambda_unlabel * SSL_T * SSL_T * BCE_soft(SSL_T) + (1 - lambda_unlabel) * KDLoss(KD_T, LAMBDA_KD)
	'multi':
		lambda_unlabel * KDLoss(SSL_T, LAMBDA_SSL_KD) + (1 - lambda_unlabel) * KDLoss(KD_T, LAMBDA_KD)
	'''
	UNLABEL_FOLDER_LIST = [''] 
	DISTILLER_LIST = ['']
	# for labeled data.
	KD_T = 8
	LAMBDA_KD = 0.5
	# for unlabed data.
	KD_SSL_MODE = 'soft' # 'multi'/'soft' # too troublesome & not necessary.
	if(KD_SSL_MODE == 'soft'):
		# BCE_soft + KD
		SSL_T = 8 # T for unlabeled data.
		LAMBDA_UNLABEL = 0.5 # weight for unlabed data loss.
	elif(KD_SSL_MODE == 'multi'):
		# KD + KD
		SSL_T = 8 # T for unlabeled data.
		LAMBDA_UNLABEL = 0.5 # weight for unlabed data loss.
		# KD_T_unlabeled = 1
		LAMBDA_SSL_KD = 0.5 # a percentage between hard and soft, only be useful when KD_SSL_MODE == 'multi'
else:
	pass

#--------------------------------------------Distiller Info ---------------------------------------------#
DISTILLER_INFO = {}

UNLABELDATA_INFO[''] = {'name': '',
									'source': '',
									'audio_track_num': 100}



# CLIPPING = 1e-07


if __name__ == '__main__':
	pass