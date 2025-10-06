# CareLog_Group7
Our CareLog Project

This folder contains the code for CareLog. It contains a prototype version of the software, where upon execution all kinds of user account pages can be accessed.


## Each part
### App:
This folder contains all the classes for `manager`, `patient`, `medstaff`, `admin` and `user`, as well as other classes related to page functions, which are within folders.

### Data:
This folder contains the `carelog.json` file that holds all saved system data.

### GUI:
This folder contains the GUI files.
- `main_dashboard`: Launches main page and page navigation
- `admin_pages`: The page for admin view
- `patient_pages`: The page for patient view
- `medstaff_pages`: The page for medstaff view
And other subpages for program functions.

### Main:
The overall main function. Runs launch.

## How to run
1. In your terminal, execute the command: streamlit run main.py
2. This opens a browser page where the app can be navigated.
3. In the sidebar the view mode can be chosen from admin, patient or medstaff, to login the password is 'password'.
4. Close the tab and ctrl + c in the terminal to stop running.

## Design choices/assumptions
- Upon execution, any existing databases are immediately searched for within the path.
    - (If none are found, a new one is created)

