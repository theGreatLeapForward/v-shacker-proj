# v-shacker-proj
thing


how to run the code locally:
1. Download the code in testsite1 (nothing else matters)
2. Install django and Pillow with pip
3. cd into testsite1 in a terminal window
4. set up the database (currently running on sqlile but in the process of moving to postgres)
by running the following commands:
  python manage.py makemigrations notinator
  python manage.py migrate notinator
  
If everything is set up correctly (and I didn't forget a step here):
  run the command: python manage.py runserver 
  go to 127.0.0.1:8000 in a search engine or click the link that appears in the termianl to view the website!
