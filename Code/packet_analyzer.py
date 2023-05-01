from filter_packets import *
from packet_parser import *

from compute_metrics import *


icmp=filter('./Captures/Node1.txt')
ar=parse(icmp)
compute(ar[5],ar[4],"192.168.100.1",ar[1],ar[2],ar[0],ar,"1")
icmp=filter('./Captures/Node2.txt')
ar=parse(icmp)
compute(ar[5],ar[4],"192.168.100.2",ar[1],ar[2],ar[0],ar,"2")
icmp=filter('./Captures/Node3.txt')
ar=parse(icmp)
compute(ar[5],ar[4],"192.168.200.1",ar[1],ar[2],ar[0],ar,"3")
icmp=filter('./Captures/Node4.txt')
ar=parse(icmp)
compute(ar[5],ar[4],"192.168.200.2",ar[1],ar[2],ar[0],ar,"4")