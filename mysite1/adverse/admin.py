from django.contrib import admin
from django.contrib.admin import RelatedFieldListFilter
import csv
from django.utils.encoding import smart_str
from .models import Question
from django.http import HttpResponse
from django.utils.html import format_html
#export_csv.short_description = u"Export CSV"
class QuestionAdmin(admin.ModelAdmin):
        def export_csv(modeladmin, request, queryset):
    
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
            writer = csv.writer(response, csv.excel)
            response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
            writer.writerow([
               smart_str(u"CRN"),
               smart_str(u"ulb"),
               smart_str(u"Status"),
               smart_str(u"Type"),
               smart_str(u"Registered On"),
               smart_str(u"Completed On"),
            ])
            for obj in queryset:
             writer.writerow([
               smart_str(obj.crn),
               smart_str(obj.ulbname),
               smart_str(obj.status),
               smart_str(obj.typee),
               smart_str(obj.frm),
               smart_str(obj.to),
               ])
            return response
        actions = [export_csv]
        list_display=('crn','distr','typee','ulbname','status','frm','to')
        search_fields=('crn','ulbname')
        list_filter = ('distr','status','typee')
admin.site.register(Question,QuestionAdmin)
admin.site.site_header = 'AP State Command & Communication Centre (MA&UD) '

    
