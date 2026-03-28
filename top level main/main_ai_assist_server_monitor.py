
#This "Main" program is a proxy for Dong's AI_Assist main() program
#Its purpose is to test the "Health_Monitor"program file (.py) which defines the "status" function
#IRL, the health_monitor4.py function will be called periodically by Dong's AI_Assist main() program

from health_monitor1  import status
from send_email import send_email   #makes the function send_email available
import asyncio

async def main():
    max_resp_time = 3    #arbitray value, set low for testing 
    health = False        #initial starting value
    i=1                  #first loop
    print("Starting values (pre-set):", " max_resp_time;", max_resp_time, "      AI Assist Server Health;", health)
    while i < 5:
        print("We are stil in the main program (proxy for main program)")
        print("Now call health_monitor1.py to get real health")
        await asyncio.sleep(2)
        # status is async, so we must await it
        health = await status(max_resp_time, health)   # status is the function in the health monitor program.
        await asyncio.sleep(1)  
        print ("monitor loop number:", i)
        i=i+1
        print ("Now back from health_monitor function")
    print ("Ending value (from status function): Final AI Assist Server Health;", health)

    health = False   # example just for testing, this forces email to be sent
    print ("email value (from status function): Final AI Assist Server Health;", health)

    if not health:                 #sends email only if False (there is a problem)
        send_email(
            subject="Health Monitor Alert",
            body="AI Assist server is not responding (actually it's OK, this is just a test",
            sender="pwilford5@gmail.com",
            receivers=["paul@withleverage.ai",
                       "pwilford5@gmail.com",
                       "dong@withleverage.ai"]
        )

if __name__ == "__main__":
    asyncio.run(main())

