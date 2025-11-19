def no_notes(a):
    Q = [1000, 500, 200, 100, 50, 40, 20, 10, 5, 1]
    x = 0
    for i in range(10):
        q = Q[i]
        x = a//q
        print("notes of {} = {}".format(q, x))
        a = a%q
amount = int(input("Enter the amount: "))
no_notes(amount)        