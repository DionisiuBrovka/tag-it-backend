from django.contrib import admin
from .models import *

admin.site.register(Art)
admin.site.register(ArtCoords)
admin.site.register(ArtImage)
admin.site.register(ArtComment)