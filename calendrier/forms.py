from django import forms
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode

class URLForm(forms.Form):
    url = forms.URLField(label='URL du Calendrier iCal')

    def clean_url(self):
        url = self.cleaned_data['url']
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query, keep_blank_values=True)

        # Modifier la valeur de 'nbWeeks' à '52'
        query_params['nbWeeks'] = ['52']

        # Reconstruire l'URL avec les nouveaux paramètres de requête
        new_query_string = urlencode(query_params, doseq=True)
        cleaned_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query_string,
            parsed_url.fragment
        ))

        return cleaned_url