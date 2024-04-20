from django.contrib import admin

from somesite.models import User, Orderer, Contractor


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['uid', 'username', 'first_name', 'last_name', 'email']
    list_display = ['uid', 'username', 'first_name', 'last_name', 'email']
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Orderer)
class OrdererAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'experience', 'created_at', 'updated_at')
    search_fields = (
        'user__first_name', 'user__last_name', 'user__email', 'slug')