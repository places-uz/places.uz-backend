from django.urls import path

from users.views.sign_in import SignInView, RefreshTokenView
from users.views.sign_out import SignOutView
from users.views.sign_up import SignUpView
from users.views.users import UsersListView, UserSettingsView, ChangePasswordView


urlpatterns = [
    path('sign-in', SignInView.as_view(), name='signin'),
    path('sign-up', SignUpView.as_view(), name='signup'),
    path('sign-out', SignOutView.as_view(), name='signout'),
    path('user', UsersListView.as_view(), name='user-list'),
    path('user_settings', UserSettingsView.as_view(), name='user-settings'),
    path('change_password', ChangePasswordView.as_view(), name='change-password'),
    path('refresh', RefreshTokenView.as_view(), name='reset-password'),
]
