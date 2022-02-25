### SETUP STEPS
1. Install required packages using:
    ~~~   
    pip install -r requirements.txt
    ~~~
2. Obtain a Google YouTube API key from the following link: https://console.developers.google.com/
    * You must first create a new project
    * Then, search for "YouTube Data API V3" in the search box
    * Lastly, enable the API then click "Create Credentials" to create an API key
    * Simple tutorial here: https://blog.hubspot.com/website/how-to-get-youtube-api-key
3. Create a file in the root project directory called ".env"
4. Paste the following into the .env file with your API key included: 
    ~~~
    YOUTUBE_API_KEY=REPLACE_THIS_WITH_API_KEY
    ~~~
   
### RUNNING THE SERVER PROGRAM
1. Run the "microservice_server.py" file located in the root project directory

### USING A CLIENT PROGRAM
1. Create a connection to the server:
    ~~~
    conn = rpyc.connect("localhost", 18861)
    ~~~
   Replace port number with the port number the server is running on
2. Use the following code to search for a specific exercise and number of results:
    ~~~
    c.root.exposed_youtube_search("bicep curls", 3)
    ~~~
   The above code will return a list of URL links to the top 3 YouTube results when searching for videos
   on "bicep curls". The first argument is the search query. The second argument specifies the max number 
   of URL links that will be returned.