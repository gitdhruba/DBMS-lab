# DBMS-lab

```markdown
# DBMS Lab PL/SQL Examples

This document contains PL/SQL examples for MySQL.

## Procedure to Calculate Factorial

This procedure calculates the factorial of a given number.

```sql
delimiter //
create procedure fact()
begin
    declare n int default 7;
    declare res int default 1;
    while n > 0 do
        set res=res*n;
        set n=n-1;
    end while;
    select res;
end //
call fact //
```

## Procedure to Reverse a Number

This procedure reverses a given number.

```sql
delimiter //
create procedure rev()
begin
    declare rev int default 0;
    declare n int default 5369;
    while n > 0 do
        set rev = rev * 10 + mod(n,10);
        set n = floor(n/10);
    end while;
    select rev;
end //
call rev() //
```

## Procedure to Generate Fibonacci Series

This procedure generates a Fibonacci series.

```sql
delimiter //
create procedure fibo()
begin
    declare n int default 5;
    declare a int default 0;
    declare b int default 1;
    declare fib int;
    while n > 0 do
        select a as fibonacci;
        set fib = a + b;
        set a = b;
        set b = fib;
        set n = n - 1;
    end while;
end //
call fibo() //
```

## Procedure to Calculate Area of Circles

This procedure calculates the area of circles with varying radii.

```sql
delimiter //
create procedure area()
begin
    declare pi double default 3.14;
    declare ar double default 0.0;
    declare i int default 3;

    create table ar(radius int,area double);

    while i < 8 do
        set ar = pi * i * i;
        insert into ar values (i,ar);
        set i = i + 1;
    end while;
    select * from ar;
end //
call area() //
```
```