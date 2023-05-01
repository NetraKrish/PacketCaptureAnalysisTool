from filter_packets import *

from compute_metrics import *


ar=get_icmp_packets('./Captures/Node1.txt')
compute(ar[5],ar[4],"192.168.100.1",ar[1],ar[2],ar[0],ar,"1")
ar=get_icmp_packets('./Captures/Node2.txt')
compute(ar[5],ar[4],"192.168.100.2",ar[1],ar[2],ar[0],ar,"2")
ar=get_icmp_packets('./Captures/Node3.txt')
compute(ar[5],ar[4],"192.168.200.1",ar[1],ar[2],ar[0],ar,"3")
ar=get_icmp_packets('./Captures/Node4.txt')
compute(ar[5],ar[4],"192.168.200.2",ar[1],ar[2],ar[0],ar,"4")
