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

```bash
python password_checker.py


