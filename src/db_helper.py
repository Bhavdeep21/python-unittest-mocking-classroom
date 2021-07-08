import mysql.connector
from getpass import getpass
class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        try:
            conn=mysql.connector.connect(user="*****", password="******", host="localhost", database="employees")
            cur=conn.cursor()
            cur.execute("select salary from salaries order by salary desc limit 1")
            ans=[]
            for i in cur.fetchall():
                ans.append(i[0])
        
        except mysql.connector.Error as e:
            print(e)
        finally:
            conn.close()
        return ans[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        try:
            conn=mysql.connector.connect(user="******", password="******", host="localhost", database="employees")
            cur=conn.cursor()
            cur.execute("select salary from salaries order by salary asc limit 1")
            ans=[]
            for i in cur.fetchall():
                ans.append(i[0])
        
        except mysql.connector.Error as e:
            print(e)
        finally:
            conn.close()
        return ans[0]

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)