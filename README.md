# DBMS-lab

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


```sql
DELIMITER //

CREATE PROCEDURE DebitFromAccount(IN account_no VARCHAR(24))

BEGIN

    DECLARE b_balance FLOAT;

    

    -- Check if the account exists and retrieve its balance

    SELECT Balance INTO b_balance

    FROM Accounts

    WHERE Account_id = account_no;

    

    -- Debit Rs. 2000 if the account has a minimum balance of Rs. 500 after the debit

    IF b_balance >= 2500 THEN

        UPDATE Accounts

        SET Balance = Balance - 2000

        WHERE Account_id = account_no;

        

        SELECT 'Rs. 2000 debited successfully from account ' AS Message, balance from Accounts where Account_id = account_no;

    ELSE

        SELECT 'Insufficient balance to perform the transaction.' AS Message;

    END IF;

END //
```

```sql
DELIMITER //



CREATE PROCEDURE TransferAmount(

    IN p_sender_id VARCHAR(24),     

    IN p_receiver_id VARCHAR(24),  
    
    IN p_receiver_name VARCHAR(5),

    IN p_transfer_amount FLOAT     

)

BEGIN

    DECLARE v_sender_balance FLOAT;     

    DECLARE v_receiver_balance FLOAT;   

    

    -- Check if sender and receiver accounts exist and retrieve their balances

    SELECT Balance INTO v_sender_balance

    FROM Accounts

    WHERE Account_id = p_sender_id;

    

    SELECT Balance INTO v_receiver_balance

    FROM Accounts

    WHERE Account_id = p_receiver_id and Name = p_receiver_name;

    

    -- Check if sender and receiver accounts exist and their balances are retrieved

    IF v_sender_balance IS NOT NULL AND v_receiver_balance IS NOT NULL THEN

        -- Transfer amount if sender has sufficient balance

        IF v_sender_balance >= p_transfer_amount THEN

          

            UPDATE Accounts

            SET Balance = Balance - p_transfer_amount

            WHERE Account_id = p_sender_id;

            

            -- Credit to receiver

            UPDATE Accounts

            SET Balance = Balance + p_transfer_amount

            WHERE Account_id = p_receiver_id;

            

            SELECT 'Transfer of Rs. ', p_transfer_amount, ' from account ', p_sender_id, ' to account ', p_receiver_id, ' successful.' AS Message;

        ELSE

            SIGNAL SQLSTATE '45000'

            SET MESSAGE_TEXT = 'Insufficient balance in account ' ;

        END IF;

    ELSE

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT = 'Invalid account number or name.';

    END IF;



END//
```

```sql
For table creation and data insertion:

create table Accounts(Account_id varchar(255), Name varchar(255),Balance float);

insert into Accounts values ('AC 001','A',5000),('AC 002','B',10000),('AC 003','D',5000),('AC 004','E',2000),('AC 005','C',250);
```