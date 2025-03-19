#  Keylogger and Anti-Keylogger System  

##  Overview  
The **Keylogger and Anti-Keylogger System** is a cybersecurity tool designed to detect and mitigate keylogging threats. The project consists of:  
1. **Keylogger** – A program that records keystrokes for monitoring purposes.  
2. **Anti-Keylogger** – A detection and alert system that scans files to identify potential keyloggers and provides options to review and delete suspicious files.  

This project is intended for **ethical cybersecurity research and educational purposes only**.  

##  Features  
- ** Keylogger** – Records keystrokes and logs them into a file for analysis.  
- ** Anti-Keylogger** – Detects suspicious files based on predefined patterns and alerts the user.  
- ** File Scanning** – Identifies keylogging activity by analyzing file extensions, names, and sizes.  
- ** User Alerts** – Provides real-time notifications for suspicious files.  
- ** GUI Interface** – Uses Tkinter for an easy-to-use graphical interface.  

##  Tech Stack  
- **Programming Language:** Python  
- **Libraries Used:**  
  - `os` – File system operations  
  - `subprocess` – System commands execution  
  - `Tkinter` – GUI for user interaction  
  - `pynput` – Keyboard input tracking (for the keylogger module)  

##  Installation  

###  Clone the Repository  
```bash
git clone https://github.com/yourusername/keylogger-anti-keylogger.git
cd keylogger-anti-keylogger
