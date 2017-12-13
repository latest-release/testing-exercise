#  accounts.py
#  
#  Copyright 2017 Wangolo Joel <wangolo@wangolo-OptiPlex-390>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from typing import List 
from typing import Dict 
from typing import Tuple 
from typing import Any
import random 

class BankAccount(object):
    """
    Objects handles bank account details
    for a particular user.
    """
    def __init__(self, firstname, lastname, sex, dob, age): # type: (...) -> None
        # type: (str, str, str, str, int)
        
        self.firstname = firstname 
        self.lastname = lastname
        self.sex = sex
        self.dob = dob
        self.age = age 
        
        self.is_loggedin = False
        
    def create_account(self, **kwargs): # type: (...) -> Any
        # type: ( Any) 
        
        if not kwargs:
            return "AccountName: {}  | AccountNumber {} ".format(self.get_bothnames(), self.generate_account_number())
        
    def get_bothnames(self):# type(...) -> Any
        """
        Returns both names combined.
        """
        return "{} {}".format(self.firstname, self.lastname) 
    
    def generate_account_number(self, length=50): # type: (...) -> int 
        # type: ( int )
        """
        Generates  a random account number.
        """
        if not length:
            return random.getrandbits(len(self.get_bothnames())) # Generate based on user name length
        return random.getrandbits(length)

class AccountOperations(BankAccount):
    """
    Extends from BankAccount to get ready made
    features.
    """
    def __init__(self, firstname, lastname, sex, dob, age, **kwargs):# type:(...) -> None
        # type: (str, str, str, str, int, Any)
        super(AccountOperations, self).__init__(firstname, lastname, sex, dob, age)
        
        self.names = self.get_bothnames() # type: str
        self.account = self.create_account() # type: str
        self.current_balance=float(500000) # type: str 
    
    def withdraw(self, amount): # type:(...) -> float
        # type:(Any)
        """
        Widthraw funds from user account.
        """
        if not amount:
            # We can't withdraw nothing
            raise ValueError("We can't width zero get serious!")
        
        if(amount > self.get_balance()):
            return 0
        
        self.current_balance = self.current_balance-amount 
        return float(self.current_balance)
        
      
    def get_balance(self): # type:(...) -> None
        """
        Return user balance.
        """
        return self.current_balance
        
