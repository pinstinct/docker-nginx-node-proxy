FROM        hm07/front
MAINTAINER  dev@abc.com


WORKDIR     /srv/app/django_app
EXPOSE      4567
CMD ["supervisord", "-n"]