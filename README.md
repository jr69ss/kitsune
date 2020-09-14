# kitsune

**[!] I'm still working on this project and am long ways of finishing, but just wanted to upload the code to git cuz why not?**


A hacking & pentesting framework/toolkit utilizing the best tools for a wide range of different task as well as custom scripts and programs coded by me.

![Screen Shot 2020-09-13 at 8 46 58 PM](https://user-images.githubusercontent.com/71098497/93033036-7619ef00-f602-11ea-99da-46baf7c34ac4.png)



## Info Gathering

### Footprinting
Efficient and quick footprinting/crawling of websites with Photon Crawler module. 
- Cloning websites locally
- Selecting level of depth of crawling
- Selecting number of threads
- Selecting delay (in seconds) between each HTTP request
- Fetch archived URLs using Wayback
- Automatically looks for auth or API keys/hashes
- Option to choose either csv or json format to save data

### **Scanning**
- Anonymous port scanning module with nmap + tor + proxychains + DNSCrypt + Unbound.
  - If you want to go hardcore on solving DNS leaking, set up an instance of BIND-DNS locally, and set all of your traffic to use Tor, so that any DNS lookups come from a server that you own, specifically, and not from one outside of your control. 
  - You can further strengthen this by setting up a Tor as a transparent proxy for all outbound traffic, at which point, even the lookup sent from your DNS server (internally hosted) will run it’s query over Tor. 
  - There are quite a few good tutorials on building transparent Tor proxies using either embedded boards (such as RPi3), or within a VM
  
 
- GitHub repo secrets scanning module with truffleHog
  - Goes through entire commit history of each branch
  - Check each diff from each branch
  - Checked through utilizing regex and entropy
  - Evaluates Shannon entropy for both the base64 char set and hexidecimal char set.
  - Custom regexes for things like subdomain enumeration and s3 bucket detection. 

