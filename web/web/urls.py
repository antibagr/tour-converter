from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from account import views as account_views


urlpatterns = [
    path('', include('pages.urls')),
    path('me/', include('account.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('signup/', account_views.sign_up, name='account-sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='account/profile/login.html'), name='login'),
    path('logout/', account_views.custom_logout, name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='account/profile/password_reset.html'),
        name='password_reset'
    ),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='account/profile/password_reset_done.html'),
        name='password_reset_done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/profile/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/profile/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
