#!/usr/bin/env python3

"""
auto.cgi
Author: Jana Alghoraibi
Year: 2021

This script is licensed under the MIT License.
See the LICENSE file for more details.

Description: Handles autocomplete functionality.
"""

import cgi
import json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    
    form = cgi.FieldStorage()
    term = form.getvalue('term')  # Ensure we're using 'term' to match request

    if not term:
        print(json.dumps([]))
        return

    try:
        # Database connection
        conn = mysql.connector.connect(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'), 
            host = os.getenv('DB_PASSWORD'), 
            database= os.getenv('DB_NAME'), 
        )

        cursor = conn.cursor()

        # Query for autocomplete suggestions
        qry = """
              SELECT DISTINCT organism_name 
                FROM mirtrons 
               WHERE organism_name LIKE %s 
               LIMIT 10
        """
        cursor.execute(qry, ('%' + term + '%', ))

        # Use a set to avoid duplicates
        suggestions = set()

        for (organism_name,) in cursor:
            suggestions.add(organism_name)  # Add to set, naturally eliminates duplicates

        # Transform set back to sorted list (optional)
        results = [{'label': name, 'value': name} for name in sorted(suggestions)]

        print(json.dumps(results))

    except mysql.connector.Error as err:
        print(json.dumps({"error": f"Database connection error: {str(err)}"}))
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
