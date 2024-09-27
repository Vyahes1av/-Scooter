import random
class Urls:
    base_url = 'https://qa-scooter.praktikum-services.ru'
    main_page = f'{base_url}/'
    order_page = f'{base_url}/order'
    redirected_page = "https://dzen.ru/?yredirect=true"


class TextQuestion:

    Text_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    Text_2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    Text_3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    Text_4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    Text_5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    Text_6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    Text_7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    Text_8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class OrderData:
    Head_page = 'Для кого самокат'
class MainData:
    Head_page = 'Вопросы о важном'

class Desing:
    Name = f"Слава"
    Surname = f"Питерский"
    Address =f"Уллица Пушкина {random.randint(1,99)}"
    Number = f"8931{random.randint(0000000, 9999999)}"
    Comment =f"Позвонить за 30 минут"
