## Message to Garcia Writeup

While exploring TryHackMe, I came across a room called “Message to Garcia.” The title immediately reminded me of the essay many of us read at the Naval Academy. This was piece emphasizing initiative and mission execution with minimal guidance.
The challenge itself ended up being a good reminder of a cybersecurity truth: initiative alone doesn't break systems, but misconfigurations certainly do. The room involved delivering an encrypted message through a "secure" file transfer service. 

This room highlighted implementation weaknesses surrounding the file transfer service.

### Walkthrough
**Reconnaissance is key.** My first step to most TryHackMe rooms is to perform an nmap scan. Nmap or "Network Mapper" is a reconaissance tool used for host/service enumeration. Stealth was not a concern for this scan so I opted for a default TCP scan with version detection. `nmap -sV <target_ip> -p-` yielded 3 open services:
   - SSH on Port 22
   - HTTP on Port 80
   - UPNP on Port 5000
UPnP (Universal Plug and Play) can expose system information, and Nmap even has a script (upnp-info) to enumerate it. I noted this for later and began with the HTTP service.
<div align="center">
<img width="600" alt="MessagetoGarcia1" src="https://github.com/user-attachments/assets/28b46153-b0ab-49ed-9a06-04bbc9619181"/>
  </div>
For the HTTP service, I conduct a directory enumeration using dirb. The command: `dirb http://&lttarget_ip&gt/ /usr/share/wordlists/dirb/common.txt` yielded several pages of interest.

<div align="center">
<img width="382" height="304" alt="MessagetoGarcia4" src="https://github.com/user-attachments/assets/ecc16b00-403a-49d6-8ea9-20219944768b"\>
</div>
The fetch page is what stould out to me the most because it allowed access to internal and external files.
<div align="center">
<img width="500" height="242" alt="MessagetoGarcia5" src="https://github.com/user-attachments/assets/e6c475d3-dec6-4336-9823-296534d706c6"\>
 </div> 
As a default I typed in the recommended file **file://README.md**
