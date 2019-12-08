## Raspi led control

Small application to control raspberry pi 3B+ GPIO pins. 

* Clone into raspberry and install dependencies
    
    - ```pip install -r requirements.txt```

* Run the server
   
   - ```sudo python3 app.py```
   
* You should now be able to access the serve in your local network:
    
    -  ```curl <device-ip>:8081/ping``` (answers *pong*)
    
       
   