from filter_packets import get_icmp_data

icmp_data = get_icmp_data()

for packet in icmp_data:
    print(packet[0] + " " + packet[1] + " " + packet[2] + " " + packet[3] + " " + packet[4] + " " + packet[5])
