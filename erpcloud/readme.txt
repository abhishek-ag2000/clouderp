argon2 = pip install django[argon2]

bcrypt = pip install bcrypt

pillow = pip install pillow

For CSS to work we need to mention the STATICFILES_DIRS and STATIC_URL in the settings.py file
for example in our project we did:

STATIC_URL = '/static/'

STATICFILES_DIRS =(

    os.path.join(BASE_DIR, 'static'),

) 


