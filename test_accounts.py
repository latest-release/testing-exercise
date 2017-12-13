#  test_accounts.py
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

import unittest 
import accounts 

class TestBankAccount(unittest.TestCase):
    
    def test_account_is_none(self):
        acc = accounts.BankAccount("Wangolo", "Joel", "Male", "1993", "24")
        self.assertNotEqual( acc.create_account(), None)
    
    def test_both_names_is_str(self):
        
        acc = accounts.BankAccount("Wangolo", "Joel", "Male", "1993", "24")
        self.assertTrue(acc.get_bothnames())

    def test_generate_account_number(self):
        
        acc = accounts.BankAccount("Wangolo", "Joel", "Male", "1993", "24")
        self.assertTrue(acc.generate_account_number())
        
        self.assertFalse(acc.generate_account_number() == len(acc.get_bothnames()) )
        
    def test_withdraw(self):
        
        amount = float(5000000)
        acc = accounts.AccountOperations("Wangolo", "Joel", "Male", "1993", "24")
        #acc.withdraw(amount)
        
        self.assertTrue(acc.get_balance() == amount)

if __name__=="__main__":
    unittest.main()
