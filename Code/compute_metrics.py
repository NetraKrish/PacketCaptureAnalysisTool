from filter_packets import get_icmp_packets


ar = get_icmp_packets()
print(set(ar[1]))
def compute(info,length,ip,source,destination) :
	#Data Metrics
	b_ereqr=0
	no_ereq=0
	d_ereqr=0
	b_ereqs=0
	d_ereqs=0
	no_ereqs=0
	no_ereqr=0
	no_ereps=0
	no_erepr=0
	no_erep=0
	no_ereps=0
	no_erepr=0
	
	
	for i in range(0,len(info)):
			if "Echo (ping) request " in info[i]:
				
			
				no_ereq+=1
				if source[i]=='192.168.100.1':
					no_ereqs+=1
					b_ereqs+=int(length[i])
					d_ereqs+=(int(length[i])-42)
				else:
					b_ereqr+=int(length[i])
					d_ereqr+=(int(length[i])-42)
					no_ereqr+=1
			if "Echo (ping) reply " in info[i]:
				print(info[i],source[i],destination[i])
				no_erep+=1
				
					
				if source[i]=='192.168.100.1':
					no_ereps+=1
					
					
				else:
					no_erepr+=1
					
	print(b_ereqr,d_ereqr,b_ereqs,d_ereqs)

	#Time based metrics
compute(ar[5],ar[4],"192.168.100.1",ar[1],ar[2])


	
print('called compute function in compute_metrics.py')

