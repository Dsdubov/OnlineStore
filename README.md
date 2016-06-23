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
1. Корзина, с функциональностью
2. Регистрация
3. Добавление товаров в корзину зарегестрированным (и не зарегестрированным) пользователем
4. Возможность сделать заказ
5. Материал дизайн!
6. Проверка статуса товара
7. Отправление email при заказе на почту админа
16. Добавить Wishlist
4. Поработать над шаблона material design, изменить стартовую страницы, страницы каталого и продуктов подумать над тем, где и как разместить навигацию
14. Сделать переход из cart на последнюю страницу (return to shopping)
2. Менять картинку favorite в зависимости от того, добавлен ли товар уже в вишлист (javascript, function), сделать иконку с количеством товаров в wishlist
2. Допилить верхнее меню сайта
5. Добавить комментарии на сайте описания продукта
8. Поиск по сайту (по продуктам)
10. Показывать в статус баре количество элементов в корзине
1. add Breadcrumbs and Paginations
2. Всплывающее оповещее об отсутствии товара
2. Сделать различный вид для grid и list

##TODO:
6. Возможность интеренет оплаты (API PayPal)
3. Сообщение о том, что заказа с таким номером нет
12. Добавить всплвающие оповещение, об отсутствии ProductDetail, и другом
7. Добавить возможность ранжирования продуктов по параметру, на странице списка продуктов (добавить в панель)
8. Сделать страницу профиля
1. ДОбавить обработку количества товара, если его нет, или выбрано слишком много
1. Обрабатывать text overflow в названиях
11. Логаут более удобный
9. Различные промоакции
17. Сделать на странице продуктов подбор велосипеда по праметрам

###Пробный сайт находится здесь 
http://buybike.pythonanywhere.com/