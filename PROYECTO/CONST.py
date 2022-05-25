#ELEMENTOS QUE SE UTILIRAZAN PARA EL RECONOCIMIENTO DEL LÉXICO

MATRIZ_ESTADO = [
     #0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27
    [212, 24,200,121,102,103,  9, 10,106,107,108,109, 11, 12, 14, 15, 16, 17, 18, 20,120,  1, 13,212,212,  0,  0,212],#0
    [  2,  8,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200],#1
    [  2,200,  5,  3,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,100,200,200,200,200,200,100],#2
    [  4,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201],#3
    [  4,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,100,201,201,201,201,201,100],#4
    [  6,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200],#5
    [  6,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,100,201,201,201,201,201,100],#6
    [200,  7,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200],#7
    [  8,  8,202,202,202,202,202,202,202,202,202,202,202,  8,202,202,202,202,202,202,202,101,202,202,  8,202,202,101],#8
    [207,207,207,207,207,207,104,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,104],#9
    [208,208,208,208,208,208,208,105,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,105],#10
    [122,122,122,122,122,122,122,122,122,122,122,122,110,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122],#11
    [123,123,123,123,123,123,123,123,123,123,123,123,123,111,123,123,123,123,123,123,123,123,123,123,123,123,123,111],#12
    [209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,209,112,209,209,209,209,112],#13
    [210,210,210,210,210,210,210,210,210,210,210,210,210,210,113,210,210,210,210,210,210,210,210,210,210,210,210,113],#14
    [211,211,211,211,211,211,211,211,211,211,211,211,211,211,211,114,211,211,211,211,211,211,211,211,211,129,129,114],#15
    [203,203,203,203,203,203,203,203,203,203,203,203,203, 25,203,115,203,203,203,203,203,203,203,203,203,128,128,115],#16
    [204,204,204,204,204,204,204,204,204,204,204,204,204,204,204,116,204,204,204,204,204,204,204,204,204,127,127,116],#17
    [205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205, 19,205,205,205,205],#18
    [205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,117,205,205,205,205,205,205,205,205,117],#19
    [206,206,206,206, 23,206,206,206,206,206,206,206,206,206,206, 21,206,206,206,118,206,206,206,206,206,206,206,118],#20
    [206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,119,206,206,206,206,206,206,206,119],#21
    [207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,207,107],#22
    [208,208,208,208,208,124,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,208,124],#23
    [213, 24,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,213,125,125,213],#24
    [203,203,203,203,203,203,203,203,203,203,203,203,203,203,203,203,126,203,203,203,203,203,203,203,203,130,130,130]#25

]

#LETRAS DISPONIBLES EN EL LENGUAJE
LETRAS = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#TODOS LOS DIGITOS QUE SE PUEDEN USAR EN EL LENGUAJE
DIGITOS = ["1","2","3","4","5","6","7","8","9","0"]


COLUMNAS_MATRIZ={
    **dict(zip(LETRAS, [1]*26)),
    **dict(zip(DIGITOS, [0]*10)),
    '.': 2,
    'E': 3,
    '{': 4,
    '}': 5,
    '[': 6,
    ']': 7,
    '(': 8,
    ')': 9,
    '*': 10,
    '/': 11,
    '+': 12,
    '-': 13,
    '&': 14,
    '=': 15,
    '<': 16,
    '>': 17,
    '~': 18,
    ':': 19,
    ';': 20,
    '$': 21,
    '|': 22,
    '!': 23,
    '_': 24,
    ' ': 25,
    '\n':26,
    'F': 27
}

PALABRAS_RESERVADAS =[
    "constants",
    "true",
    "false",
    "number",
    "real",
    "sequence",
    "logical",
    "list",
    "beginning",
    "finishing",
    "on",
    "that",
    "loop",
    "into",
    "to",
    "condition",
    "do",
    "while",
    "cycle",
    "texto",
    "numero",
    "in",
    "consecutive",
    "repeat",
    "occurrence",
    "write",
    "input",
    "break",
    "instance",
    "variables"
]

ESTADOS_FINALES={
    100: "RECONOCE: NÚMEROS",
    101: "RECONOCE: IDENTIFICADORES",
    102: "RECONOCE: {",
    103: "RECONOCE: }",
    104: "RECONOCE: [[",
    105: "RECONOCE: ]]",
    106: "RECONOCE: (",
    107: "RECONOCE: )!",
    108: "RECONOCE: *",
    109: "RECONOCE: /",
    110: "RECONOCE: ++",
    111: "RECONOCE: --",
    112: "RECONOCE: ||",
    113: "RECONOCE: &&",
    114: "RECONOCE: ==",
    115: "RECONOCE: <=",
    116: "RECONOCE: >=",
    117: "RECONOCE: ~!~",
    118: "RECONOCE: ::",
    119: "RECONOCE: :=:",
    120: "RECONOCE: ;",
    121: "RECONOCE: ϵ",
    122: "RECONOCE: +",
    123: "RECONOCE: -",
    124: "RECONOCE: {}",
    125: "RECONOCE: PALABRAS RESERVADAS",
    126: "RECONECE: <-<",
    127: "RECONECE: >",
    128: "RECONECE: <",
    129: "RECONECE: =",
    130: "RECONOCE: <-"


}

