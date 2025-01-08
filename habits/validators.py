from rest_framework.serializers import ValidationError


def time_validator(value):
    if value >= 120:
        raise ValidationError("Ошибка: время на привычку должно быть не больше 120 секунд")
    return value


def period_validator(value):
    if value < 0 or value > 7:
        raise ValidationError("Ошибка: привычка должна выполняться хотя бы раз в неделю.")
    return value


class PleasantHabitValidator:

    def __call__(self, value):
        if dict(value).get("pleasant_habit"):
            if dict(value).get("related_habit") or dict(value).get("reward"):
                raise ValidationError("Ошибка: невозможно существование, одновременно, у приятной привычки"
                                      "награды или связанной привычки.")


class RelatedHabitValidator:
    def __call__(self, value):
        valid_related_habit = dict(value).get("related_habit")
        if valid_related_habit and not valid_related_habit.pleasant_habit:
            raise ValidationError("Ошибка: связанная привычка не является приятной.")


class RewardRelatedHabitValidator:
    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        if dict(value).get(self.related_habit) and dict(value).get(self.reward):
            raise ValidationError("Ошибка: не может существовать, одновременно, за выполнение"
                                  "привычки - награда и связанная привычка")
