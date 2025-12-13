# DevOps Python Utility Scripts

This repository contains Python scripts commonly used in DevOps workflows to improve **security**, **monitoring**, and **data protection**.  
Each script is designed to be simple, reusable, and easy to execute from the command line.

---

## Prerequisites

Before running any script, ensure the following are installed on your system:

- Python **3.7 or higher**
- pip (Python package manager)


## Password Strength Checker
**Description**

This script validates the strength of a password based on common security best practices.

**Validation Rules**

The password must:

- Be at least 8 characters long
- Contain uppercase and lowercase letters
- Include at least one digit (0–9)
- Include at least one special character (e.g. ! @ # $ %)

**Script Name**
password-validation.py

```bash
python password-validation.py
```

<img width="832" height="147" alt="image" src="https://github.com/user-attachments/assets/aa4f94c4-370c-4a16-a880-8f039593b2e3" />
<img width="832" height="41" alt="image" src="https://github.com/user-attachments/assets/a97ded5a-d269-4784-9a9f-e4d86476d7f2" />

---
## CPU Health Monitoring Script
**Description**

This script continuously monitors CPU usage on the local machine and raises alerts when usage exceeds a defined threshold of 80%.

**Features**
- Continuous CPU monitoring
- Alert triggered when CPU usage exceeds 80%
- Runs indefinitely until manually stopped
- Graceful error handling

**Library Used**
- psutil
- time

```bash
pip install psutil
pip install time
```

**How to Run**

```bash
python system_health.py
```

**Expected Output**

```
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
Monitoring Stopped by User by pressing CTRL+C
```

**Stop execution using:**
```
Ctrl + C
```

## File Backup Script
**Description**
The backup script copies all files from a source directory to a destination directory while ensuring file name uniqueness.

**Features**
- Accepts source and destination paths as command-line arguments
- Appends timestamps to duplicate file names
- Handles missing directories and permission errors gracefully

**Library Used**
- shutil
- sys
- os
- datetime

```
pip install shutil
pip install sys
pip install os
pip install datetime
```

**Script Name**
backup.py

**How to Run**

```bash
python backup.py /path/to/source /path/to/destination
```

**Example**
```bash
python backup.py ./data ./backup
```

If a file already exists in the destination directory, it will be renamed as:
```
file_2025-01-10_14-30-45.txt
```
