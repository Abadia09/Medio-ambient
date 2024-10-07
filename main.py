import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola como estas soy un bot que te ayuda a cuidar el Medio Ambiente  \n ,Como quieres ayudar al Medio Ambiente:\n ,1- Reducir el consumo de agua (agua) \n , 2- Reducir el consumo de basura (basura) \n , 3- Reducir el cosumos de recursos no aprobechables (consumo) \n , 4- Quieres hacer una campaña o leccion (campaña)')


@bot.command()
async def agua(ctx):
    await ctx.send(f'Para reducir el uso del agua:\n  Cierra el grifo mientras te lavas los dientes \n  Repara fugas de agua \n  Realiza duchas mas cortas \n  Cuando vas a lavar el carro utiliza un balde con solo el agua que vayas a utilizar no una manguera')    
    lista_imagene = os.listdir('agua')
    imagen_seleccionada = random.choice(lista_imagene)
    with open(f'agua/{imagen_seleccionada}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def basura(ctx):
    await ctx.send(f'Para reducir el uso de la basura debemos: \n  Los plasticos como botellas, podemos reutalizarlos haciendo manualidades \n  Puedes donar las tapas de las botellas para que la reutilizen \n  Cajas donarlas a fundaciones ejemplo: animales les hacen casas y mas cosas ')
    lista_imagenes = os.listdir('basura')
    imagen_seleccionada = random.choice(lista_imagenes)
    with open(f'basura/{imagen_seleccionada}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def campaña(ctx):
    await ctx.send(f'Aquí te presento algunas ideas para hacer una campaña de cuidado del medio ambiente dirigida a jóvenes: \n1. Utiliza redes sociales: Los jóvenes están muy activos en las redes sociales, así que crea contenido atractivo y compartible para concienciar sobre la importancia del cuidado del medio ambiente.\n2. Organiza eventos y actividades: Realiza actividades prácticas como limpiezas de parques o playas, talleres de reciclaje, etc.\n3. Crea un movimiento: Anima a los jóvenes a unirse a una causa común, como reducir el uso de plásticos o ahorrar energía.\n4. Colabora con influencers: Invita a influencers jóvenes a unirse a la campaña y compartir su compromiso con el medio ambiente.\n5. Educa y conciencia: Ofrece información y recursos para que los jóvenes entiendan la importancia del cuidado del medio ambiente.\n6. Hazlo divertido: Incorpora elementos lúdicos y creativos para que los jóvenes se sientan atraídos y comprometidos con la causa.\n7. Involucra a la comunidad: Anima a los jóvenes a involucrar a sus familias y comunidades en la campaña.\n8. Establece metas y desafíos: Establece objetivos y desafíos para que los jóvenes trabajen juntos para lograrlos.\n9. Reconoce y premia: Reconoce y premia a los jóvenes que se destacan en la campaña para motivar a otros.\n10. Sé constante: Mantén la campaña activa y continua para que el mensaje se mantenga vivo.\nRecuerda, la clave es hacer que los jóvenes se sientan parte de la solución y no solo del problema.¡Buena suerte!')
    lista_imagenes = os.listdir('campaña')
    imagen_seleccionada = random.choice(lista_imagenes)
    with open(f'campaña/{imagen_seleccionada}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("")
