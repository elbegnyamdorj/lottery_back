from lottery.models import Lottery
import csv


def run():
    Lottery.objects.all().delete()
    with open('lottery/lottery.csv', "r", encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        lotteries = []
        count = 0
        for row in data:
            lottery = Lottery(
                lottery_number=row[0], 
                date=row[1], 
                name = row[2], 
                plate_number = row[3],
                phone_number=row[4]
            )
            lotteries.append(lottery)
            if len(lotteries) > 5000:
                Lottery.objects.bulk_create(lotteries)
                print(count*5000)
                lotteries = []
                count = count+1
        if lotteries:
            Lottery.objects.bulk_create(lotteries)

