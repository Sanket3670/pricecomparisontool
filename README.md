This Python code implements a simple price comparison tool with a graphical user interface (GUI) using Tkinter. Here's a breakdown of its functionality:

# Imports:
1.tkinter: Python's standard GUI (Graphical User Interface) library.</br>
2.requests: Library for making HTTP requests.</br> 
3.time: Provides various time-related functions.</br> 
4.sqlite3: Library for SQLite database operations.</br>

# Database Setup:
1.Establishes a connection to an SQLite database named price_data.db.</br>
2.Creates a table named prices if it doesn't exist, with columns for the product name, Amazon price, and Google price.

# Database Functions:
insert_into_db: Inserts data into the SQLite database table.

# Search Functionality:
1.search: Gets the product name from the entry widget.</br>
2.Sends requests to a price comparison API (price-analytics.p.rapidapi.com) for Amazon and Google prices. </br>
3.Polls the API to get the results after a delay (120 seconds in this case). </br>
4.Updates the GUI labels with the retrieved Amazon and Google prices.</br>
5.Inserts the product name, Amazon price, and Google price into the SQLite database.</br>
6.Graphical User Interface (GUI):

Creates a Tkinter window titled "Price Comparison". Includes labels and an entry field for entering the product name. Provides a "Search" button to trigger the search functionality. Displays labels for showing the Amazon and Google prices.

# Main Loop:
Starts the Tkinter event loop to run the GUI application.

# Database Connection Closing:
Closes the connection to the SQLite database when the Tkinter event loop exits. This code can be useful for users to quickly compare prices of a product on Amazon and Google within the specified country (in this case, India) and store the results for future reference. It provides a simple interface for conducting price comparisons efficiently. 
![Screenshot (182)](https://github.com/Sanket3670/pricecomparisontool/assets/144824011/6f645a01-64e3-464e-bdee-b5be44373bf6)
![Screenshot (184)](https://github.com/Sanket3670/pricecomparisontool/assets/144824011/552489b9-8da0-4ebd-a437-588daa8081a9)

