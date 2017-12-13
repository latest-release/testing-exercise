#  main.py
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
import accounts
import sys
import os
import time 

def run_tests():
    path = os.getcwd()
    test_file = "test_accounts.py"
    full_path = os.path.join(path, test_file)
    
    cmd = "python {}".format(full_path)
    ret_status = os.system(cmd)
    
def run_mypy():
    path = os.getcwd()
    accountfile = "accounts.py"
    full_path = os.path.join(path, accountfile)
    
    cmd = "mypy --py2 {}".format(full_path)
    ret_status = os.system(cmd)
    

if len(sys.argv) > 1:
    # We got some args.
    if(sys.argv[1] == "run"):
        print "Welcome to ---Localhost host--- Bank"
        print "Please wait while we initialize you creds for regisration"
        time.sleep(100)
    elif(sys.argv[1] == "test"):
        print "Initializing testing system please ..."
        time.sleep(2)
        run_tests()
        print "Running test done...."
        
    elif(sys.argv[1] == "mypy"):
        print "\nRunning mypy"
        run_mypy()
        print "\n done..."
        
        
