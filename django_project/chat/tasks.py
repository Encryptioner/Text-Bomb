from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_project.celery import app
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# REPORT_TEMPLATE = """
# Here's how you did till now:

# {% for post in posts %}
#         "{{ post.title }}": viewed {{ post.view_count }} times |

# {% endfor %}
# """

REPORT_TEMPLATE = """
Number of total users registered in last hour = {{ cnt }}

Thank You for staying with us.

Sincierly,

"""


@app.task
def send_view_count_report():

    usr_dates = User.objects.all().values_list('date_joined')

    hour_count = datetime.now() - timedelta(hours=1)

    data = []
    cnt = 0

    for u in usr_dates:
        data.append(str(u[0]))

    for i in range(0, len(data)):
        s = data[i]
        p = s[0:18]
        d = datetime.strptime(p, "%Y-%m-%d %H:%M:%S")
        if d > hour_count:
            cnt = cnt + 1

    for user in get_user_model().objects.all():

        template = Template(REPORT_TEMPLATE)

        send_mail(
            'Hello Dear, ',
            template.render(context=Context({'cnt': cnt})),
            'from@Text-Bomb.dev',
            [user.email],
            fail_silently=False,
        )


# @app.task
# def send_view_count_report():
#     for user in get_user_model().objects.all():
#         posts = Post.objects.filter(author=user)
#         if not posts:
#             continue

#         template = Template(REPORT_TEMPLATE)

#         send_mail(
#             'Your QuickPublisher Activity',
#             template.render(context=Context({'posts': posts})),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )
