from rest_framework import serializers

from habits.models import Habit
from habits.validators import time_validator, period_validator, PleasantHabitValidator, RelatedHabitValidator, \
    RewardRelatedHabitValidator


class HabitBaseSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[time_validator])
    period = serializers.IntegerField(validators=[period_validator])

    class Meta:
        model = Habit
        exclude = ["owner"]
        validators = [
            PleasantHabitValidator(),
            RelatedHabitValidator(),
            RewardRelatedHabitValidator(related_habit="related_habit", reward="reward"),
        ]


class HabitPublicSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField(read_only=True)

    def get_is_owner(self, obj):
        request = self.context.get("request")
        if request and request.user == obj.owner:
            return "Личная привычка пользователя"
        return "Публичная привычка"

    class Meta:
        model = Habit
        fields = ("id", "action", "time", "place", "period", "time_to_complete", "created_at", "pleasant_habit",
                  "reward", "is_owner")
