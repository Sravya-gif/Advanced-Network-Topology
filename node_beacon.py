import socket,json,time,uuid

BCAST="255.255.255.255"
PORT=6000
ID=str(uuid.uuid4())[:8]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while True:
    msg=json.dumps({"id":ID})
    s.sendto(msg.encode(),(BCAST,PORT))
    time.sleep(2)
