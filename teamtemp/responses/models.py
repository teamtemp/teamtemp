import django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


from teamtemp import utils


def make_uuid():
    return utils.random_string(8)


class User(models.Model):
    id = models.CharField(max_length=8, primary_key=True)


class TeamTemperature(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=make_uuid())
    creation_date = models.DateField()
    creator = models.ForeignKey(django.contrib.auth.models.User)

    def stats(self):
        result = dict()
        responses = self.temperatureresponse_set.all()
        result['count'] = responses.count()
        result['average'] = responses.aggregate(models.Avg('score'))
        result['words'] = responses.values('word').annotate(models.Count("id")).order_by()
        return result

    def __unicode__(self):
        return u"{}: {} {}".format(self.id, self.creator.id,
                                   self.creation_date)


class TemperatureResponse(models.Model):
    request = models.ForeignKey(TeamTemperature)
    responder = models.ForeignKey(User)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Temperature (1-10)')
    word = models.CharField(
        max_length=32,
        verbose_name="One word to describe how you're feeling",
        validators=[RegexValidator(regex='^[A-Za-z0-9\'-]+$',
                                   message="please enter a single word with alphanumeric characters only.",
                                   code='Invalid Word')])

    def __unicode__(self):
        return u"{}: {} {} {} {}".format(self.id, self.request.id,
                                         self.responder.id,
                                         self.score, self.word)
