# FLOW
1. Access the website
2. Find and select File Type
3. Find and select Date
4. Download File

# HOW TO USE
1. Open terminal on the directory and run: `pip install -r requirements.txt`
2. You can config some constants in .env file
2. Run: `python3 main.py` to run by default configurations (try using python instead of python3 if it fails)
3. Run: `python3 main.py --help` for advanced scraping (file/time config)
4. The result is logged in scrape.log files, check it!

# WHAT I HAVE DONE
1. Create job to download files daily from website
2. Can download historical files and different file types
2. Can run in command line with options/config file
3. Logging has implemented

# SOME PROBLEMS
1. Download only recent files but not older files
2. Redownloading manually for missed files