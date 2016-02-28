# OnlineStore

## Проект Дубова Дмитрия
## Группа
НИУ-ВШЭ, Факультет Компьютернх Наук, Отделение Прикладной Математики и Информатики, группа 144
## Описание
Будет создан магазин велосипедов, запчастей и акссесуаров к нему. Сервис будет состять из: витрины/каталога товаров, разбитых по категориям; корзины, в которую пользователь может добавлять покупки; для электронных товаров реализована возможность скачать (или получить по почте) и оплата с помощью PayPal (наиболее простой для интеграции, для проекта достаточно показать работу с разработческим апи PayPal) или другими системами оплаты. Для неэлектронных товаров будет возможность указать их наличие, при покупке количество изменяется. В магазине могут быть промоакции: скидка при оформлении заказа по промокоду, скидка при заказе на определенную сумму, временная скидка на конкретную категорию товаров.
## Структура сайта
Сайт будет состоять из главной страницы, на которой будут находиться каталоги различных видов продукции. (Велосипеды, акссесуары, запчасти и др.)
Каждый каталог будет состоять из ращличных категорий. (например для велосипедов: горные, городские, шоссейнике и т.п.). Каждая категория будет уже состоять из различных продуктов. Нажав на продукт, можно будет перейти на его описание.
На странице продуктов, а таже в описании продукта, можно будет добавлять продукт в корзину. (так же будет отображаться количество товара, которое осталось в магазине).
При заказе товара, пользователь сможет вводить значение промокода, если имеется, и получать скидку при оплате. Оплата будет возможно при помощи paypal.
##Прототип интерфейса
[interface](https://github.com/Dsdubov/OnlineStore/blob/master/interface.png)

<img src="https://github.com/Dsdubov/OnlineStore/blob/master/interface.png" alt="Pull" />
##Диаграмма деятельности покупки товара
[diagramm](https://github.com/Dsdubov/OnlineStore/blob/master/buy_product.png)

<img src="https://github.com/Dsdubov/OnlineStore/blob/master/buy_product.png" alt="Pull" />
##Done:
Корзина, с функциональностью
Регистрация
Добавление товаров в корзину зарегестрированным (и не зарегестрированным) пользователем
Возможность сделать заказ
Материал дизайн! статуса товара
Проверка
##TODO:
Количество товаров на сервере +-
Допилить верхнее меню сайта +-
Добавить возможность ранжирования продуктов по параметру, на странице списка продуктов
Добвить комментарии на сайте описания продукта
Отправление email при заказе на почту админа +
Возможность интеренет оплаты (API PayPal)
Различные промоакции
Поиск по сайту
ПОказывать в статус баре количество элементов в корзине
Логаут более удобный
add Breadcrumbs and Paginations
Добавить всплвающие оповещение, об отсутствии ProductDetail, и другом
ДОбавить обработку количества товара, если его нет, или выбрано слишком много
Сделать переход после логина обратно на страницу откуда перешл на login
Сделать переход из cart на последнюю страницу
Изменить страницу заказа
Сообщение о том, что заказа с таким номером нет
ПОработать над шаблона material design, изменить стартовую страницы, страницы каталого и продуктов подумать над тем, где и как разместить навигацию
Сделать на странице продуктов выбор продуктов по праметрам
Добавить Wishlist
###Пробный сайт находится здесь 
http://buybike.pythonanywhere.com/