#  TODO

#  ANALISAR SE É NECESSARIO 


# import bugsnag
# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
# from project.apps.accounts.models import Participation 


# @periodic_task(
#     run_every=(crontab(hour=7, minute=30, day_of_month=1)), # EVERY DAY 
#     name="clean_annonymouslogs",
#     ignore_result=True
# )

# def clean_annonymouslogs():
#     try:
#         AnonymousAccessLog.objects.all().delete()
    
#     except Exception as e:
#         bugsnag.notify(e)
        