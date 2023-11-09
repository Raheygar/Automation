import pyshark
##Live Capture traffic in the wifi adapter
Live_Capture_Traffic = pyshark.LiveCapture(interface='Wi-Fi')
for packet in Live_Capture_Traffic:
    try:
        Source = packet.ip.src
        Destination = packet.ip.dst
        Protocol = packet.transport_layer
        Src_Port = packet.tcp.srcport
        Dst_Port = packet.tcp.dstport
        if Protocol == 'TCP':
            print(f"{Protocol}####{Source}:{Src_Port}----->>>>{Destination}:{Dst_Port}")
    except AttributeError as e:
        pass