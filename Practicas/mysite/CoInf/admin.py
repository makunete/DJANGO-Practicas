from django.contrib import admin

# Register your models here.
from .models import Departaments

admin.site.register(Departaments)

from .models import Usuaris

admin.site.register(Usuaris)

from .models import Incidencies

admin.site.register(Incidencies)

from .models import Compres

admin.site.register(Compres)

from .models import Material

admin.site.register(Material)
