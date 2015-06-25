from django.contrib import admin
from models import Event, Peer

class EventAdmin(admin.ModelAdmin):
    # exclude = ('author',)
    list_display = ('name', 'date')
    search_fields = ('name', 'date')
    fields = ('name', 'date', 'create_date', 'author')


    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(EventAdmin, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
    #         return False
    #     return True

    # def get_queryset(self, request):
    #     if request.user.is_superuser:
    #         return Event.objects.all()
    #     return Evernt.objects.filter(author=request.user)

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.author = request.user
    #     obj.save()

class PeerAdmin(admin.ModelAdmin):
    # exclude = ('author',)
    list_display = ('name', 'favorite_contact')
    search_fields = ['^name']
    fields = ('name', 'event', 'favorite_contact', 'email', 'telephone_number', 'notes')

    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(PeerAdmin, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
    #         return False
    #     return True

    # def get_queryset(self, request):
    #     if request.user.is_superuser:
    #         return Peer.objects.all()
    #     return Peer.objects.filter(author=request.user)

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.author = request.user
    #     obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(Peer, PeerAdmin)