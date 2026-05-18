from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('manager/loan-requests/', views.loan_request_list, name='loan_request_list'),
    path(
        'manager/loan-requests/<int:request_id>/complete/',
        views.complete_loan_request,
        name='complete_loan_request'
    ),
    path(
        'manager/loan-requests/<int:request_id>/delete/',
        views.delete_loan_request,
        name='delete_loan_request'
    ),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('update-isbn-status/', views.update_isbn_status, name='update_isbn_status'),


    # AJAX 저장용
    path('<int:pk>/like/', views.book_like, name='book_like'),
    path('<int:pk>/reviews/add/', views.review_add, name='review_add'),
    path('<int:pk>/loan/', views.loan_book, name='loan_book'),
]
