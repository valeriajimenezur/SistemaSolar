from vpython import *

ventana=canvas(title='Sistema Solar',width=1500, height=600, center= vec(0,5,0),background=vec(0.01,0.01,0.1))

Sol = sphere(pos=vec(0,0,0), radius=50, color = color.yellow,  texture='https://i.imgur.com/XdRTvzj.jpg')
mercurio = sphere(pos=vec(-200,0,0), radius=4, make_trail = True,trail_color=color.gray(0.5), texture = 'https://i.imgur.com/YttpWJD.jpg')
venus = sphere(pos=vec(-230,0,0), radius=5,  make_trail = True,trail_color=vec(0.6,0.6,0.7), texture = 'https://i.imgur.com/7VTEX2w.jpg')
tierra = sphere(pos=vec(-260,0,0), radius=5, make_trail = True, trail_color=vec(0,0.4,0.9), texture = textures.earth)
marte = sphere(pos=vec(-290,0,0), radius=4.8, make_trail = True, trail_color=vec(0.6,0.1,0.1),  texture = 'https://i.imgur.com/Mwsa16j.jpg')
jupiter = sphere(pos=vec(-320,0,0), radius=10, make_trail = True, trail_color=vec(0.9,0.7,0.6), texture = 'https://i.imgur.com/KbVscNb.jpg')
saturno = sphere(pos=vec(-350,0,0), radius=10, make_trail = True,trail_color=vec(0.8,0.6,0.5), texture = 'https://i.imgur.com/r9h0U9E.jpg')
urano = sphere(pos=vec(-380,0,0), radius=7,  make_trail = True,trail_color=vec(0,0.5,0.7), texture = 'https://i.imgur.com/2kZNvFw.jpeg')
neptuno = sphere(pos=vec(-410,0,0), radius=7, make_trail = True,trail_color=vec(0,0,0.7), texture = 'https://i.imgur.com/lyLpoMk.jpeg')

mercuriov = vec(0,0,4.5)
venusv = vec(0,0,4.5)
tierrav = vec(0,0,4.5)
martev = vec(0,0,4.5)
jupiterv = vec(0,0,4.5)
saturnov = vec(0,0,4.5)
uranov = vec(0,0,4.5)
neptunov = vec(0,0,4.5)


while True:
    rate(60)
    
    mercurio.pos = mercurio.pos + mercuriov
    Distancia = (mercurio.pos.x**2 + mercurio.pos.y**2 + mercurio.pos.z**2)**0.5
    Unitario = (mercurio.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    mercuriov = mercuriov + FuerzaG
    mercurio.pos = mercurio.pos + mercuriov
    

    venus.pos = venus.pos + venusv
    Distancia = (venus.pos.x**2 + venus.pos.y**2 + venus.pos.z**2)**0.5
    Unitario = (venus.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    venusv = venusv + FuerzaG
    venus.pos = venus.pos + venusv
    

    tierra.pos = tierra.pos + tierrav
    Distancia = (tierra.pos.x**2 + tierra.pos.y**2 + tierra.pos.z**2)**0.5
    Unitario = (tierra.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    tierrav = tierrav + FuerzaG
    tierra.pos = tierra.pos + tierrav
    

    marte.pos = marte.pos + martev
    Distancia = (marte.pos.x**2 + marte.pos.y**2 + marte.pos.z**2)**0.5
    Unitario = (marte.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    martev = martev + FuerzaG
    marte.pos = marte.pos + martev
    

    jupiter.pos = jupiter.pos + jupiterv
    Distancia = (jupiter.pos.x**2 + jupiter.pos.y**2 + jupiter.pos.z**2)**0.5
    Unitario = (jupiter.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    jupiterv = jupiterv + FuerzaG
    jupiter.pos = jupiter.pos + jupiterv
    
    
    saturno.pos = saturno.pos + saturnov
    Distancia = (saturno.pos.x**2 + saturno.pos.y**2 + saturno.pos.z**2)**0.5
    Unitario = (saturno.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    saturnov = saturnov + FuerzaG
    saturno.pos = saturno.pos + saturnov
    

    urano.pos = urano.pos + uranov
    Distancia = (urano.pos.x**2 + urano.pos.y**2 + urano.pos.z**2)**0.5
    Unitario = (urano.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    uranov = uranov + FuerzaG
    urano.pos = urano.pos + uranov
    

    neptuno.pos = neptuno.pos + neptunov
    Distancia = (neptuno.pos.x**2 + neptuno.pos.y**2 + neptuno.pos.z**2)**0.5
    Unitario = (neptuno.pos - Sol.pos)/Distancia
    FuerzaG = -10000*Unitario/Distancia**2
    neptunov = neptunov + FuerzaG
    neptuno.pos = neptuno.pos + neptunov
