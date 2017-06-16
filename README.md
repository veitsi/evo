ЗАДАЧА №1
Сделать оптимизатор данных для шаблонов. Шаблон задается в виде строки форматирования x = "Some text: {some_dict[text]}". Её можно отформатировать помощью `x.format(**data)`. Но, вместо этого, вам нужно написать функцию `optimize_data()` которая вернёт минимальный словарь с данными, которые используются в шаблоне. Словарь может быть произвольной вложенности. Используйте `string.Formatter().parse` для разбора строки. Достаточно поддержки переменных верхнего уровня и словарей (квадратные скобки в шаблоне, как в примере выше).
Ссылка на тесты https://git.io/vHIB2 (тесты запускать с помощью `pytest`)
Дополнительные задания (выполнять необязательно, по твоему желанию)
1. Напишите интерактивный режим 
2. Добавьте тестов 
3. Реализуйте поддержку списков (test_list_keys) 
4. Реализуйте поддержку аттрибутов объектов (test_objects)