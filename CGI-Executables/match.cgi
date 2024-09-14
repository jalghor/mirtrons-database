#!/usr/bin/env python3

"""
match.cgi
Author: Jana Alghoraibi
Year: 2022

This script is licensed under the MIT License.
See the LICENSE file for more details.

Description: Handles search functionality for organism names and sequences.
"""

import cgi
import json
import os
import mysql.connector
import sys

def main():
    print("Content-Type: application/json\n\n")

    # Get form data
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')  # For searching by organism name
    term2 = form.getvalue('search_seq')   # For searching by sequence

    # Logging inputs for debugging
    print("Received search_term:", term, file=sys.stderr)
    print("Received search_seq:", term2, file=sys.stderr)

    # Initialize the results structure
    results = {'match_count': 0, 'matches': []}

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'), 
            host = os.getenv('DB_PASSWORD'), 
            database= os.getenv('DB_NAME'), 
        )
        cursor = conn.cursor()

        # Check if we have a search term provided
        if term:
            qry = """
                SELECT organism_id, organism_name, mirtron_name, type, sequence
                FROM mirtrons
                WHERE organism_name LIKE %s
            """
            cursor.execute(qry, ('%' + str(term) + '%', ))
            
        elif term2:
            qry = """
                SELECT organism_id, organism_name, mirtron_name, type, sequence
                FROM mirtrons
                WHERE sequence LIKE %s
            """
            cursor.execute(qry, ('%' + str(term2) + '%', ))

        # Process the cursor results
        for (organism_id, organism_name, mirtron_name, type, sequence) in cursor:
            results['matches'].append({
                'organism_id': organism_id,
                'organism_name': organism_name,
                'mirtron_name': mirtron_name,
                'type': type,
                'sequence': sequence.decode('utf-8')  # Decode if bytes, otherwise keep as is
            })
            results['match_count'] += 1

    except mysql.connector.Error as err:
        # Returning any database-related errors
        print(json.dumps({"error": f"Database connection error: {str(err)}"}))
        print("Error connecting to database:", str(err), file=sys.stderr)
        return  # Exit on error

    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
    # If no matches were found, indicate this in the response
    if results['match_count'] == 0:
        print(json.dumps({"message": "No matches found.", "match_count": results['match_count'], "matches": []}))
    else:
        # Print the results in JSON format
        print(json.dumps(results))

if __name__ == '__main__':
    main()

