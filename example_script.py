from pos_integrado import posIntegrado

p = posIntegrado()
p.auto_select_port()

print(p.pos_execute('TES'))
#print(p.pos_execute('TAR', index=3))
#print(p.pos_execute('ULT'))
#print(p.pos_execute('ULC',index=3)) #reinicia el equipo 
#print(p.pos_execute('CIE')) #Error a reintentar cerrar 
"""

print(p.pos_execute('VEN', amount=300, invoice=1, instaments=1, tip=0,
                    card_code='VI', plan=0,commerce='03659307',
                    commerce_name='pruebas', cuit='00-00000000-0', line_mode='\x01'))
"""



#print (p.tes())
"""


print(p.pos_execute('PRI'))
"""

#print(p.pos_execute('CIE'))
