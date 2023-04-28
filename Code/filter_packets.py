def get_icmp_packets():
    icmp_data = []

    with open('PacketCaptureAnalysisTool/Captures/Node1.txt', 'r') as f:

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
                icmp_data.append([time, source_ip, dest_ip, protocol, length, info])

    return icmp_data

