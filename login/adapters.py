from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class EmailNotAllowedException(Exception):
    pass


class RestrictEmailAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        email = sociallogin.account.extra_data.get('email').lower()

        if email.endswith('esiee.fr'):
            return True
        raise EmailNotAllowedException("Seules les adresses email 'esiee.fr' sont acceptées.")
