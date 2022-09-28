from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import json
import time, datetime, pytz


class Parser:
	def __init__(self, group):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		self.url = "https://rasp.dmami.ru"
		self.group = group
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
		self.dates = self._get_dates_from_file()
		self.soup = self._get_soup()


	def _get_dates_from_file(self):
		with open("dates.json", encoding='utf-8') as file:
			return json.load(file)


	def _get_soup(self):
		self.driver.get(self.url)														# переход по ссылке
		time.sleep(1)
		self.driver.find_element(By.CLASS_NAME, 'groups').send_keys(self.group)			# поиск текстового поля и заполнение его номером группы
		time.sleep(1)
		try:
			self.driver.find_element(By.ID, self.group).click()							# нажатие на кнопку с группой
		except(Exception):
			return "polomalos'"
		time.sleep(1)
		html = self.driver.page_source													# сохранить страницу с расписанием в переменную
		return BS(html, 'lxml')


	def _get_pair_dates(self, pair):
		date_pair_start, date_pair_end = pair.find(class_='schedule-dates').text.split('-')						# получаем время начала и конца пары в формате строки
		date_pair_start, date_pair_end = date_pair_start.strip().split(), date_pair_end.strip().split()			# получить даты начала и конца пары, тк на сайте могут быть указаны пары, которых еще или уже нет
		
		pair_start_date_year = self.dates[date_pair_start[1]][1]												# по месяцу получить год начала пары
		pair_start_date_month = self.dates[date_pair_start[1]][0]												# по месяцу получить месяц начала пары в числовом формате
		pair_start_date_day = int(date_pair_start[0])															# получить число начала пары
		date_start = datetime.datetime(pair_start_date_year, pair_start_date_month, pair_start_date_day)		# сформировать дату для дальнейшего сравнения

		pair_end_date_year = self.dates[date_pair_end[1]][1]													# по месяцу получить год конца пары
		pair_end_date_month = self.dates[date_pair_end[1]][0]													# по месяцу получить месяц конца пары в числовом формате
		pair_end_date_day = int(date_pair_end[0])																# получить число конца пары
		date_end = datetime.datetime(pair_end_date_year, pair_end_date_month, pair_end_date_day)				# сформировать дату для дальнейшего сравнения
		return date_start, date_end


	def _get_current_local_time(self):
		current_time = pytz.utc.localize(datetime.datetime.now())
		return datetime.datetime(current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute)



	def get_next_pair(self):
		if self.soup != "polomalos'":
			pairs = self.soup.find(class_='schedule-day_today').find_all(class_='pair')								# получить расписание на сегодня
			for pair in pairs:
				current_time = self._get_current_local_time()
				date_start, date_end = self._get_pair_dates(pair)
				if current_time >= date_start and current_time <= date_end:										# узнать, есть ли пара в расписании
					pair_time = pair.find(class_='time').text.split('-')[0]										# получить время пары (9:00 - 10:40)
					time_start = pair_time.split(':')

					time_start_in_minutes = int(time_start[0]) * 60 + int(time_start[1])						# перевести время начала пары в минуты
					current_time_in_minutes = current_time.hour * 60 + current_time.minute 						# перевести текущее время в минуты
					time_to_pair = time_start_in_minutes - current_time_in_minutes								# посчитать время до начала пары
					if time_to_pair > 0 and time_to_pair < 16:
						pair_rooms = " ".join([room.text for room in pair.find_all(class_="schedule-auditory")])
						pair_name = pair.find(class_="bold").text
						pair_teacher = pair.find(class_="teacher").text
						return f"Пара через {time_to_pair} минут\n{pair_rooms}\n{pair_name}\n{pair_teacher}"
			return "Cегодня нет пар"
		else:
			return "Введена неверная группа!"


if __name__ == "__main__":
	parser = Parser("211-321")
	print(parser.get_next_pair())
