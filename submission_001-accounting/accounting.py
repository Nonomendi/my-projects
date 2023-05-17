"""TODO"""

import user.authentication as auth
import transactions.journal as j1
# import banking.reconciliation as b1
import banking.fvb.reconciliation as fvb1
# import banking.ubsa.reconciliation as ubsa1
# import banking.online.reconciliation as online
import sys


if __name__ == "__main__":
    mends=sys.argv
    if len(mends) > 1:
        for i in mends:
            if i != "accounting.py":
                print(i)

    auth.authenticate_user()
    j1.receive_income(100)
    j1.pay_expense(100)
    # b1.do_reconciliation()
    fvb1.do_reconciliation()
    # ubsa1.do_reconciliation()
    # online.do_reconciliation()