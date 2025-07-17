from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
import pandas as pd


def index(request: HttpRequest):
  return render(request, "basic/index.html")


def snippet(request):
  return render(request, "basic/snippet.html")


def contacts(request):
  return render(request, "contacts/index.html")


"""
def (request: HttpRequest):
  all_contacts = pd.read_csv("htmxtutorial/static/contacts.csv")
  search_string = request.POST["search"]
  is_in_first_name = all_contacts.loc[:, "first_name"].str.contains(search_string)
  is_in_last_name = all_contacts.loc[:, "last_name"].str.contains(search_string)
  is_in_email = all_contacts.loc[:, "email"].str.contains(search_string)
  contacts_found = all_contacts.loc[is_in_first_name | is_in_last_name | is_in_email, :]
  contacts_found = contacts_found.to_dict("records")
  return render(request, "contacts/table_template.html", {"contacts_found": contacts_found})
"""