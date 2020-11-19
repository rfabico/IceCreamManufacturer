# IceCreamManufacturer
A web UI for CPS510 assignment 9, created using Python Flask.

# Installing Dependencies
Requires Python 3. Tested on 3.9, but earlier versions may work.
The following Python packages need to be installed

`pip install pandas`

`pip install cx_oracle`

`pip install flask`

Also requires Oracle Instant Client libraries to be installed and on your machine's PATH (for macOS, use the DYLD_LIBRARY_PATH). These may be included with Oracle XE, or can be downloaded separately here: https://www.oracle.com/database/technologies/instant-client/downloads.html

# Running the Application
First, make sure the `FLASK_APP` environment variable is set to `IceCreamMain`. Then, from the root directory of the project, run `flask run`.

The app should then be accessible from `localhost:5000` on any web browser.
