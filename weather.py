from pyowm import OWM
from config import token
from decor import logger


@logger
def get_temperature(city, token):
    """
    Функция, возвращающая погодные условия конкретного города
    """
    owm = OWM(token)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    detail = w.detailed_status
    wind = w.wind()
    hum = w.humidity
    temp = w.temperature('celsius')
    return f"Погодные условия в Донецке:\n {temp},\n {detail},\n {wind},\n {hum}"


if __name__ == '__main__':
    print(get_temperature('Donetsk,UA', token))