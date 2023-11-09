from django.contrib import admin

# Register your models here.

from .models import Poll
from .models import Option
from .models import Response
from django.db.models import Count

class OptionInLine(admin.TabularInline):
    model = Option
    extra = 0
    classes = ('collapse',)

class ResponseInLine(admin.TabularInline):
    model = Response
    extra = 0
    classes = ('collapse',)

class PollAdmin(admin.ModelAdmin):
    list_display = ['question','active_until','status','response_count']
    list_filter = ['status']
    search_fields = ['question']
    inlines = [OptionInLine,ResponseInLine,]

    def response_count(self, obj):
        return obj.option_set.aggregate(response_count=Count('response')).get('response_count', 0)  
        #we use .aggregate(response_count=Count('response')): to count respond
    
    pass

class OptionAdmin(admin.ModelAdmin):
    inlines = [ResponseInLine,]
    pass

class ResponseAdmin(admin.ModelAdmin):
    pass


admin.site.site_header="This is our Poll Project"

admin.site.register(Poll, PollAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Response, ResponseAdmin)
