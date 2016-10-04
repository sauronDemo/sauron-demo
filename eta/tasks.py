from celery import task, periodic_task
from django.test import TestCase

@task
def run_etas():
	# adding my run_etas function
	pass

@periodic_task
def run_eta():
	pass
