from django.shortcuts import render

# Create your views here.
def index(request):
    from django.utils import timezone
    from dateutil.relativedelta import relativedelta
    start_date = timezone.now()
    end_date = timezone.now() + relativedelta(days=1)
    return render(request, 'index.html',
                  {
                      'start_date': start_date.strftime('%m/%d/%Y'),
                      'end_date': end_date.strftime('%m/%d/%Y'),
                  }
                  )