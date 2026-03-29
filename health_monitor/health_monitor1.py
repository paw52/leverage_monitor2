

import asyncio
import websockets
import json

url = "wss://do.trustbcs.com/api/SW/ws?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdGFuIiwiZXhwIjoxNzg3MTczMDEyfQ.U3Z62c8icXLr1t4acFWiOCsOqBtko_MBK0vLyyoA--o"

async def status(max_resp_time,health):
    async with websockets.connect(url) as ws:
        print(">>>> Entered Health_Monitor Function")

      # Send initiation code to server over ws connection, pause until message is fully sent
        await ws.send(json.dumps({"start_chat":""}))

      # check to see if standard first response (thread id) is correctly received
        try:
            thread_reply = await asyncio.wait_for(ws.recv(), timeout=max_resp_time)
            print("Received Thread ID:", thread_reply)
            heath=True
            print ("health=",health)

        except asyncio.TimeoutError:
            print("No response for thread_id in 30 seconds, sending timeout message...")
            await ws.send(json.dumps({"timeout": "no_response"}))
            health=False
            print ("health=",health)

      # check to see if standard second response (initial chat greeting) is correctly received
        try:
            greeting_reply = await asyncio.wait_for(ws.recv(), timeout=max_resp_time)
            print("Received Initial Chat Greeting:", greeting_reply)
            health=True
            print ("health=",health, "second check_smiley")
            print ("server is seems to be properly active, monitor received thread ID and greeting")

        except asyncio.TimeoutError:
            print("No response greeting reply in 30 seconds, sending timeout message...")
            await ws.send(json.dumps({"timeout": "no_response"}))
            health=False
            print ("health=",health)


      # now send server a continuing message chain
        #await ws.send(json.dumps({"messages":[{"text":"How are you"}]}))
        #print("Seems like nothing more will be sent, so the final ws.recv() just hangs")
        print(">>>> Returning to main() proxy function")

    return health

    # receive a "final, continuing message" from the server
    # note   -   since websocket communication is not "up", this hangs things)
    # final_reply = await asyncio.wait_for(ws.recv(), timeout=max_resp_time)
    # print("Received Final Reply:", final_reply)





