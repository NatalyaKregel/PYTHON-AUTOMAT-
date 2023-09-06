import logging
logging.basicConfig(filename='my_func2.log', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)

def get_num(num):
    while num > 0:
        try:
            if num < 10:
                res = num ** 2
                logger.info(f'квадрат числа {num} = {res}')
            elif 9 < num < 100:
                first_number = num // 10
                second_number = num % 10
                res = first_number * second_number
                logger.info(f'произведение чисел {first_number} и {second_number} = {res}')
            else:
                first_number = num // 100
                second_number = num % 100 // 10
                third_number = num % 10
                res = (third_number * 100) + (second_number * 10) + first_number
                logger.info(f'зеркальное отражение чисел {first_number} и {second_number} и {third_number} = {res}')
            return res

        except ZeroDivisionError as exp:
            logger.error(f'число должно быть > 0 ')
            return float('inf')
    else:
        logger.error(f'введенное число должно быть > 0 ')
        return float('inf')

if __name__ == '__main__':
    get_num(2)
    get_num(45)
    get_num(158)
    get_num(0)

