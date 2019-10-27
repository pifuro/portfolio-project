from django.db import models

# Create blog models
#tittle, pub_date, body, image
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#add the blog app to the settings

#create a migration

# migrate

#add to the admin
