## MiRBase  (Mirtrons Database) 

## Description
The Mirtrons Database Project is a web application designed to facilitate the searching and retrieval of mirtron (micro RNA) information. 
This application allows users to search for organism names and DNA sequences and provides a user-friendly interface for exploring mirtron data.


<img src="https://github.com/jalghor/MiRBase/blob/main/images/search_example.png" alt="My Image" width="1000" />


## Features
- **Search for Organism Names**: Users can search for specific organism names and obtain relevant mirtron data.
- **Search for DNA Sequences**: Users can perform searches based on the DNA sequences associated with the mirtrons.
- **Autocomplete Suggestions**: The search input provides autocomplete suggestions based on user input.
- **Responsive Design**: The interface is designed to be responsive and user-friendly across devices.
  
## Tools Used
- **Frontend**: HTML, CSS, JavaScript (jQuery, jQuery UI)
- **Backend**: Python (CGI scripts)
- **Database**: MySQL

## Installation

### Prerequisites
- A web server (e.g., Apache) running PHP or Python CGI support.
- MySQL Database server set up to host the mirtron database.
- Python with the `mysql-connector-python` library installed.

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mirtrons-database.git
   ```

2. Navigate into the project directory:
   ```bash
   cd mirtrons-database
   ```

3. Place HTML, CSS, and JavaScript files in the appropriate directory for your web server. 
   - Typically, HTML files go in `DocumentRoot`, while CGI scripts go in the `CGI-Executables` directory (modify paths based on your server configuration).

4. Create a MySQL database and import the mirtron data:
   - Use a MySQL client to connect to your database and run the necessary commands to create tables and populate them with data.

5. Ensure that your CGI scripts have the correct permissions:
   ```bash
   chmod +x /path/to/CGI-Executables/*.cgi
   ```

## Usage
- Access the application via a web browser using:
  ```plaintext
  http://localhost/index.html
  ```
- Enter an organism name or DNA sequence in the search fields to retrieve results.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Jana Alghoraibi  
Year: 2021
