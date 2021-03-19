
# coding: utf-8
'''
用于写一些经常需要被调用的函数或者是处理特定任务的函数；
比如对于输入数据image或者video的处理；
如果工程量很大的话可以分开写多个utils文件；
'''
import os
import config
import numpy as np
import torch

'''
The file is used for frequently used fuctions, thus named as utilis.
	Functions:
		(1). soft2Hard(probOut): Transform probility to tag, the input must be on cpu
		(2). deviceGetter(): Current availabel device getter, 'gpu'/'cpu'.
	Description:
		(a). (1) is model related, could be used for 
		(b). (2) is device realted.
	Using:
		(x). ------------
'''

def soft2Hard(probOut):
	'''
	Transform probility to tag, the input must be on cpu
	Input:
		probOut: model output which could be interpreted as probilities
	Output:
		hardLabel: 0/1 hard label got by probOut and config.THRESHOLD
	'''
	with torch.no_grad():
		return (probOut >= config.THRESHOLD).float()

def deviceGetter():
	'''
	Current availabel device getter, 'gpu'/'cpu'.
	Output:
		device: 'gpu'/'cpu'
	'''
	if(config.GPU_FLAG == False):
		device = torch.device("cpu")
	else:
		device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	return device


def fun():
	






if __name__ == '__main__':
	pass