
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import  all
from django.template import loader


def courses (request):
    ac=all.objects.all()
    template=loader.get_template('Tech/courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context,request))
def detail(request, course_id):
    course=get_object_or_404(all, pk=course_id)
    return render(request, 'Tech/detail.html', {'course':course})
def yourchoice(request, course_id):
    course=get_object_or_404(all, pk=course_id)
    try:
        selected_ct=course.details_set.get(pk=request.POST['choice'])
    except (KeyError, all.DoesNotExist):
        return render(request, 'Tech/detail.html',{
            'course':course,
            'error_message':"Select a Valid Option"
        })
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'Tech/detail.html', {'course':course})