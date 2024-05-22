#puedo borrar codigo sin miedo a perder lo que tenía
import module
import mod_feat_01 as m01
import feat_02 as m02
import feat_03 as f03

d = ((50 + 23 - 60) * module.f + m01.i)/2 #importar variable de otro fichero creado por mi
print(f'Mi valor es => {d}')

d2 = m02.sumatoria(12, 4, 6, 9, 45)
print(f'La sumatoria es {d2}')

fact = m02.factorial(5)
print(f'5! = {fact}')

f = 44 #esto va a generar un cnflicto, si la modifico aqui y en la rama master, debido a que ha sido modificada en ambas partes
print(f + f03.var1)

print('Este codigo se ha modificado, en el repositorio remoto')