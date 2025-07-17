============================================= Project Name: ================================================

Contact Management System

This is the file that you can refer to in order to solve any problems related to this project.

This project is designed to handle user authentication and validation tasks using a graphical interface built with Tkinter and a backend database managed with MySQL.

------------------------------------------------------------------------------------------------------------
📦 Files Overview
------------------------------------------------------------------------------------------------------------

🔹 main.py  
- The main script of the project.  
- It brings together the functions and modules to implement the core functionality of the application.  
- Running this script will start the contact management workflow (Add, Display, Delete, and Search contacts).

------------------------------------------------------------------------------------------------------------
🔧 Installing MySQL Connector
------------------------------------------------------------------------------------------------------------

To install the Python MySQL connector, open your command line interface (CMD) and run:

    pip install mysql-connector-python

------------------------------------------------------------------------------------------------------------
💾 Installing MySQL 8.0 Command Line Client
------------------------------------------------------------------------------------------------------------

If you haven’t installed MySQL yet, download and install it from the official website:

    https://dev.mysql.com/downloads/mysql/

Or search for “MySQL 8.0 download” on Chrome or any browser and install it from a trusted source.

------------------------------------------------------------------------------------------------------------
🗃️ MySQL Command Line Integration (Database Setup)
------------------------------------------------------------------------------------------------------------

Here are all the SQL commands you need to run in the MySQL command line to set up your database:

    -- Step 1: Create the database
    CREATE DATABASE contact_management;

    -- Step 2: Use the database
    USE contact_management;

    -- Step 3: Create the table
    CREATE TABLE contact_register (
        f_name VARCHAR(50) NOT NULL,
        l_name VARCHAR(50) NOT NULL,
        address VARCHAR(200) NOT NULL,
        contact VARCHAR(15) NOT NULL,
        email VARCHAR(100) NOT NULL,
        PRIMARY KEY (contact)
    );

    -- Step 4: Create a new MySQL user
    CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

    -- Step 5: Grant all privileges to the new user
    GRANT ALL PRIVILEGES ON contact_management.* TO 'username'@'localhost';

    -- Step 6: Grant basic CRUD privileges (optional but recommended)
    GRANT SELECT, INSERT, UPDATE, DELETE ON contact_management.* TO 'username'@'localhost';

    -- Step 7: Apply changes
    FLUSH PRIVILEGES;

    -- Step 8: Exit the MySQL CLI
    EXIT;

------------------------------------------------------------------------------------------------------------
📊 Helpful Additional Queries for Manual Use
------------------------------------------------------------------------------------------------------------

You can use the following queries in MySQL to manage and inspect your data manually:

    -- View the structure of the contact_register table
    DESCRIBE contact_register;

    -- Count total number of contacts
    SELECT COUNT(*) FROM contact_register;

    -- Search by partial email or contact number
    SELECT * FROM contact_register WHERE email LIKE '%gmail.com%' OR contact LIKE '%0321%';

    -- View recently added contacts (sorted by contact as primary key)
    SELECT * FROM contact_register ORDER BY contact DESC LIMIT 10;

    -- Export all contact data to CSV (ensure MySQL has write access to this path)
    SELECT * FROM contact_register INTO OUTFILE '/tmp/contact_backup.csv'
    FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

    -- Delete all contacts (⚠️ use with caution)
    DELETE FROM contact_register;

------------------------------------------------------------------------------------------------------------
💡 Troubleshooting & Help
------------------------------------------------------------------------------------------------------------

If you run into any issues:

    ✅ Google your error message  
    ✅ Ask ChatGPT  
    ✅ Watch tutorials on YouTube  

------------------------------------------------------------------------------------------------------------
📌 Reminder
------------------------------------------------------------------------------------------------------------

Always ensure that:
- Your MySQL service is running.
- The database credentials in your Python code match the ones set in MySQL.
- You have installed required libraries using pip.

------------------------------------------------------------------------------------------------------------
✅ All Set!
------------------------------------------------------------------------------------------------------------

You are now ready to use the Contact Management System. Happy coding! 🎉
