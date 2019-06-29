from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class CITY(models.Model):
    city_name = models.CharField( max_length=200 )
    longitude = models.CharField(max_length=30, blank=True)
    latitude = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='allImages/')

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'

    '''def __str__(self):
        return str(self.pk) + "," + self.city_name + "," + self.longitude + "," \
               + self.latitude + "," + self.image'''



class HOTEL(models.Model):
    hotel_name = models.CharField(max_length=200)
    image = models.ImageField( upload_to='allImages/' )
    longitude = models.CharField(max_length=30, blank=True)
    latitude = models.CharField(max_length=30, blank=True)
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))
    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.hotel_name + "," + self.image + "," \
               + self.longitude + "," + self.latitude + "," + str(self.cityID)'''


class USER(models.Model):
    Email = models.EmailField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, blank=True)
    Password = models.CharField(max_length=50)
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE, default=3 )
    Address = models.CharField(max_length=200)
    Contact = models.CharField(max_length=50)
    image = models.ImageField( upload_to='allImages/' , default='noimage.jpg' )
    About = models.CharField(max_length=50, blank=True)
    Gender = models.CharField(max_length=50)

    #def get_absolute_url(self):

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.Email + "," + self.FirstName +"," + self.LastName + "," \
               + self.Password+ "," + "," + str(self.cityID) + "," + self.Address+ "," +  self.Contact+ "," \
               + self.Picture+ "," + self.About+ "," + self.Gender'''



class GROUP(models.Model):
    GroupName = models.CharField(max_length=100)
    '''def __str__(self):
        return str(self.pk) + "," + self.GroupName'''


class GUIDE(models.Model):
    Email = models.EmailField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, blank=True)
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Contact = models.CharField(max_length=50)
    image = models.ImageField( upload_to='allImages/' , default='noimage.jpg' )
    About = models.CharField(max_length=50, blank=True)
    Gender = models.CharField(max_length=50)

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.Email + "," + self.FirstName + "," + self.LastName + "," \
               + self.Password + "," + self.Address + "," + self.Contact + "," \
               + self.Picture + "," + self.About + "," + self.Gender'''



class BLOG(models.Model):
    blogCaption = models.CharField(max_length=200)
    blogPostDate = models.DateField( auto_now_add=True )
    blogData = models.CharField(max_length=2000)
    guideID = models.ForeignKey(GUIDE, on_delete=models.CASCADE, null=True)
    userID = models.ForeignKey(USER, on_delete=models.CASCADE, null=True)
    image = models.ImageField( upload_to='allImages/', default='noimage.jpg' )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.blogCaption + "," + str(self.blogPostDate)+","+self.blogData+","\
               +str(self.guideID)+","+str(self.userID) + "," + self.images'''




class TOURISTSPOT(models.Model):
    spotName = models.CharField(max_length=75)
    spotInfo = models.CharField(max_length=2000)
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='allImages/')
    longitude = models.CharField(max_length=30, blank=True)
    latitude = models.CharField(max_length=30, blank=True)
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.spotName + "," + self.spotInfo + "," + str(self.cityID) + "," \
               + self.longitude + "," + self.latitude + "," + self.touristSpotImages'''



class ACTIVITY(models.Model):
    activityName = models.CharField(max_length=50)
    activityCost = models.IntegerField(default= -2147483647)
    image = models.ImageField( upload_to='allImages/' )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'

    '''def __str__(self):
        return str(self.pk) + "," + self.activityName + "," + str(self.activityCost) + "," + self.activityImages'''



class PREFERENCE(models.Model):
    preferenceName = models.CharField(max_length=50)
    image = models.ImageField( upload_to='allImages/' )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))

    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + self.preferenceName + "," + self.preferenceImages'''



class TOURINFO(models.Model):

    groupID = models.ForeignKey(GROUP, on_delete=models.CASCADE)
    userID = models.ForeignKey(USER, on_delete=models.CASCADE)
    guideID = models.ForeignKey(GUIDE, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    dailyTravelTime = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    finished = models.IntegerField( default=0 )
    '''def __str__(self):
        return str(self.pk) + "," + str(self.groupID) + "," + str(self.userID)+","\
               +str(self.guideID)+","+str(self.startDate)+","+str(self.endDate)++","\
               +str(self.dailyTravelTime)+","+str(self.description) + "," + str(self.finished)'''





class TOURINFOGROUP(models.Model):
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    groupID = models.ForeignKey(GROUP, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.groupID)'''


class TOURINFOACTIVITY(models.Model):
    activityID = models.ForeignKey(ACTIVITY, on_delete=models.CASCADE)
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.activityID)'''



class TOURINFOTOURISTSPOT(models.Model):
    spotID = models.ForeignKey(TOURISTSPOT, on_delete=models.CASCADE)
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.spotID)'''


class USERGROUP(models.Model):
    userID = models.ForeignKey(USER, on_delete=models.CASCADE)
    groupID = models.ForeignKey(GROUP, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.userID) + "," + str(self.groupID)'''


class GUIDETOURINFO(models.Model):
    guideID = models.ForeignKey(GUIDE, on_delete=models.CASCADE)
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.guideID) + "," + str(self.tourID)'''





class CITYTOURINFO(models.Model):
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE)
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.cityID)'''



class PREFERENCETOURINFO(models.Model):
    preferenceID = models.ForeignKey(PREFERENCE, on_delete=models.CASCADE)
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.preferenceID)'''


class CITYGUIDE(models.Model):
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE)
    guideID = models.ForeignKey(GUIDE, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.cityID) + "," + str(self.guideID)'''



class SPOTACTIVITY(models.Model):
    activityID = models.ForeignKey(ACTIVITY, on_delete=models.CASCADE)
    spotID = models.ForeignKey(TOURISTSPOT, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    image = models.ImageField( upload_to='allImages/' )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))
    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + str(self.spotID) + "," + str(self.activityID) + "," \
               + self.description + "," + self.image'''

class TOURISTSPOTPREFERENCE(models.Model):
    preferenceID = models.ForeignKey(PREFERENCE, on_delete=models.CASCADE)
    spotID = models.ForeignKey(TOURISTSPOT, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    image = models.ImageField( upload_to='allImages/' )
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="50" />'.format(str(self.image.url)))
    image_tag.short_description = 'Image'
    '''def __str__(self):
        return str(self.pk) + "," + str(self.spotID) + "," + str(self.preferenceID) + "," +\
               self.description + "," + self.image'''


class CITYPREFERENCE(models.Model):
    cityID = models.ForeignKey(CITY, on_delete=models.CASCADE)
    preferenceID = models.ForeignKey(PREFERENCE, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.cityID) + "," \
               + str(self.preferenceID)'''



class TOURINFOPREFERENCE(models.Model):
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    preferenceID = models.ForeignKey(PREFERENCE, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.preferenceID)'''


class HOTELTOURINFO(models.Model):
    tourID = models.ForeignKey(TOURINFO, on_delete=models.CASCADE)
    hotelID = models.ForeignKey(HOTEL, on_delete=models.CASCADE)
    '''def __str__(self):
        return str(self.pk) + "," + str(self.tourID) + "," + str(self.hotelID)'''


