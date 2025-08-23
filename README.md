# CRUD (Create, Read, Update, Delete)


# PURWADHIKA INTERNATIONAL AIRPORT INFORMATION SYSTEM

This system is a program for managing flight information, airlines, routes, and terminals at Purwadhika International Airport. The application provides various features to manage flight data and related information about airlines, routes, and terminals.  

## Data Tables  

| Variable                          | Data Type   | Description                                                                 |
|----------------------------------|-------------|-----------------------------------------------------------------------------|
| `info_penerbangan`               | List        | A list of flight information, initially empty                               |
| `info_maskapai`                  | List        | A list of available airlines, each represented as a string                  |
| `rute_domestik`                  | Dictionary  | A dictionary with airlines as keys and domestic routes (list) as values     |
| `rute_internasional`             | Dictionary  | A dictionary with airlines as keys and international routes (list) as values|
| `terminal_maskapai`              | Dictionary  | A dictionary with airlines as keys and terminal (string) as values          |
| `terminal_maskapai_domestik`     | Dictionary  | Similar to `terminal_maskapai`, but specifically for domestic routes        |
| `terminal_maskapai_internasional`| Dictionary  | Similar to `terminal_maskapai`, but specifically for international routes   |

---

## Main Features  

1. **Manager Login**  
   - Login system for managers with predefined ID and password.  

2. **Passenger Menu**  
   - **View Flight Information**: Displays a list of available flights.  
   - **View Airlines, Routes, Terminals**: Displays information about airlines, routes, and terminals.  
   - **Sort Airlines, Routes, Terminals**: Sorts data of airlines, routes, and terminals based on user preference.  

3. **Manager Menu**  
   - **Flight Information**  
     - **View Flight Information**: Displays flight data.  
     - **Add Flight Information**: Adds a new flight.  
     - **Delete Flight Information**: Deletes a flight by number.  
     - **Edit Flight Information**: Updates details of an existing flight.  
   - **Airlines, Routes, and Terminals**  
     - **Display Data**: Shows information about airlines, routes, and terminals.  
     - **Add Data**: Adds new airlines, routes, and terminals.  
     - **Delete Data**: Removes airlines, routes, and terminals.  
     - **Edit Data**: Modifies existing information about airlines, routes, and terminals.  
     - **Sort Data**: Sorts airlines, routes, and terminal data.  


