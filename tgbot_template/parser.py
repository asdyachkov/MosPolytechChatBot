# https://rasp.dmami.ru/site/group?group=211-327&session=0


from selenium import webdriver
import time, datetime, pytz
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS

# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100")

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(exutable_path="E:\\code/ChatBotPolytech\\tgbot_template\\driver\\chromedriver.exe")


month = {
	'Янв': [1, 2023],
	'Фев': [2, 2023],
	'Мар': [3, 2023],
	'Апр': [4, 2023],
	'Май': [5, 2023],
	'Июн': [6, 2023],
	'Июл': [7, 2023],
	'Авг': [8, 2023],
	'Сен': [9, 2022],
	'Окт': [10, 2022],
	'Ноя': [11, 2022],
	'Дек': [12, 2022]
}

driver.get("https://rasp.dmami.ru")
# driver.get("https://whatmyuseragent.com")
time.sleep(1)
best_group = "211-321"
login = driver.find_element(By.CLASS_NAME, 'groups').send_keys(best_group)
time.sleep(1)

gropup = driver.find_element(By.ID, best_group).click()
time.sleep(1)
src = driver.page_source
soup = BS(src, 'lxml')

pairs = soup.find(class_='schedule-day_today').find_all(class_='pair')
for pair in pairs:

	actual_date_of_pair_start, actual_date_of_pair_end = pair.find(class_='schedule-dates').text.split('-')
	current_time = pytz.utc.localize(datetime.datetime.now())

	current_now = datetime.datetime(current_time.year, current_time.month, current_time.day)
	date_start = datetime.datetime(month[actual_date_of_pair_start.strip().split(' ')[1]][1], month[actual_date_of_pair_start.strip().split(' ')[1]][0], int(actual_date_of_pair_start.strip().split(' ')[0]))
	date_end = datetime.datetime(month[actual_date_of_pair_end.strip().split(' ')[1]][1], month[actual_date_of_pair_end.strip().split(' ')[1]][0], int(actual_date_of_pair_end.strip().split(' ')[0]))

	if current_now >= date_start and current_now <= date_end:
		time_start = pair.find(class_='time').text.split('-')[0]
		tmp = time_start.split(':')
		time_start_in_minutes = int(tmp[0]) * 60 + int(tmp[1])

		current_time_in_minutes = current_time.hour * 60 + current_time.minute

		diff = time_start_in_minutes - current_time_in_minutes
		


