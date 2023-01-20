Select * from employees order by FIRST_NAME ; 

Select FIRST_NAME, lAST_NAME, SALARY, COMMISSION_PCT from employees where COMMISSION_PCT = 0.15 ; 

Select sum(salary) from employees ;

Select max(salary), min(salary) from employees ;

Select avg(salary), count(EMPLOYEE_ID) from employees ;