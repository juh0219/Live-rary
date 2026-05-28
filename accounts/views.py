from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from books.models import Loan

class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # 1. 폼을 통해 User 객체를 안전하게 먼저 저장 (username, first_name, email 자동 저장됨)
        response = super().form_valid(form)
        user = self.object

        # 2. 학번(username)을 학생증 도서관 번호(library_code)로 연동하여 Profile 생성
        Profile.objects.create(
            user=user,
            library_code=user.username  # 학번 데이터 그대로 입력
        )
        return response

@login_required
def my_page(request):
    # 현재 대출중(반납 안 됨)인 것만 가져와서 2개 슬롯에 넣기
    active_loans = (
        Loan.objects
        .select_related("book")
        .filter(user=request.user, returned_at__isnull=True)
        .order_by("loaned_at")[:2]
    )

    loan1 = active_loans[0] if len(active_loans) > 0 else None
    loan2 = active_loans[1] if len(active_loans) > 1 else None

    context = {
        "user_obj": request.user,
        "loan1": loan1,
        "loan2": loan2,
    }
    return render(request, "accounts/my_page.html", context)
