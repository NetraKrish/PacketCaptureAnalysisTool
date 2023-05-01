def get_icmp_packets(filename):
    icmp_data = []


    time_data = []
    source_ip_data = []
    dest_ip_data = []
    protocol_data = []
    length_data = []
    info_data = []

    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if "ICMP" in lines[i]:
                data = lines[i].split()
                time = data[1]
                source_ip = data[2]
                dest_ip = data[3]
                protocol = data[4]
                length = data[5]
                info = " ".join(data[6:])
                
                time_data.append(time)
                source_ip_data.append(source_ip)
                dest_ip_data.append(dest_ip)
                protocol_data.append(protocol)
                length_data.append(length)
                info_data.append(info)

                icmp_data.append([time, source_ip, dest_ip, protocol, length, info])

    return time_data, source_ip_data, dest_ip_data, protocol_data, length_data, info_data, icmp_data
