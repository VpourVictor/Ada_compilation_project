with Ada.Text_IO ; use Ada.Text_IO ;
[284, (285, 'Ada'), 46, (285, 'Text_IO'), 59, 282, (285, 'Ada'), 46, (285, 'Text_IO'), 59,

procedure unDebut is
 274, (285, 'unDebut'), 267
    function aireRectangle(larg : integer; long : integer) return integer is
    264, (285, 'aireRectangle'), 40, (285, 'larg'), 58, (285, 'integer'), 59(20), (285, 'long'), 58, (285, 'integer'), 41, 277, (285, 'integer'), 267
    aire: integer;
    (285, 'aire'), 58, (285, 'integer'), 59(31),
    begin
     258,
        aire := larg * long ;
        (285, 'aire'), 58, 61, (285, 'larg'), 42, (285, 'long'), 59,
    return aire
    277, (285, 'aire'),
    end aireRectangle ;
    261, (285, 'aireRectangle'), 59,

    function perimetreRectangle(larg : integer; long : integer) return integer is
    264, (285, 'perimetreRectangle'), 40, (285, 'larg'), 58, (285, 'integer'), 59, (285, 'long'), 58, (285, 'integer'), 41, 277, (285, 'integer'), 267
    p : integer
    112, 58, (285, 'integer'),
    begin
    258
        p := larg*2 + long*2 ;
         112, 58, 61, (285, 'larg'), 42, 50, 43, (285, 'long'), 42, 50, 59,
    return p
    277, 112,
    end perimetreRectangle;
    261, (285, 'perimetreRectangle'), 59,

        -- VARIABLES
choix : integer ;
(285, 'choix'), 58, (285, 'integer'), 59,

        -- PROCEDURE PRINCIPALE
begin
258,
    choix := 2;
    (285, 'choix'), 58, 61, 50, 59,

    if choix = 1
    265, (285, 'choix'), 61, 49,
        then valeur := perimetreRectangle(2, 3) ;
        279, (285, 'valeur'), 58, 61, (285, 'perimetreRectangle'), 40, 50, 44, 51, 41, 59,
            put(valeur) ;
            (285, 'put'), 40, (285, 'valeur'), 41, 59,
        else valeur := aireRectangale(2, 3) ;
        259, (285, 'valeur'), 58, 61, (285, 'aireRectangale'), 40, 50, 44, 51, 41, 59,
            put(valeur) ;
            (285, 'put'), 40, (285, 'valeur'), 41, 59,
    end if;
    261, (285, 'if'), 59,
end unDebut ;
261, (285, 'unDebut'), 59]