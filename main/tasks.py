from celery import shared_task
from datetime import datetime, timedelta
from main.models import Habit
from main.services import MyBot

my_bot = MyBot()


@shared_task
def send_message():
    """Отправка уведомления пользователю о привыче за 2 минуты, до ее совершения"""

    for habit in Habit.objects.filter(pleasant=False):
        habit_datetime = datetime.combine(datetime.today(), habit.time)
        time_habit = habit_datetime - timedelta(minutes=2)

        if time_habit.time().hour == datetime.now().time().hour and \
                time_habit.time().minute == datetime.now().time().minute:
            message = f'Не забудьте о своей привычке: "{habit.action}". Время: {habit.time}, место: {habit.place}'
            my_bot.send_message(chat_id=849900865, text=message)
