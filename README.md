# kitsune
[![DeepSource](https://deepsource.io/gh/rai0x90/kitsune.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/rai0x90/kitsune/?ref=repository-badge)

**[!] I'm still working on this project and am long ways of finishing, but just wanted to upload the code to git cuz why not?**


A hacking & pentesting framework/toolkit utilizing the best tools for a wide range of different tasks as well as custom scripts and programs coded by me.
Please check out the wiki for full guides on using the various modules.

![Screen Shot 2020-09-13 at 8 46 58 PM](https://user-images.githubusercontent.com/71098497/93033036-7619ef00-f602-11ea-99da-46baf7c34ac4.png)



## Info Gathering


### Footprinting
**efficient and quick footprinting/crawling of websites with Photon Crawler module.**
- Cloning websites locally
- Selecting level of depth of crawling
- Selecting number of threads
- Selecting delay (in seconds) between each HTTP request
- Fetch archived URLs using Wayback
- Automatically looks for auth or API keys/hashes
- Option to choose either csv or json format to save data



### Scanning
- **ordinary Nmap recon scanning** 
- **Nmap Shodan API Scanning**
  - Utilizes Nmap's Shodan NSE script 
- **anonymous scanning with automated "burnable" DigitalOcean droplet deployment + nmap + tor**
  - very secure aggressive scanning method! (used by the pro bad guys lol)
  - Automates droplet spinup and utilizes tor to avoid correlation attacks
  - Sets up nmap scanning automatically so you only need to input target URL/IP
  - Automatically "burns" the droplet after scanning is finished
- **GitHub repo secrets scanning with truffleHog**
  - Goes through entire commit history of each branch
  - Check each diff from each branch
  - Checked through utilizing regex and entropy
  - Evaluates Shannon entropy for both the base64 char set and hexidecimal char set
  - Custom regexes for things like subdomain enumeration and s3 bucket detection
  
  

### OSINT
- **facial recognition search module**
  - With 1 pic and a name, you can search the internet for any SNS profiles. 
  - Modified EagleEye with better facial recognition algorithm and support for around 75 sites.
