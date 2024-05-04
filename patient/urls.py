from rest_framework import routers
from .api import PacienteViewSet, ProfesionalViewSet, RecepcionistaViewSet , InformeViewSet, HistoriaClinicaViewSet, TurnoViewSet

router = routers.DefaultRouter()

router.register('api/pacientes', PacienteViewSet, 'pacientes')
router.register('api/profesionales', ProfesionalViewSet, 'profesionales')
router.register('api/recepcionistas', RecepcionistaViewSet, 'recepcionistas')
router.register('api/informes', InformeViewSet, 'informes')
router.register('api/historias-clinicas', HistoriaClinicaViewSet, 'historia-clinica')
router.register('api/turnos', TurnoViewSet, 'turnos')

urlpatterns = router.urls