from django.shortcuts import render
from django.views import generic
from .models import MahallaModel, TumanModel, ViloyatModel, YearModel, ChoiceModel


class YearDetailView(generic.DetailView):
    template_name = "regions/year_detail.html"
    model = YearModel
    context_object_name = "year"

    def get_context_data(self, **kwargs):
        context = super(YearDetailView, self).get_context_data(**kwargs)
        context["mahallalar"] = MahallaModel.objects.all()
        context["years"] = YearModel.objects.all()
        return context


class MahallaDetailView(generic.DetailView):
    template_name = "regions/mahalla_detail.html"
    model = MahallaModel
    context_object_name = "mahalla"

    def get_context_data(self, *args, **kwargs):
        context = super(MahallaDetailView, self).get_context_data(*args, **kwargs)
        context["years"] = YearModel.objects.all()
        context["mahallalar"] = MahallaModel.objects.all()
        context["tumanlar"] = TumanModel.objects.all()
        return context


class TumanDetailView(generic.DetailView):
    template_name = "regions/tuman_detail.html"
    model = TumanModel
    context_object_name = "tuman"

    def get_context_data(self, *args, **kwargs):
        context = super(TumanDetailView, self).get_context_data(*args, **kwargs)
        context["mahallalar"] = MahallaModel.objects.all()
        context["tumanlar"] = TumanModel.objects.all()
        context["viloyatlar"] = ViloyatModel.objects.all()
        return context


class ViloyatListView(generic.ListView):
    template_name = "regions/home.html"
    model = ViloyatModel
    context_object_name = "viloyatlar"


class ViloyatDetailView(generic.DetailView):
    template_name = "regions/viloyat_detail.html"
    model = ViloyatModel
    context_object_name = "viloyat"

    def get_context_data(self, *args, **kwargs):
        context = super(ViloyatDetailView, self).get_context_data(*args, **kwargs)
        context["tumanlar"] = TumanModel.objects.all()
        context["viloyatlar"] = ViloyatModel.objects.all()
        return context
