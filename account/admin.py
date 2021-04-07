from django.contrib import admin

from account.models import contact_us,roomtype,book_room

admin.site.register(contact_us)
admin.site.register(roomtype)
admin.site.register(book_room)