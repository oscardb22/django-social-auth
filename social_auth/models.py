from django.conf import settings

MODELS = getattr(settings, 'SOCIAL_AUTH_MODELS', 'social_auth.db.django_models')

if MODELS == 'social_auth.db.django_models':
    from social.apps.django_app.default.models import UserSocialAuth as UserSocialAuthBase
    from social.apps.django_app.default.models import Nonce as NonceBase
    from social.apps.django_app.default.models import Association as AssociationBase
    from social.apps.django_app.default.models import DjangoStorage as DjangoStorageBase
else:
    from social.apps.django_app.me.models import UserSocialAuth as UserSocialAuthBase
    from social.apps.django_app.me.models import Nonce as NonceBase
    from social.apps.django_app.me.models import Association as AssociationBase
    from social.apps.django_app.me.models import DjangoStorage as DjangoStorageBase


class UserSocialAuth(UserSocialAuthBase):
    class Meta:
        proxy = True


class Nonce(NonceBase):
    class Meta:
        proxy = True


class Association(AssociationBase):
    class Meta:
        proxy = True


class DjangoStorage(DjangoStorageBase):
    user = UserSocialAuth
    nonce = Nonce
    association = Association
