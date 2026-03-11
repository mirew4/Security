## Message to Garcia Writeup

While exploring TryHackMe, I came across a room called “Message to Garcia.” The title immediately reminded me of the essay many of us read at the Naval Academy. This was piece emphasizing initiative and mission execution with minimal guidance.
The challenge itself ended up being a good reminder of a cybersecurity truth: initiative alone doesn't break systems, but misconfigurations certainly do. The room involved delivering an encrypted message through a "secure" file transfer service. 

This room highlighted implementation weaknesses surrounding the file transfer service.

### Walkthrough
#### Reconnaissance is key
My first step to most TryHackMe rooms is to perform an nmap scan. Nmap or "Network Mapper" is a reconaissance tool used for host/service enumeration. Stealth was not a concern for this scan so I opted for a default TCP scan with version detection. `nmap -sV <target_ip> -p-` yielded 3 open services:
   - SSH on Port 22
   - HTTP on Port 80
   - UPNP on Port 5000
UPnP (Universal Plug and Play) can expose system information, and Nmap even has a script (upnp-info) to enumerate it. I noted this for later and began with the HTTP service.

<div align="center">
<img width="600" alt="MessagetoGarcia1" src="https://github.com/user-attachments/assets/28b46153-b0ab-49ed-9a06-04bbc9619181"/>
</div>

For the HTTP service, I performed directory enumeration using dirb. The command: `dirb http://<target_ip>/ /usr/share/wordlists/dirb/common.txt` yielded several pages of interest.

<div align="center">
<img width="382" height="304" alt="MessagetoGarcia4" src="https://github.com/user-attachments/assets/ecc16b00-403a-49d6-8ea9-20219944768b"\>
</div>

The `/fetch` page is what stould out to me the most because it allowed access to internal and external files.

<div align="center">
<img width="500" height="242" alt="MessagetoGarcia5" src="https://github.com/user-attachments/assets/e6c475d3-dec6-4336-9823-296534d706c6"\>
</div> 

As a default I typed in the recommended file: **file://README.md**

#### README reveals
The README file revealed the type of encryption and the server-side scripts the application used to encrypt the message. Using the `/fetch` endpoint, I entered `file://create_message.py`. The application revealed the entire script used to generate the encrypted message, including the key, the message, and the method. Running create_message.py as a local script outputs a file `message.enc` which in turn can be uploaded into the API to reveal the flag.

### Answers
##### Question 1: Who is the Lieutenant who delivered the message to Garcia?
Answer to this one lies within the story itself. No spoilers here. 
##### Question 2: What implementation of authenticated encryption is used?
Answer is found in the README.md file found on the `/fetch` endpoint. 
##### Question 3: What is the encryption key?
Answer is found in the create_message.py file. Enter `file://create_message.py` into `/fetch` input.
##### Question 4: What is the message that needs to be delivered?
Answer is found in the create_message.py file. Enter `file://create_message.py` into `/fetch` input.
##### Question 5: What is the flag?
Flag found by running the create_message.py script locally and uploading the `message.enc` file into the "secure" file transfer service.

### Lessons Learned
1. **Strong cryptography does not guarantee a secure system.** Fernet authentication is a secure and widely accepted cryptographic implementation. However, the application exposed internal files through the /fetch endpoint. The key and message were easily retrievable. Security failed at the implementation layer of the program.
2. **Improper file access controls can expose sensitive information.** The `/fetch` functionality allowed retrieval of internal files using `file://` paths. This created a **local file inclusion-style vulnerability**
3. **Server-side code should never be accessible to users.** Retrieval of the python code exposed the encryption key and the plaintext message required to solve this challenge. In the real world, exposure of backend scripts can lead to credential leaks and compromise of application logic.
