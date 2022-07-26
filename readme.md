### Overview
- A python application representing a TinyURL like service that maps shorter links to longer links

### Requirements
- Creating and deleting short URLs associated with long URLs
  - Long URLs can be mapped to many short URLs
- Retrieving long URL from short URL
- Tracked statistics on number of times a short URL has been "clicked" i.e. number of times long URL has been retrieved
- Entering custom short URL or letting application randomly generate one while maintaining uniqueness

### Setup Instructions
- Create a new python virtual environment in the unzipped directory containing the files, i.e. on Windows `py -m venv venv` 
- Activate the virtual env by running `activate` from the `venv` bin or Scripts directory
- Install requirements.txt in the activated virtualenv using `pip install -r requirements.txt`
- Run the application `python main.py`