from rest_framework.response import Response
from rest_framework import generics
import lottery
from .serializers import *
from .models import *
import csv, io
from rest_framework.views import APIView
class LotteryView(generics.CreateAPIView):
    serializer_class = LotterySerializer
    queryset = Lottery.objects.all()

    def get(self, request):
        lottery = Lottery.objects.all().order_by('-id')[:70] 
        count = Lottery.objects.all().count()
        serializers = LotterySerializer(lottery, many = True)

        result = {
            'lottery': serializers.data,
            'count': count
        }
        return Response(result)
    
    def create(self, request, *args, **kwargs):
        csv_file = request.FILES['myFile']
        
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        lottery_list=[]
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            lottery_list.append(Lottery(lottery_number=column[0], date=column[1], name = column[2], plate_number = column[3], phone_number=column[4]))
        Lottery.objects.bulk_create(lottery_list, batch_size=100000)
        print('done')
        return Response({'status':'success'})

class LotteryChecker(APIView):
    def get(self, request, number, *args, **kwargs):
            
            # lottery = Lottery.objects.values('lottery_number', 'phone_number')
            count = Lottery.objects.filter(lottery_number__endswith=number).count()
            if count < 1000:
                lottery = Lottery.objects.filter(lottery_number__endswith=number).values().order_by('-lottery_number')[:70] 
                result = {
                'lottery': lottery,
                'count': count
                }
                return Response(result)
            
            lottery = Lottery.objects.filter(lottery_number__endswith=number).values('lottery_number').order_by('-lottery_number')[:70] 
            result = {
            'lottery': lottery,
            'count': count
            }
            return Response(result)


            # print(lottery)
            # lottery_list = list(lottery)
            # length = len(number)
            # final_list=[]
            # for i in lottery_list:
            #     lottery_number = i['lottery_number']
            #     lot_num_digits = lottery_number[10-length:10]
            #     if lot_num_digits == number:
            #         final_list.append(i)
    

class LotteryDelete(generics.RetrieveDestroyAPIView):
    serializer_class = LotterySerializer
    queryset = Lottery.objects.all()
    def get(self, request, *args, **kwargs):
        lottery = Lottery.objects.all()
        serializers = LotterySerializer(lottery, many = True)
        return Response(serializers.data)
    def delete(self, request, *args, **kwargs):
        Lottery.objects.all().delete()
        return Response({'status':'success'})