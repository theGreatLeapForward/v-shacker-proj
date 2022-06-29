# v-shacker-proj
thing


how to run the code locally:

0. Install PostgreSQL
1. Download the code in testsite1 (nothing else matters)
2. Install dependencies in requirements.txt with pip
3. cd into testsite1 in a terminal window
4. set up the database postgres
  a. download pgAdmin and set up a database 
  b. set up environment variables PGPASSFILE and PGSERVICEFILE
  
    PGPASSFILE should point to a .my_pgpass file containing localhost:5432:(database name):(user of db):(password of db user)
    PGSERVICEFILE should point to a .pg_service.conf file containing:
    
      [my servive]
      host=localhost
      
      user=(user of db)
      
      dbname=(name of db)
      
      port=5432
      
      
      more info can be found here: https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes

  c. run the following commands:
    python manage.py makemigrations notinator
    python manage.py migrate notinator
  
If everything is set up correctly (and I didn't forget a step here):
  run the command: python manage.py runserver 
  go to 127.0.0.1:8000 in a search engine or click the link that appears in the termianl to view the website!
