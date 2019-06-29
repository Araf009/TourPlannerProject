from django.contrib import admin
from .models import *
# Register your models here.


class USERAdmin(admin.ModelAdmin):
    list_display = ['id', 'Email', 'FirstName', 'LastName', 'Password', 'cityID',
                    'Address', 'Contact', 'image_tag', 'About', 'Gender']


class GROUPAdmin(admin.ModelAdmin):
    list_display = ['id', 'GroupName']


class CITYAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_name', 'longitude', 'latitude', 'image_tag']


class HOTELAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel_name', 'longitude', 'latitude', 'image_tag', 'cityID']


class GUIDEAdmin(admin.ModelAdmin):
    list_display = ['id','FirstName', 'LastName', 'Contact', 'Email', 'Address', 'image_tag', 'About', 'Gender']


class BLOGAdmin(admin.ModelAdmin):
    list_display = ['id', 'blogCaption', 'blogPostDate', 'blogData', 'guideID', 'userID', 'image_tag']


class PREFERENCEAdmin(admin.ModelAdmin):
    list_display = ['id', 'preferenceName', 'image_tag']


class ACTIVITYAdmin(admin.ModelAdmin):
    list_display = ['id', 'activityName', 'activityCost', 'image_tag']


class TOURISTSPOTAdmin(admin.ModelAdmin):
    list_display = ['id', 'spotName', 'spotInfo', 'cityID', 'longitude', 'latitude','image_tag']


class TOURINFOAdmin(admin.ModelAdmin):
    list_display = ['id', 'groupID', 'userID', 'guideID', 'startDate', 'endDate', 'dailyTravelTime', 'description', 'finished']


admin.site.register(HOTEL, HOTELAdmin)
admin.site.register(CITY, CITYAdmin)
admin.site.register(USER, USERAdmin)
admin.site.register(GROUP, GROUPAdmin)
admin.site.register(GUIDE, GUIDEAdmin)
admin.site.register(TOURISTSPOT, TOURISTSPOTAdmin)
admin.site.register(ACTIVITY, ACTIVITYAdmin)
admin.site.register(PREFERENCE, PREFERENCEAdmin)
admin.site.register(BLOG, BLOGAdmin)
admin.site.register(TOURINFO, TOURINFOAdmin)



class USERGROUPAdmin(admin.ModelAdmin):
    list_display = ['id', 'userID', 'groupID']


class HOTELTOURINFOAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'hotelID']


class CITYGUIDEAdmin(admin.ModelAdmin):
    list_display = ['id', 'cityID', 'guideID']


class GUIDETOURINFOAdmin(admin.ModelAdmin):
    list_display = ['id', 'guideID', 'tourID']


class CITYTOURINFOAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'cityID']


class PREFERENCETOURINFOAdmin(admin.ModelAdmin):
    list_display = ['id','tourID', 'preferenceID']


class TOURINFOTOURISTSPOTAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'spotID']


class CITYPREFERENCEAdmin(admin.ModelAdmin):
    list_display = ['id', 'cityID', 'preferenceID']


class TOURISTSPOTPREFERENCEAdmin(admin.ModelAdmin):
    list_display = ['id', 'spotID', 'preferenceID', 'description', 'image_tag']


class TOURINFOPREFERENCEAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'preferenceID']


class SPOTACTIVITYAdmin(admin.ModelAdmin):
    list_display = ['id', 'spotID', 'activityID', 'description', 'image_tag']


class TOURINFOACTIVITYAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'activityID']


class TOURINFOGROUPAdmin(admin.ModelAdmin):
    list_display = ['id', 'tourID', 'groupID']


admin.site.register(USERGROUP, USERGROUPAdmin)
admin.site.register(HOTELTOURINFO, HOTELTOURINFOAdmin)
admin.site.register(CITYGUIDE, CITYGUIDEAdmin)
admin.site.register(GUIDETOURINFO, GUIDETOURINFOAdmin)
admin.site.register(CITYTOURINFO, CITYTOURINFOAdmin)
admin.site.register(PREFERENCETOURINFO, PREFERENCETOURINFOAdmin)
admin.site.register(TOURINFOTOURISTSPOT, TOURINFOTOURISTSPOTAdmin)
admin.site.register(CITYPREFERENCE, CITYPREFERENCEAdmin)
admin.site.register(TOURISTSPOTPREFERENCE, TOURISTSPOTPREFERENCEAdmin)
admin.site.register(TOURINFOPREFERENCE, TOURINFOPREFERENCEAdmin)
admin.site.register(SPOTACTIVITY, SPOTACTIVITYAdmin)
admin.site.register(TOURINFOACTIVITY, TOURINFOACTIVITYAdmin)
admin.site.register(TOURINFOGROUP, TOURINFOGROUPAdmin)
