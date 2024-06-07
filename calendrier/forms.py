from django import forms
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode

from icalendar import Calendar
from django.core.exceptions import ValidationError
import requests


class URLForm(forms.Form):
    url = forms.URLField(label='URL du Calendrier iCal')

    def clean_url(self):
        # url = self.cleaned_data['url']
        # parsed_url = urlparse(url)
        # query_params = parse_qs(parsed_url.query, keep_blank_values=True)
        #
        # # Modifier la valeur de 'nbWeeks' à '52'
        # query_params['nbWeeks'] = ['52']
        #
        # # Reconstruire l'URL avec les nouveaux paramètres de requête
        # new_query_string = urlencode(query_params, doseq=True)
        # cleaned_url = urlunparse((
        #     parsed_url.scheme,
        #     parsed_url.netloc,
        #     parsed_url.path,
        #     parsed_url.params,
        #     new_query_string,
        #     parsed_url.fragment
        # ))
        try:
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

            response = requests.get(cleaned_url)
            response.raise_for_status()  # S'assurer que la requête a réussi

            # Vérifier si le contenu est bien un fichier iCal
            cal = Calendar.from_ical(response.content)
        except Exception as e:
            raise ValidationError("L'URL fournie ne semble pas être celle d'un iCal valide.")

        return cleaned_url
