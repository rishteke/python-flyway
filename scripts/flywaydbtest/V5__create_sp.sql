DELIMITER &&  
CREATE PROCEDURE get_addition_procedure ()  
BEGIN  
    set @a = 1;
    set @b = 10;
    select @a + @b;    
END &&  
DELIMITER ; 