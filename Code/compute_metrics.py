

def compute(info,length,ip,source,destination) :
	#Data Metrics
	b_ereq=0
	no_ereq=0
	d_ereq=0
	no_ereqs=0
	no_ereqr=0
	no_ereps=0
	no_erepr=0
	for i in range(0,len(info)):
			if "Echo (ping) request " in info[i]:
				no_ereq+=1
				b_ereq+=length[i]
				d_ereq+=length[i]
				if source[i]==ip:
					no_ereqs+=1
				elif destination[i]==ip:
					no_ereqr+=1
			elif "Echo (ping) reply " in info[i]:
				no_erep+=1
				b_erep+=length[i]
				d_erep+=length[i]		
				if source[i]==ip:
					no_ereps+=1
				elif destination[i]==ip:
					no_erepr+=1
	#Time based metrics




	
	print('called compute function in compute_metrics.py')

