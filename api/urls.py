from django.urls import path
from .views.crew_views import CrewsView, CrewDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('crews/', CrewsView.as_view(), name='crews'),
    path('crews/<int:pk>/', CrewDetailView.as_view(), name='crew_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-password/', ChangePasswordView.as_view(), name='change-pw')
]
