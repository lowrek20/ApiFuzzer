# API Fuzzer

This project is a Python-based API fuzzer that sends HTTP GET requests to a specified API endpoint using a list of words. The fuzzer reads words from standard input and appends each word to the API endpoint URL to discover potential valid or interesting endpoints. It handles HTTP errors and non-JSON responses, making it a useful tool for testing and exploring APIs.

## Features
- **Wordlist Input:** Reads a list of words from a file or standard input to be used as URL parameters.
- **API Fuzzing:** Sends HTTP GET requests to the target API endpoint, appending each word to the URL.
- **Error Handling:** Handles HTTP errors (like 404) and non-JSON responses gracefully.
- **Customizable:** Easily modify the wordlist and API endpoint to fuzz different APIs.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries:
  - `requests`: A simple, yet powerful HTTP library for Python.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/api-fuzzer.git
   cd api-fuzzer

    Install the required library:

    bash

    pip install requests

Usage

    Prepare a wordlist in a text file, with each word on a new line. For example, save the following words in a file named wordlist.txt:

    bash

login
admin
dashboard
api
test

Run the script with the wordlist as input:

bash

    python api_fuzzer.py < wordlist.txt

    The script will send a GET request for each word appended to the base URL and output the results.

Example

If your base API endpoint is https://example.com/api, and the word admin is in your wordlist, the script will make a request to:

arduino

https://example.com/api/admin

    Sample Output:

    vbnet

    URL: https://example.com/api/admin
    Status Code: 200
    Response: {"status": "success", "message": "Admin panel accessed"}

Error Handling

    If a URL returns a 404 Not Found, the script will skip to the next word and continue fuzzing.
    If the response is not in JSON format, the script will output the raw text for further analysis.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any issues or questions, please open an issue on this repository or contact me at [your-email@example.com].
Disclaimer

This project is for educational and testing purposes. Unauthorized use of this tool against any system or API without permission is illegal and unethical. Use this tool responsibly.
