# IceCreamManufacturer
A web UI for CPS510 assignment 9, created using Python Flask.

# Installing Dependencies
Requires Python 3. Tested on 3.9, but earlier versions may work.
The following Python packages need to be installed

```
pip install pandas
pip install cx_oracle
pip install flask
```

Also requires Oracle Instant Client libraries to be installed and on your machine's PATH (for macOS/Linux, you may need to use the DYLD_LIBRARY_PATH). These may be included with Oracle XE, or can be downloaded separately here: https://www.oracle.com/database/technologies/instant-client/downloads.html

If downloading separately, the Basic or Basic Light libraries are sufficient for our application.

For connecting to the Ryerson Oracle database, you must install and run the VPN as per the course instructions.

# Running the Application
First, make sure the `FLASK_APP` environment variable is set to `IceCreamMain`. Then, from the root directory of the project, run `flask run`.

The app should then be accessible from `localhost:5000` on any web browser. Make sure your VPN is running before performing any actions, so that the database connection works.

Run on Windows:

```
set FLASK_APP=IceCreamMain
flask run
```

Run on macOS/Linux:
```
export FLASK_APP=IceCreamMain
flask run
```

# Features
1. Test Connection
1. Drop Tables
1. Create Tables
1. Populate Tables
1. Run Queries (click dropdown to view)
   * Query 1: List orders shipped within the last 90 days
   
    ![query1](/images/query1.PNG?raw=true)
   
   * Query 2: List flavours & ingredients
   
    ![query2](/images/query2.PNG?raw=true)
   
   * Query 3: Count suppliers outside of Toronto
   
    ![query3](/images/query3.PNG?raw=true)
   
   * Query 4: List flavours without sugar
   
    ![query4](/images/query4.PNG?raw=true)
   
   * Query 5: List orders before October 8th with total payment over $700
   
   ![query5](/images/query5.PNG?raw=true)


