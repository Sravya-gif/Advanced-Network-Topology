import asyncio,json
from topology import update_node,cleanup,rebuild_edges

PORT=6000

class UDP(asyncio.DatagramProtocol):
    def datagram_received(self,data,addr):
        d=json.loads(data.decode())
        update_node(d["id"])

async def run():
    loop=asyncio.get_running_loop()
    await loop.create_datagram_endpoint(
        UDP,local_addr=("0.0.0.0",PORT)
    )
    while True:
        cleanup()
        rebuild_edges()
        await asyncio.sleep(1)

asyncio.run(run())
