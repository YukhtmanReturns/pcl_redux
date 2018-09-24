from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



from pcl.models import * 

# Tag, Procedure, ProcedureAdmin, Question, QuestionAdmin, Contact, ForumArea


admin.site.register( Tag )
admin.site.register( Procedure, ProcedureAdmin )
admin.site.register( Question, QuestionAdmin ) 
admin.site.register( Contact )

admin.site.register( ForumArea )
admin.site.register( ForumTopic )
admin.site.register( ForumPost )

admin.site.register( User )


handler404 = 'pcl.views.custom_404'


urlpatterns = patterns('',
    # Examples:

    url(r'^', include('pcl.urls', namespace="pcl")),
    url(r'^pcl-admin/', include(admin.site.urls)),    
)
