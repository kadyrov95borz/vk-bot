1) Чтобы запустить данный скрипт на компьтере, нужно:
	1. Установить Python 3 с официального сайта https://www.python.org/downloads
	
	2. Открыть cmd и выполнить команды:
		pip install vk_api
		pip install python3-anticaptcha
	При возникновении ошибки добавьте параметр --user:
		pip install --user vk_api
		pip install --user python3-anticaptcha
		
	3. Открыть файл main.py и заменить в 4-ой строчке слово ТОКЕН на токен аккаунта вк, на который вы ставите бота.
	Чтобы получить токен, нужно перейти по ссылке https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 нажать "разрешить" и скопировать в адресной строке все, что идёт после access_token= до &
	4. Запустить файл main.py через ide, которая установилась у вас вместе с Python 3 или через командную строку:
		python путь до файла
		
		Пример: python c:/example/main.py
	
	(Файлы main.py и bot.py обязательно должны находиться в одной папке)

2) Чтобы запустить данный скрипт на хостинге, нужно:
	1. Зарегистрироваться на сайте pythonanywhere.com
	2. Перейти в раздел Files и загрузить на сайт файлы main.py и bot.py (обязательно в одну папку)
	3. Перейти в разлел Consoles и в блоке Start a new console выбрать bash
	4. В открывшейся консоли выполнить команды:
		pip3.8 install --user vk_api
		pip3.8 install --user python3-anticaptcha
		
		После этого данную консоль можно будет закрыть в разделе Consoles
	5. Перейти в раздел Files и выполнить пункт 1.3
	6. Нажать кнопку Run

3) Дополнительно:
	1. Чтобы получить идентификатор голосового сообщения, нужно перейти на сайт http://hereme.pythonanywhere.com, заполнить поля токен и id, загрузить на сайт аудиофайл, который вы хотите использовать как голосовое сообщение. Проделав все эти действия, нажмите на кнопку "Загрузить" и скопируйте идентификатор вашего голосового сообщения.
	2. Чтобы подключить антикаптчу, нужно зарегистрироваться на сайте https://anti-captcha.com, пополнить счёт на минимально возможную сумму (этого должно хватить на долго), скопировать api ключ в настройках аккаунта и вставить его в файле main.py, где написано КЛЮЧ ОТ АНТИКАПТЧИ (4-я строка).
	3. Чтобы бот упомянул в своём сообщении пользователя, на чьё сообщение он отвечает, нужно добавить переменную name в шаблон.
		Пример:
			"Привет, {name}!"
	4. Чтобы бот отправил конкретный стикер после отправки конкретного сообщения с шаблоном/вложением/голосовым сообщением, нужно добавить параметр sticker_ids к шаблону или идентификатору вложения\голосового сообщения.
		Примеры:
			Шаблон: "Какой-то текст {sticker_ids[60, 19657, 64]}" // 60, 19657, 64 - это id стикеров, из которых случаиным образом будет выбран тот, стикер которого будет отправлен после сообщения с текстом "Какой-то текст". Узнать id стикера можно, например, с помощью бота https://vk.com/im?sel=-170091052
			Вложение: "photo530941218_457262715 {sticker_ids[60, 19657, 64]"
			голосовое сообщение: "doc599521094_554607859 {sticker_ids[60, 19657, 64]}"
		ВНИМАНИЕ!!! Параметр sticker_ids должен быть указан перед параметром delay при его наличии.
	5. Чтобы изменить задержку перед отправкой конкретного сообщения с шаблоном/вложением/голосовым сообщением, нужно добавить параметр delay к шаблону или идентификатору вложения\голосового сообщения. Если параметр delay не указан, то при отправке сообщения будет использоваться стандартное значение параметра delay, котороё равняется 5.
		Примеры:
			Шаблон: "Какой-то текст {delay: 10}" // В данном случае бот отправит сообщение с текстом "Какой-то текст" через 10 секунд
			Вложение: "photo530941218_457262715 {delay: 11}" // Значение параметра delay в данном случае будет округлено до 15
			Голосовое сообщение: "doc599521094_554607859 {delay: 0}" // В данном случае голосовое сообщение будет отправлено без какой-либо задержки
		ВНИМАНИЕ!!! Параметр delay должен быть указан после параметра sticker_ids при его наличии.
	6. К одному шаблону/идентификатору вложения/идентификатору голосового сообщения можно добавить несколько параметров при условии, что параметр sticker_ids будет указан до параметра delay.
		Пример:
			Шаблон: "Привет, {name}! {sticker_ids: [20012]} {delay: 10}"
