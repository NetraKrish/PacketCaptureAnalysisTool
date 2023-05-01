
import re


def compute(info,length,ip,source,destination,timearr,ar,num) :
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
	totaltime =0
	totaltime2=0
	hopsum=0
	
	for i in range(0,len(info)):
			#check if request or reply
			if "Echo (ping) request " in info[i]:
				no_ereq+=1
				#check of sent or received
				if source[i]==ip:
					#for roundtrip, throughput and goodput calculation
					reptime = float(ar[0][i+1])
					time = abs(reptime - float(timearr[i]))
					totaltime+=time
					no_ereqs+=1
					b_ereqs+=int(length[i])
					d_ereqs+=(int(length[i])-42)
				else:
					#for average reply delay
					reptime2 = float(ar[0][i+1])
					time2 = abs(reptime2 - float(timearr[i]))
				
					totaltime2+=time2
					b_ereqr+=int(length[i])
					d_ereqr+=(int(length[i])-42)
					no_ereqr+=1
			if "Echo (ping) reply " in info[i]:
				

				no_erep+=1
				if source[i]==ip:
					no_ereps+=1
					
				else:
					#for average hop
					ttl_match = re.search(r'ttl=(\d+)', info[i])
					if ttl_match:
						ttl = float(ttl_match.group(1))
						hopsum+=(abs(129-ttl))
					no_erepr+=1
				
						

	rtt =round(totaltime*1000/no_ereqs,2)	
	ert = round(b_ereqs/totaltime/1000,1)	
	erg = round(d_ereqs/totaltime/1000,1)	
	ard = round((totaltime2/no_ereqr)*1000000,2)
	ah=round(hopsum/no_ereqs)
	if (ip == "192.168.100.1"):
		file = open("./output.csv","w")
	else: 
		file = open("./output.csv","a")
	file.write("Node"+num)
	file.write("  \n")
	file.write("Echo Requests Sent" + "," + "Echo Requests Received" + "," + "Echo Replies Sent" + "," + "Echo Replies "+ "Received\n")
	file.write(str(no_ereqs)+ "," + str(no_ereqr) + "," + str(no_ereps) + "," + str(no_erepr) + "\n")
	file.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
	file.write(str(b_ereqs) + "," + str(d_ereqs) + "\n")
	file.write("Echo Request Bytes Received (bytes)" + "," + "Echo Request Data Received (bytes)\n")
	file.write(str(b_ereqr) + "," + str(d_ereqr) + "\n")
	file.write(" \n")

	file.write("Average RTT (milliseconds)" + "," + str(rtt)+ "\n")
	file.write("Echo Request Throughput (kB/sec)" + "," + str(ert)+ "\n")
	file.write("Echo Request Goodput (kB/sec)" + "," + str(erg) + "\n")
	file.write("Average Reply Delay" + "," + str(ard) + "\n")
	file.write("Average Echo Request Hop Count" + "," + str(ah) + "\n")
	file.write(" \n")
	file.close()
	


