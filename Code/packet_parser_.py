from filter_packets_ import get_icmp_packets

time_data = []
source_ip_data = []
dest_ip_data = []
protocol_data = []
length_data = []
info_data = []

icmp_data = get_icmp_packets()

for packet in icmp_data:
    time_data.append(packet[0])
    source_ip_data.append(packet[1])
    dest_ip_data.append(packet[2])
    protocol_data.append(packet[3])
    length_data.append(packet[4])
    info_data.append(packet[5])

print("Time data:", time_data)
print("\n\n\n\n")
print("Source IP data:", source_ip_data)
print("\n\n\n\n")
print("Destination IP data:", dest_ip_data)
print("\n\n\n\n")
print("Protocol data:", protocol_data)
print("\n\n\n\n")
print("Length data:", length_data)
print("\n\n\n\n")
print("Info data:", info_data)
