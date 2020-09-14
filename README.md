# kitsune
A hacking & pentesting framework/toolkit utilizing the best tools for a wide range of different task as well as custom scripts and programs coded by me.



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

### Scanning
- Anonymous port scanning module with nmap + tor + proxychains.
- GitHub repo secrets scanning module with truffleHog
  - Goes through entire commit history of each branch
  - Check each diff from each branch
  - Checked through utilizing regex and entropy
  - Evaluates Shannon entropy for both the base64 char set and hexidecimal char set.
  - Custom regexes for things like subdomain enumeration and s3 bucket detection. 

