# leverage_monitor2
This suite of programs monitors the RU Leverage AI Assist server   
It periodically and regularly pings the server.   
If it does not get the expected response, it sends an email alert to the specified people.
The top-level Main program controls things
   - It enters a loop (simulating monitoring) 
   - Each loop: 
        - 	calls status() from your health monitor 
        - gets back health = True/False 
    After loop finishes: 
         -check final health 
            -If unhealthy: 
                 call send_email() 

