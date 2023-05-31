from django.contrib import admin
from .models import Link, Script, Tag, Man, Command, Archivefile


admin.site.register(Tag)
admin.site.register(Script)
admin.site.register(Link)
admin.site.register(Man)
admin.site.register(Command)
admin.site.register(Archivefile)
