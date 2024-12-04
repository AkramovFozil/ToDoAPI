from rest_framework.routers import DefaultRouter
from .views import TodoView

router = DefaultRouter()
router.register(r'todo', TodoView)

urlpatterns = router.urls
