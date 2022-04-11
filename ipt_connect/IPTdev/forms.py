from django import forms
from django.http import JsonResponse
from django.utils.encoding import smart_text

from .models import Participant


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         exclude = ('country',)

# class RegisterForm(forms.Form):
#
#    name = forms.CharField(max_length=20)
#
#    surname = forms.CharField(max_length=20)
#
#    email = forms.EmailField(label="Email address")
#
#    veteran = forms.BooleanField(help_text="Have you already participated in the tournament?", required=True)


class UploadForm(forms.Form):
    csvfile = forms.FileField(label="Select a CSV file:")


def member_for_team(request):
    res = []
    if request.user.is_authenticated() and request.GET and "team_id" in request.GET:
        objs = Participant.objects.filter(team=request.GET["team_id"])
        res.extend({"id": o.id, "name": smart_text(o)} for o in objs)
    return JsonResponse({"res": res})
