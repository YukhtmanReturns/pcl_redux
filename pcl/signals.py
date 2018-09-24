from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from pcl.models import ForumTopic, ForumArea, Procedure

import pprint

    

'''
@receiver(pre_save,   sender=ForumTopic)
def topic_pre_changed(instance, **kwargs):
    
    # update topic stats    
    topic = instance
    topic.forum_url = topic.create_absolute_forum_url()
#    topic.save()




@receiver(post_save,   sender=Procedure)
def procedure_pre_changed(instance, **kwargs):
    
    proc = instance
    # update forum URL
    proc.forum_url = proc.create_absolute_forum_url()
#    proc.save()
'''
















@receiver(post_save,   sender=ForumTopic)
@receiver(post_delete, sender=ForumTopic)
def topic_post_changed(instance, **kwargs):
    
    # update topic stats    
    topic = instance
    proc  = topic.procedure
    
    pprint.pprint( proc )
    
    proc.count_topics = proc.topics.count()
    proc.save()
    
    
    # update the topics per area count as well
    area = proc.area
    
    area.count_topics = ForumTopic.objects.filter(procedure__area=area).count()
    
    pprint.pprint( area )
        
    area.save()


    topic.forum_url = topic.create_absolute_forum_url()
    # topic.save()




@receiver(post_save,   sender=Procedure)
@receiver(post_delete, sender=Procedure)
def procedure_post_changed(instance, **kwargs):
    
    # got to update all in case a proc moves from area to area    
    areas = ForumArea.objects.all()
    
    for area in areas:

        area.count_procs  = area.procedures.filter( active=True ).count()
        area.count_topics = ForumTopic.objects.filter( procedure__area = area, procedure__active=True ).count()
        
        area.save()

    proc = instance
    proc.forum_url = proc.create_absolute_forum_url()
    # proc.save()



