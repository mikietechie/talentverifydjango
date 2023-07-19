from django.urls import path

from app.views import user, company, department, employee, employment, auth, options, uploads


urlpatterns = [
    # MODELS CRUD
    path("auth/", auth.UserView.as_view()),
    path("user/", user.UserList.as_view()),
    path("user/<int:pk>/", user.UserDetail.as_view()),
    path("company/", company.CompanyList.as_view()),
    path("company/<int:pk>/", company.CompanyDetail.as_view()),
    path("department/", department.DepartmentList.as_view()),
    path("department/<int:pk>/", department.DepartmentDetail.as_view()),
    path("employee/", employee.EmployeeList.as_view()),
    path("employee/<int:pk>/", employee.EmployeeDetail.as_view()),
    path("employment/", employment.EmploymentList.as_view()),
    path("employment/<int:pk>/", employment.EmploymentDetail.as_view()),
    # FORM OPTIONS
    path("company/form/", options.company_form),
    path("employment/form/", options.employment_form),
    # UPLOADS
    path("upload/", uploads.upload),
]
