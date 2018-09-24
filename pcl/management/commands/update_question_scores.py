from django.core.management.base import BaseCommand, CommandError


from pcl.models import Procedure, Question, Vote, ProcedureQuestionScore

from django.db import connection, transaction



def tally_score_for_procedure_and_question_id( pid, qid ):
    res = 100
    # print c
    votes = Vote.objects.filter( question_id=qid, procedure_id=pid ).all()
    
    for v in votes:
        res += v.val
    
    return res






class Command(BaseCommand):
    args = 'none...'
    help = 'recalc scores of questions'

    def handle(self, *args, **options):


        procedures = Procedure.objects.all()
        
        for p in procedures:
            
            votes = []
            
            for q in p.questions.all():
        
                c =  Vote.objects.filter( question=q, procedure=p ).count()
                # print q
                score = tally_score_for_procedure_and_question_id( p.id, q.id )
                
                print score

                s = ProcedureQuestionScore.objects.get( question_id=q.id, 
                                                        procedure_id=p.id )
        
                s.score = score
                s.save()
                
                print "updated " + str( s )
   
        """
        
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



"""