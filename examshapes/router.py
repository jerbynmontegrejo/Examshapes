from account.viewsets import AccountViewset
from shapes.viewsets import ShapesViewset
# from myshapescomputation.viewsets import MyShapesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('account', AccountViewset)
router.register('shapes', ShapesViewset)
# router.myshapes('my-shapes', MyShapesViewset)
