from django.contrib import admin

from .models import MahallaModel, TumanModel, ViloyatModel, YearModel, ChoiceModel


admin.site.register(MahallaModel)
admin.site.register(TumanModel)
admin.site.register(ViloyatModel)
admin.site.register(YearModel)
admin.site.register(ChoiceModel)
