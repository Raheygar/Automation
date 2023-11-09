import pyshark
##Capturing live traffic
Live_Capture = pyshark.LiveCapture(interface='Wi-Fi')
Source = input("Enter the source ip!! : ")
Destination = input("Enter the destination ip !! : ")
syn_recv = False
syn_ack_sent = False
ack_sent = False
for packet in Live_Capture:
    if hasattr(packet,'TCP')  and packet.ip.src == Source and packet.ip.dst == Destination:
        if packet.tcp.flags.syn == '1':
            syn_recv = True
        elif packet.tcp.flags.syn == '1' and packet.tcp.flags.ack == '1':
            syn_ack_sent =True
        elif packet.tcp.flags.ack == '1':
            ack_sent = True
        if syn_recv and syn_ack_sent and ack_sent:
            print(f"3-way handshake established between {Source} and {Destination}")
        else:
            print("3-way handshake cannot be established!!")