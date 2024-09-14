
/ search.js
// Author: Jana Alghoraibi
// Year: 2021
// 
// This script is licensed under the MIT License.
// See the LICENSE file for more details.
// 
// Description: Handles search form submission and result processing for the Mirtrons web application.


$(document).ready(function() {
    // Function to execute our search via an AJAX call
    function runSearch(term, type) {
        // Hide and clear previous results, if any
        $('#results').hide();
        $('tbody').empty();

        let dataToSend;
        if (type === 'term') {
            // Prepare data to send based on term
            dataToSend = $('#miRna_search').serialize(); // for search_term
        } else if (type === 'sequence') {
            // Prepare data to send based on sequence
            dataToSend = $('#seq_search').serialize(); // for search_seq
        }

        // Make AJAX request to match.cgi for search_term or search_seq
        $.ajax({
            url: 'cgi-bin/match.cgi',  // Ensure this matches the correct path
            dataType: 'json',
            data: dataToSend,
            success: function(data) {
                processJSON(data);
            },
            error: function() {
                alert('Error fetching search results. Please try again.');
            }
        });
    }

    // Function to handle form submission for organism name search
    $('#miRna_search').submit(function(event) {
        event.preventDefault();  // Prevent default form submission
        const searchTerm = $('#search_term').val();
        if (searchTerm) {
            runSearch(searchTerm, 'term');  // Run search on organism name
        } else {
            alert('Please enter a term to search.');
        }
    });

    // Function to handle form submission for DNA sequence search
    $('#seq_search').submit(function(event) {
        event.preventDefault();  // Prevent default form submission
        const searchSeq = $('#search_seq').val();
        if (searchSeq) {
            runSearch(searchSeq, 'sequence');  // Run search on sequence
        } else {
            alert('Please enter a sequence to search.');
        }
    });

    // Function to process JSON responses from the server
    function processJSON(data) {
        // Update match count display
        $('#match_count').text(data.match_count);

        // Clear previous results
        $('tbody').empty();

        // If there are any matches, process them
        if (data.matches.length > 0) {
            // Iterate over each match and add a row to the result table
            $.each(data.matches, function(i, item) {
                const row = $('<tr/>');
                row.append($('<td/>').text(item.organism_id));
                row.append($('<td/>').text(item.organism_name));
                row.append($('<td/>').text(item.mirtron_name));
                row.append($('<td/>').text(item.type));
                row.append($('<td/>').text(item.sequence));
                $('tbody').append(row);
            });

            // Show the results section
            $('#results').show();
        } else {
            // Handle case when no matches are found
            $('#results').hide();
            alert('No matches found.');
        }
    }

    // Autocomplete Setup for organism name
    $('#search_term').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: 'cgi-bin/auto.cgi', // Make sure this points to your autocomplete script
                dataType: 'json',
                data: { term: request.term }, // Send 'term' parameter to the CGI script
                success: function(data) {
                    response(data); // Send the data back to the autocomplete widget
                },
                error: function() {
                    response([]); // Return an empty array on error
                }
            });
        },
        minLength: 2, // Minimum length of input to trigger the autocomplete
        select: function(event, ui) {
            // This event is triggered when an item is selected from the autocomplete list
            $('#search_term').val(ui.item.label); // Set the input field to the selected item's label
            runSearch(ui.item.label, 'term'); // Optionally, trigger a search immediately on selection
        }
    });
});
