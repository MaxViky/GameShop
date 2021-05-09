from django.contrib import admin

from gameApp.models import *

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(GameLabel)
admin.site.register(Tagged)
admin.site.register(GameShots)
admin.site.register(Reviews)
admin.site.register(Cart)