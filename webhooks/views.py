import json
from django.http import HttpResponse

def getrequest(request):
	if request.method == "GET":
		return HttpResponse('<strong>m00</strong>')

	if request.method == "POST":
		json_data = None
		
		for key in request.POST:
			json_data = key
		json_data = json.loads(json_data)
		event = json_data['hook']
		
		#if event == "topic.created":
			#print "Topic has been created"
			#print ""
		print request.POST
		
		return HttpResponse('<strong>heh</strong>')