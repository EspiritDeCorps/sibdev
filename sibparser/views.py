from .models import *
from django.views import generic
import datetime

class IndexView(generic.ListView):
    template_name = "sibparser/index.html"
    context_object_name = 'sites_list'

    def get_queryset(self):
        return self.tagsList(ParsedSite.objects.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["successList"] = self.successfulSites(ParsedSite.objects.all())
        return context

    def successfulSites(self, sites):
        result = []
        for site in sites:
            date = "<Дата " + datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S") + ">: "
            if site.successfully:
                result.append(date + str(site.site) + " успешно обработан")
            else:
                result.append(date + str(site.site) + " Не удалось обработать")
        return result

    def tagsList(self, sites):
        result = []
        for site in sites:
            if site.successfully:
                title = "Title: " + site.title if site.title else "Title: Не обнаружено "
                h1 = "h1: " + site.h1 if site.h1 else "h1: Не обнаружено "
                charset = "Charset: " + site.encoding if site.encoding else "Charset: Не обнаружено "


                result.append(str(site.site) + "-" + title + h1 + charset)

        return result

