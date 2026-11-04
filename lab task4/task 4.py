def employee(**kwargs):
    for key, value in\
            kwargs.items():
        print(key,":" , value)
employee(name ="Areesha" , age = 20, salary= 5000000, department = "artifical intelligence")

