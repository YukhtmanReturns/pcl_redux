from django.core.management.base import BaseCommand, CommandError


from pcl.models import Question, Tag

from django.db import connection, transaction




class Command(BaseCommand):
    args = 'none...'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):


        qs = Question.objects.all()
        
        update_count = 0
        
        
        for q in qs:
            
            tags = q.tags.all()
            
            txt = ""
           
            for t in tags:
                txt += t.label
                txt += " "
                
            #
            #print "\n"    
        
            q.tags_txt = q.label + " " + txt
            q.save()
            
            #print txt
            # print q.label
            print "."
            update_count += 1

        
        

        cursor = connection.cursor()

        cursor.execute( "UPDATE pcl_question SET tsvec=to_tsvector( tags_txt )" )
        transaction.commit_unless_managed()

        print "Updated " + `update_count` + " questions."