ESTADOS_ERROR={
    200: "ERROR SE ESPERABA  DIGITO",
    201: "ERROR SE ESPERABA  DIGITOS",
    202: "ERROR SE ESPERABA  letra|digito|_|-|",
    203: "ERROR SE ESPERABA  =,-,< ",
    204: "ERROR SE ESPERABA  =",
    205: "ERROR SE ESPERABA  !, ~",
    206: "ERROR SE ESPERABA  =,:,{",
    207: "ERROR SE ESPERABA  [",
    208: "ERROR SE ESPERABA  ]",
    209: "ERROR SE ESPERABA  |",
    210: "ERROR SE ESPERABA  &",
    211: "ERROR SE ESPERABA  =",
    212: "ERROR CARACTER INVALIDO",
    213: "ERROR SE ESPERABA  ESPACIO, SALTO DE LINEA, LETRA"
}


MATRIZ_SINTACTICA = [
# 0	   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51   
[  1,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#0
[301, 16,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 16,301,301,301,301,301,301,301,301,301, 16, 16,301,301,301,301, 16, 16,301, 16, 16, 16, 16, 16,301,301, 15,301,301],#1
[301,  4,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,  3,301,301,301,301,301,301,301,301,301,  4,  4,301,301,301,301,  4,  4,301,  4,  4,  4,  4,  4,301,301,  4,301,301],#2
[301, 36,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 35, 35,301,301,301,301, 35, 35,301, 35, 35, 35, 35, 35, 35,301,301,301,301],#3
[301,  6,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,  5,  5,  5,  5,  5,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#4
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,  7,  7,  7,  7,  7,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#5
[301,  9,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,  8,  8,  8,  8,  8,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#6
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 19, 20, 21, 22, 23,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#7
[ 14,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 10, 11,301, 12, 13,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#8
[ 48,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#9
[301, 18,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 17,301,301,301,301],#10
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 24,301,301,301,301],#11
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 27,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 30,301,301,301,301],#12
[ 40,301,301,301, 41,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 41,301, 41, 41,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 41,301,301,301,301],#13
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 44,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 43,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#14
[ 29,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 28,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#15
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 26, 26, 26, 26, 26,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 25,301,301,301,301],#16
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 32,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#17
[ 31,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#18
[301, 34,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 33,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#19
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 38, 39,301,301, 55,301, 56, 54,301, 57, 58, 59, 60, 61, 62,301,301,301,301],#20
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 37,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#21
[301,301,301,301, 68,301,301,301,301,301,301,301,301,301,301,301,301,301, 69,301,301,301, 70,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 70,301,301,301,301],#22
[ 48,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#23
[301,301,301,301, 78,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 78,301, 78, 78,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 78,301,301,301,301],#24
[301,301,301,301,301,301,301,301,301,301, 76, 77, 71, 73, 72, 75, 74,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#25
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 45,301,301,301,301],#26
[ 46,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 47,301,301,301,301],#27
[301,301,301,301,301,301,301,301, 64, 65,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#28
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 51,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 50,301,301,301,301],#29
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 49,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 49,301,301,301,301],#30
[301, 53,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 52,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 52,301,301,301,301],#31
[301, 67,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 301,66,301,301,301],#32
[301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 63,301,301,301,301],#33
[301,301,301,301, 82,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 82,301, 82, 82,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 82,301,301,301,301],#34
[301,301,301,301,301,301,301,301, 79, 80, 81, 81, 81, 81, 81, 81, 81,301,301,301, 81,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301],#35
[301,301,301,301,301, 85, 83, 84, 85, 85, 85, 85, 85, 85, 85, 85, 85,301,301,301, 85,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 85,301,301,301,301],#36
[301,301,301,301, 86,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 88,301, 89, 90,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301,301, 87,301,301,301,301]#37
]

#SE DEFINE UNA LIISTA VACIA YA QUE NO EXISTE LA PRODUCCIÓN 0 E INICIE EN EL 1
PRODUCCIONES=[
[],
["{", "SECCION_VARIABLES","SECCION_CONSTANTES","SECCION_ESTATUTO","}"],
["constants", "::", "{","DECLARACION_CONSTANTES", "}", "SECCION_CONSTANTES"],
["EPSILON"],
["LISTA_CONSTANTE", "DECLARACION_CONSTANTES"],
["EPSILON"],
["TIPO", "identificador", "<-", "VALOR", "LISTAPRIMACONSTANTES"],
["LISTA_CONSTANTE"],
["EPSILON"],
["texto"],
["numero"],
["true"],
["false"],
["LISTAVALORES"],
["variables", "::", "{", "DECLARACION_VARIABLES", "}", "SECCION_VARIABLES"],
["EPSILON"],
["LISTA","TIPO","DECLARACION_VARIABLES"],
["EPSILON"],
["number"],
["real"],
["sequence"],
["logical"],
["list"],
["identificador","EXTRA", "LISTAPRIMA"],
["LISTA"],
["EPSILON"],
[":=:", "NUMERO_ LISTA_NUMEROS"],
["NUMEROS"],
["LISTA_NUMEROS"],
["EPSILON"],
["{", "NUMEROS", "}"],
["numero", "LISTANUMERO"],
[";", "NUMEROS"],
["EPSILON"],
["ESTATUTO",";", "SECCION_ESTATUTOS"],
["EPSILON"],
["beginning", "ESTATUTOS", "finishing"],
["on","condition", "that", "CONDICION", "CUERPOESTATUTOS"],
["loop", "{", "identificador", "INTO", "EXTRA2","}"],
["LISTAVALORES", "}", "CUERPOESTATUTOS"],
["EXPRESION", "identificador", "OPERADOR", "EXPRESION", "INCREDECRE", "}"],
["LISTAORANGO", "}", "CUERPOESTATUTOS"],
["into"],
["<-<"],
["identificador","SIGNO"],
["{", "IDENTIFICADOROVALOR", "to", "IDENTIFICADOROVALOR", "}"],
["identificador"],  
["{", "LISTA_VALORES", "}"],
["IDENTIFICADOROVALOR", "LISTAVALORESPRIMA"],
["identificador"],
["número"],
["LISTA_VALORES"],
["EPSILON"],
["while", "CONDICION", "CUERPOESTATUTOS"],
["do", "CUERPOESTATUTOS", "while", "loop", "CONDICION"],
["cycle", "while", "identificador", "consecutive", "LISTAORANGO", "CUERPOESTATUTOS"], 
["repeat", "CUERPOESTATUTOS", "CONDICION"],
["occurrence", "identificador", "{","LISTAOCURRENCE","}"],
["write","{","IDENTIFICADOROVALOR","}"],
["input", "{", "identificador", "}"],
["break"],
["ASIGNACION"],
["identificador", ":=:", "EXPRESION"],
["++"],
["--"],
["instance", "numero", "CUERPOESTATUTOS", "LISTAOCURRENCE"],
["EPSILON"],
["(", "EXPRESION", "OPERADOR", "EXPRESION",")"],
["~!~", "(", "EXPRESION", "OPERADOR", "EXPRESION",")"],
["IDENTIFICADOROVALOR", "in", "[[", "IDENTIFICADOROVALOR", "to", "IDENTIFICADOROVALOR", "]]"],
["="],
[">"],
["<"],
[">="],
["<="],
["||"],
["&&"],
["TERMINO","EXPPRIMA"],
["+", "TERMINO", "EXPPRIMA"],
["-", "TERMINO", "EXPPRIMA"],
["EPSILON"],
["FACTOR", "TERMPRIMO"],
["*", "FACTOR", "TERMPRIMO"],
["/", "FACTOR", "TERMPRIMO"],
["EPSILON"],
["(", "EXPRESION", ")"],
["identificador"],
["numero"],
["true"],
["false"]
]

TERMINALES= ["{","}","[","]","(",")","*","/","+","-","||",
            "&&","=","<",">","<=",">=","<-<","~!~",":=:",";",
            "texto","numero","constants","true","false","number",
            "real","sequence", "logical", "list", "beginning", "finishing",
            "on","loop","into","to","do","condition","cycle",
            "while","consecutive","repeat","occurrence","write","input",
            "break","identificador","instance","variables","in","that"]

NO_TERMINALES= ["P",
"SECCION_VARIABLES",
"SECCION_CONSTANTES",
"SECCION_ESTATUTOS",
"DECLARACION_CONSTANTES",
"LISTA_CONSTANTE",
"LISTAPRIMACONSTANTES",
"TIPO",
"VALOR",
"LISTAVALORES",
"DECLARACION_VARIABLES", 
"LISTA",
"EXTRA",
"EXTRA2",
"INTO",
"NUMERO_LISTA_NUMEROS",
"LISTAPRIMA",
"NUMEROS", 
"LISTA_NUMEROS",
"LISTANUMERO",
"ESTATUTO",
"CUERPOESTATUTOS",
"CONDICION",
"LISTAVALORES",
"EXPRESION",
"OPERADOR",
"INCREDECRE",
"LISTAORANGO",
"SIGNO",
"IDENTIFICADOROVALOR",
"LISTA_VALORES",
"LISTAVALORESPRIMA",
"LISTAOCURRENCE", 
"ASIGNACION",
"TERMINO",
"EXPRIMA",
"TERMPRIMO",
"FACTOR"
]