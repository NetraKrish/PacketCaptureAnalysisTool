from filter_packets import filter



def parse(icmp_data):

    time_data = []
    source_ip_data = []
    dest_ip_data = []
    protocol_data = []
    length_data = []
    info_data = []
    for packet in icmp_data:
        time_data.append(packet[0])
        source_ip_data.append(packet[1])
        dest_ip_data.append(packet[2])
        protocol_data.append(packet[3])
        length_data.append(packet[4])
        info_data.append(packet[5])

    return time_data, source_ip_data, dest_ip_data, protocol_data, length_data, info_data, icmp_data

