import numpy as np
import requests
import json

#tasks=dict()
#for i in range(1):
	#tasks[i]=int(np.random.uniform(100,1000))
	#tasks[i]=750
#print(tasks)
#while 1:
load=dict()
load['round']=1000
r=requests.post('http://34.80.232.139:80', data = json.dumps(load))
#r=requests.post('http://127.0.0.1:80', data = json.dumps(tasks))
print(json.loads(r.text)['t'])