import asyncio
import time


async def call():
    print('Начался звонок....')
    await asyncio.sleep(5)
    print('Звонок закончился.')

async def prin_pos():
    print('Пришёл посетитель')
    await asyncio.sleep(2)
    print('Посетитель ушёл.')

async def grafiks():
    print('Начало работы с графиками')
    await asyncio.sleep(2)
    print('Работа с графиками завершена.')
async def aeroticket():
    print('Выбор авиабилетов')
    await asyncio.sleep(5)
    print('Авиабилет куплен.')
async def documents():
    print('Начало заполнения')
    await asyncio.sleep(3)
    print('Документы заполнены.')

async def main():
    print('9:00')
    await prin_pos()
    print('10:00')
    await asyncio.gather(aeroticket(),documents())
    print('11:00')
    await call()
    print('12:00')
    await grafiks()
    print('13:00')
    await asyncio.gather(aeroticket(),documents())

asyncio.run(main())