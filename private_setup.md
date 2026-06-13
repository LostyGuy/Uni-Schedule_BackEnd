# How to setup folder with confidential data

### Structure

 - backend/
    - Folder (eg. 'hidden')
        - database_url.py
        - jwt_settings.py
        - pass_hashing.py

<hr>

<h4>.gitignore</h4>
add this line without # (comment)

```markdown
backend/hidden/
```

<hr>

<h4>database_url.py</h4>
Supabase provides lots of ways to connect to their service. Check them for yourself. Here is one of them:

```python
DATABASE_URL = "postgresql://postgres.[SUPABASE-PROJECT-ID]:[YOUR-PASSWORD]@aws-1-eu-west-2.pooler.supabasecom:5432/postgres"
```

<hr>

<h4>jwt_settings.py</h4>

```python
import datetime as dt

SECRET_KEY = "your-super-secret-key"
# example: jwt library provides variety of algorithms like HS256 and HS512 
ALGORITHM = "HS512"
# example: token lifetime set to 1 hour
TOKEN_LIFESPAN = dt.timedelta(hours=1)
```

<hr>

<h4>pass_hashing.py</h4>

```python
#
algorithm = ""

# Salt can be a letter, number oraz enourmously long set of characters
hash_salt = "anything" 

# You'll have to hash some values manually and put them here
# Example:
hashed_answer_1 = "2ed0ce1dfcac0121b78b729e7532a07095a4c4db28005c88d78ea24fa93cd65ea331d471c838397491753e2b8803cbf7bb997f3b8f47ad4effa13fcbd58f77b9"
hashed_answer_2 = "983d43ddff6da90f6a5d3b6172446a1ffe228b803fe64fdd5dcfab5646078a896851fe82f623c9d6e5654b3d2f363a04ec17cfb62b607437a9c7c132d511e522"
hashed_answer_3 = "ff1f9cb2a3731732c2e5cdc7fb601b450b754d92bb8eef370a523fb40ec0805eca24e304320daa177ff11b3e3d941c72d0b4f28776759593b51b125fb6533a5d"
```