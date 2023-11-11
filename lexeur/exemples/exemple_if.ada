with TEXT_IO; use TEXT_IO;

PROCEDURE IfSamples IS BEGIN
   age : Integer := 32309 ;
   IF age = 200 THEN
      PUT_LINE ("La condition est vrai");
   END IF;
END IfSamples;